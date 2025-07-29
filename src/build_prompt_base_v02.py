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
    from field_descriptions import DESCRIPTIONS as field_descriptions
except ImportError:
    field_descriptions = {}

# --------------------------------------------------------------------------- #
# Utilities
# --------------------------------------------------------------------------- #

console = Console()

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

    def __init__(self, data: Dict[str, Any]) -> None:
        self.data = data
        self.undo_stack: List[Dict[str, Any]] = []

    def push_undo(self, section: str) -> None:
        self.undo_stack.append({section: dict(self.data[section])})

    def pop_undo(self) -> Optional[Dict[str, Any]]:
        return self.undo_stack.pop() if self.undo_stack else None

    # --------------------------------------------------------------------- #
    # Section helpers
    # --------------------------------------------------------------------- #

    def section_description(self, section: str) -> str:
        return field_descriptions.get(section, {}).get("_section", {}).get("description", "")

    def field_meta(self, section: str, field: str) -> Dict[str, Any]:
        return field_descriptions.get(section, {}).get(field, {})

    def suggest(self, section: str, field: str, current: Any) -> Any:
        if current is not None and str(current).strip():
            return current
        meta = self.field_meta(section, field)
        return meta.get("examples", [""])[0]

    # --------------------------------------------------------------------- #
    # Interactive field loop
    # --------------------------------------------------------------------- #

    def edit_section(self, section: str) -> None:
        sec_data: Dict[str, Any] = self.data[section]
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
                nav.next()
                continue
            else:  # Accept new value
                new_value = Prompt.ask("Enter value", default=str(suggestion))
                sec_data[field] = new_value
                nav.next()

            # Auto-save
            save_json(self.data, ARGS.output)

# --------------------------------------------------------------------------- #
# Entrypoint
# --------------------------------------------------------------------------- #

def main() -> None:
    global ARGS
    parser = argparse.ArgumentParser(description="Interactive prompt builder")
    parser.add_argument("-i", "--input", required=True, help="Base JSON file")
    parser.add_argument("-o", "--output", default="prompt_simple.json", help="Output JSON file")
    ARGS = parser.parse_args()

    data = load_json(ARGS.input)

    key_sections = ["subject", "character", "composition", "setting",
                    "lighting", "style", "rendering", "colorPlate"]

    builder = PromptBuilder(data)

    console.print("[bold green]Welcome to the Step-by-Step Prompt Builder![/bold green]")
    console.print("Use [yellow]arrow keys[/yellow] or shortcuts. [red]q[/red] to quit.\n")

    for sec in key_sections:
        if sec not in data:
            continue
        builder.edit_section(sec)

    save_json(data, ARGS.output)
    console.print("[bold green]All done! Enjoy your prompt.[/bold green]")

if __name__ == "__main__":
    main()