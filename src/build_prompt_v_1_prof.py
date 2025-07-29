#!/usr/bin/env python3
"""
Interactive JSON-prompt builder for AI image generation.
Creates a file `prompt_out.json` that mirrors the structure
of the original prompt_v1.json (schemaVersion 1.1).
"""
import json
from typing import Any, Dict

# ------------------------------------------------------------------
# 1) Helper utilities
# ------------------------------------------------------------------
def ask(prompt: str, default: Any = None, cast=str) -> Any:
    """Ask the user for input and cast it to the required type."""
    if default is not None:
        prompt = f"{prompt} [{default}]: "
    else:
        prompt = f"{prompt}: "
    raw = input(prompt).strip()
    if raw == "" and default is not None:
        return default
    if cast == bool:
        return raw.lower() in {"y", "yes", "true", "1"}
    if cast == int:
        return int(raw)
    if cast == float:
        return float(raw)
    if cast == list:
        # comma-separated → list
        return [x.strip() for x in raw.split(",")] if raw else []
    return raw


def load_schema(path: str) -> Dict[str, Any]:
    """Load the JSON schema from a file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def edit_dict(data: Dict[str, Any], prefix: str = "") -> None:
    """Interactively edit a dictionary in-place by showing immediate keys and allowing navigation."""
    keys = list(data.keys())
    i = 0
    while i < len(keys):
        key = keys[i]
        full_key = f"{prefix}.{key}" if prefix else key
        value = data[key]
        print(f"\nCurrent field: {full_key}")
        if isinstance(value, dict):
            enter = ask(f"Do you want to edit sub-fields of '{full_key}'? (y/n)", "n", bool)
            if enter:
                edit_dict(value, full_key)
            else:
                skip = ask("Skip editing this field? (y/n)", "y", bool)
                if not skip:
                    # Allow user to re-prompt this field again by not incrementing i
                    continue
        elif isinstance(value, list):
            print(f"Editing list '{full_key}' with {len(value)} elements.")
            for idx, elem in enumerate(value):
                elem_key = f"{full_key}[{idx}]"
                if isinstance(elem, dict):
                    enter = ask(f"Do you want to edit sub-fields of '{elem_key}'? (y/n)", "n", bool)
                    if enter:
                        edit_dict(elem, elem_key)
                else:
                    new_val = input(f"Current value for {elem_key}: {elem}. Enter new value or press Enter to keep: ").strip()
                    if new_val != "":
                        data[key][idx] = new_val
            # After finishing list, ask if want to replace entire list
            replace = ask(f"Do you want to replace entire list '{full_key}'? (y/n)", "n", bool)
            if replace:
                new_list_str = input(f"Enter comma-separated values for '{full_key}': ").strip()
                data[key] = [x.strip() for x in new_list_str.split(",")] if new_list_str else []
        else:
            new_val = input(f"Current value for {full_key}: {value}. Enter new value or press Enter to keep: ").strip()
            if new_val != "":
                # Try to preserve type
                try:
                    if isinstance(value, bool):
                        data[key] = new_val.lower() in {"y", "yes", "true", "1"}
                    elif isinstance(value, int):
                        data[key] = int(new_val)
                    elif isinstance(value, float):
                        data[key] = float(new_val)
                    elif isinstance(value, list):
                        data[key] = [x.strip() for x in new_val.split(",")]
                    else:
                        data[key] = new_val
                except Exception:
                    # fallback to string if cast fails
                    data[key] = new_val
        i += 1


# ------------------------------------------------------------------
# 3) Main loop
# ------------------------------------------------------------------
def main() -> None:
    print("=== Interactive Prompt Builder ===\n")
    print("Loading schema from 'prompt_v1.json'...\n")
    prompt = load_schema("/Users/alex/Pycha/foto_prompt/files/prompt_v1.json")

    while True:
        print("\nTop-level sections:")
        keys = list(prompt.keys())
        for i, key in enumerate(keys):
            print(f"  {i + 1}. {key}")
        print("  q. Quit and save")

        choice = input("\nEnter the number of the section to edit (or 'q' to quit): ").strip()
        if choice.lower() == "q":
            break
        if not choice.isdigit():
            print("Invalid input, please enter a number or 'q'.")
            continue
        idx = int(choice) - 1
        if idx < 0 or idx >= len(keys):
            print("Invalid number, please try again.")
            continue

        section_key = keys[idx]
        section_value = prompt[section_key]
        if isinstance(section_value, dict):
            # For dict, call edit_dict to navigate immediate keys and sub-objects
            edit_dict(section_value, section_key)
        elif isinstance(section_value, list):
            print(f"\nEditing list section '{section_key}' with {len(section_value)} elements.")
            for i, elem in enumerate(section_value):
                elem_key = f"{section_key}[{i}]"
                if isinstance(elem, dict):
                    enter = ask(f"Do you want to edit sub-fields of '{elem_key}'? (y/n)", "n", bool)
                    if enter:
                        edit_dict(elem, elem_key)
                else:
                    new_val = input(f"Current value for {elem_key}: {elem}. Enter new value or press Enter to keep: ").strip()
                    if new_val != "":
                        section_value[i] = new_val
            replace = ask(f"Do you want to replace entire list '{section_key}'? (y/n)", "n", bool)
            if replace:
                new_list_str = input(f"Enter comma-separated values for '{section_key}': ").strip()
                prompt[section_key] = [x.strip() for x in new_list_str.split(",")] if new_list_str else []
        else:
            new_val = input(f"Current value for {section_key}: {section_value}. Enter new value or press Enter to keep: ").strip()
            if new_val != "":
                try:
                    if isinstance(section_value, bool):
                        prompt[section_key] = new_val.lower() in {"y", "yes", "true", "1"}
                    elif isinstance(section_value, int):
                        prompt[section_key] = int(new_val)
                    elif isinstance(section_value, float):
                        prompt[section_key] = float(new_val)
                    elif isinstance(section_value, list):
                        prompt[section_key] = [x.strip() for x in new_val.split(",")]
                    else:
                        prompt[section_key] = new_val
                except Exception:
                    prompt[section_key] = new_val

    # ------------------------------------------------------------------
    # 4) Write to file
    # ------------------------------------------------------------------
    outfile = "prompt_out.json"
    with open(outfile, "w", encoding="utf-8") as f:
        json.dump(prompt, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Prompt saved to {outfile}")

if __name__ == "__main__":
    main()