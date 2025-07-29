#!/usr/bin/env python3
"""
Interactive prompt builder for AI image generation.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any, Dict, List, Optional

from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns

try:
    from field_descriptions import DESCRIPTIONS as field_descriptions, MANDATORY_FIELDS
except ImportError:
    field_descriptions = {}
    MANDATORY_FIELDS: list[str] = []

# --------------------------------------------------------------------------- #
# Utilities
# --------------------------------------------------------------------------- #

console = Console()

def ensure_mandatory_fields(data: Dict[str, Any]) -> None:
    """
    Guarantee that all paths listed in MANDATORY_FIELDS exist in *data*.
    Arrays are initialised with a single element when the path component
    ends with '[]'.  Missing leaf nodes are initialised with an empty
    string so that the user can fill them interactively.
    """
    for path in MANDATORY_FIELDS:
        cursor: Any = data
        parts = path.split(".")
        for i, raw_part in enumerate(parts):
            is_array = raw_part.endswith("[]")
            key = raw_part[:-2] if is_array else raw_part

            # Handle last part
            if i == len(parts) - 1:
                if is_array:
                    cursor.setdefault(key, [{}])
                else:
                    cursor.setdefault(key, "")
                break

            # Handle intermediate part
            if is_array:
                cursor.setdefault(key, [{}])
                cursor = cursor[key][0]
            else:
                cursor.setdefault(key, {})
                cursor = cursor[key]

def load_json(path: str) -> Dict[str, Any]:
    try:
        with open(path, encoding="utf-8") as fp:
            return json.load(fp)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        console.print(f"[red]Cannot load {path}: {e}[/red]")
        sys.exit(1)

def save_json(data: Dict[str, Any], path: str) -> None:
    with open(path, "w", encoding="utf-8") as fp:
        json.dump(data, fp, indent=2, ensure_ascii=False)
    console.print(f"[green]Saved → {path}[/green]")

# --------------------------------------------------------------------------- #
# Navigation helpers
# --------------------------------------------------------------------------- #

class Navigator:
    """
    Small state machine that lets the user move between fields
    with arrow keys or shortcuts.
    """

    def __init__(self, fields: List[str]) -> None:
        self.fields = fields
        self.index = 0

    @property
    def current(self) -> str:
        return self.fields[self.index]

    def next(self) -> bool:
        if self.index < len(self.fields) - 1:
            self.index += 1
            return True
        return False

    def prev(self) -> bool:
        if self.index > 0:
            self.index -= 1
            return True
        return False

    def goto(self, idx: int) -> None:
        self.index = max(0, min(idx, len(self.fields) - 1))

# --------------------------------------------------------------------------- #
# Core interaction
# --------------------------------------------------------------------------- #

class PromptBuilder:

    def __init__(self, data: Dict[str, Any], output_path: str) -> None:
        """
        Parameters
        ----------
        data : Dict[str, Any]
            The JSON data structure that is being edited.
        output_path : str
            Destination path for the incrementally‑saved prompt file.
        """
        self.data = data
        self.output_path = output_path
        self.undo_stack: List[Dict[str, Any]] = []

    def push_undo(self, section: str) -> None:
        self.undo_stack.append({section: dict(self.data[section])})

    def pop_undo(self) -> Optional[Dict[str, Any]]:
        return self.undo_stack.pop() if self.undo_stack else None

    # --------------------------------------------------------------------- #
    # Section helpers
    # --------------------------------------------------------------------- #

    def section_description(self, section: str) -> str:
        """
        Return the description for an entire section.  First, look for an
        exact match in *field_descriptions* (i.e. 'meta', 'subjects', etc.).
        If the entry is a simple string, return it directly.  Otherwise, keep
        backward‑compatibility with the old nested structure ( _section key ).
        """
        desc = field_descriptions.get(section, {})
        if isinstance(desc, str):
            return desc
        return desc.get("_section", {}).get("description", "")

    def field_meta(self, section: str, field: str) -> Dict[str, Any]:
        """
        Retrieve metadata (description, examples) for a given field.
        For flattened schemas, the key is '<section>.<field>'.  If not found,
        gracefully fall back to an empty dict.
        """
        flattened_key = f"{section}.{field}"
        entry = field_descriptions.get(flattened_key, {})
        if isinstance(entry, str):
            return {"description": entry}
        return entry

    def suggest(self, section: str, field: str, current: Any) -> Any:
        """
        Return a proposed value for *field*.

        Priority:
        1. If *current* is non‑empty → keep it (già validato).
        2. Otherwise pick the first example in DESCRIPTIONS, if available.
        3. Fallback: empty string.
        """
        if current is not None and str(current).strip():
            return current
        meta = self.field_meta(section, field)
        examples = meta.get("examples", [])
        return examples[0] if examples else ""

    # --------------------------------------------------------------------- #
    # Interactive field loop
    # --------------------------------------------------------------------- #

    def edit_section(self, section: str) -> None:
        sec_data_raw = self.data[section]
        # Support both dict sections and list‑based sections (e.g. subjects[])
        sec_data: Dict[str, Any]
        if isinstance(sec_data_raw, list) and sec_data_raw:
            sec_data = sec_data_raw[0]  # operate on first element
        elif isinstance(sec_data_raw, dict):
            sec_data = sec_data_raw
        else:
            console.print(f"[red]Unsupported section structure for {section}[/red]")
            return

        fields = list(sec_data.keys())
        nav = Navigator(fields)

        console.print("\n")
        console.rule(f"[bold cyan]SECTION: {section.upper()}[/bold cyan]")
        desc = self.section_description(section)
        if desc:
            console.print(Panel(desc, style="dim"))

        self.push_undo(section)

        while True:
            field = nav.current
            current = sec_data[field]
            suggestion = self.suggest(section, field, current)

            meta = self.field_meta(section, field)
            examples = meta.get("examples", [])
            description = meta.get("description", "")

            # Build rich prompt
            text = Text()
            text.append(f"\nField: [bold]{field}[/bold]\n", style="cyan")
            if description:
                text.append(f"Description: {description}\n", style="white")
            if examples:
                text.append(f"Examples: {', '.join(examples)}\n", style="white")
            text.append(f"Current / Suggested: [yellow]{current}[/yellow]  →  [green]{suggestion}[/green]\n")
            console.print(text)

            choices = {
                "": "accept suggested",
                "e": "edit / add value",
                ".": "skip / keep current",
                "r": "reset section",
                "u": "undo last change",
                "n": "next",
                "p": "previous",
                "s": "skip rest",
                "q": "quit"
            }

            cmd = Prompt.ask(
                "Choose",
                choices=list(choices.keys()),
                default="",
                show_choices=False
            ).strip()

            if cmd == "q":
                console.print("[red]Bye![/red]")
                sys.exit(0)

            elif cmd == "s":
                console.print(f"[dim]Skipping rest of section {section}[/dim]")
                return

            elif cmd == "r":
                console.print("[yellow]Resetting section...[/yellow]")
                self.data[section] = dict(self.undo_stack[-1][section])
                nav.goto(0)
                continue

            elif cmd == "u":
                undo = self.pop_undo()
                if undo:
                    sec, old = next(iter(undo.items()))
                    self.data[sec].update(old)
                    console.print("[green]Undo done.[/green]")
                    nav.goto(0)
                continue

            elif cmd == "n":
                if not nav.next():
                    console.print("[dim]Last field already[/dim]")
                continue

            elif cmd == "p":
                if not nav.prev():
                    console.print("[dim]First field already[/dim]")
                continue

            elif cmd == ".":
                # Skip / keep current
                if nav.next():
                    continue
                # Fine: last field reached → persist & exit section
                if isinstance(sec_data_raw, list) and sec_data_raw:
                    sec_data_raw[0] = sec_data
                save_json(self.data, self.output_path)
                return

            elif cmd == "":
                # Accept suggested value
                sec_data[field] = suggestion
                if nav.next():
                    continue
                # Last field processed
                if isinstance(sec_data_raw, list) and sec_data_raw:
                    sec_data_raw[0] = sec_data
                save_json(self.data, self.output_path)
                return

            elif cmd == "e":
                # Edit / add custom value
                new_value = Prompt.ask("Enter value", default=str(current))
                sec_data[field] = new_value
                if nav.next():
                    continue
                # Last field processed
                if isinstance(sec_data_raw, list) and sec_data_raw:
                    sec_data_raw[0] = sec_data
                save_json(self.data, self.output_path)
                return

            # If we edited a list entry, write back the dict into the list.
            if isinstance(sec_data_raw, list) and sec_data_raw:
                sec_data_raw[0] = sec_data

            # Auto-save
            save_json(self.data, self.output_path)

# --------------------------------------------------------------------------- #
# Entrypoint
# --------------------------------------------------------------------------- #

def main() -> None:
    parser = argparse.ArgumentParser(description="Interactive prompt builder")
    parser.add_argument("-i", "--input", default="prompt_v1.json", help="Base JSON file (default: prompt_v1.json)")
    parser.add_argument("-o", "--output", default="prompt_v1_edited.json", help="Output JSON file (default: prompt_v1_edited.json)")
    ARGS = parser.parse_args()

    data = load_json(ARGS.input)

    ensure_mandatory_fields(data)

    key_sections = sorted({part.split(".")[0].replace("[]", "") for part in MANDATORY_FIELDS})

    builder = PromptBuilder(data, ARGS.output)

    console.print("[bold green]Welcome to the Step-by-Step Prompt Builder![/bold green]")
    console.print("""[bold]Avvio[/bold]: python build_prompt_base_v02.py [green]-i[/green] prompt_v1.json [green]-o[/green] prompt_v1_edited.json

[bold]Tasti rapidi[/bold]
[cyan][Invio][/cyan] accetta suggerimento | [cyan]e[/cyan] modifica/aggiungi valore | [cyan].[/cyan] mantieni valore attuale
[cyan]r[/cyan] reset sezione | [cyan]u[/cyan] undo | [cyan]n[/cyan] next | [cyan]p[/cyan] previous
[cyan]s[/cyan] skip sezione | [cyan]q[/cyan] quit
""")

    for sec in key_sections:
        if sec not in data:
            continue
        builder.edit_section(sec)

    save_json(data, ARGS.output)
    console.print("[bold green]All done! Enjoy your prompt.[/bold green]")

if __name__ == "__main__":
    main()