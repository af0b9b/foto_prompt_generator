import json
import os

def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_suggestion(section, field, current_value):
    """
    Return the current value as suggestion if it exists,
    otherwise an empty string. No external descriptions used.
    """
    return current_value if current_value else ''

def print_section_header(section):
    print("\n" + "=" * 48)
    print(f"SECTION: {section.upper()}")
    print("=" * 48 + "\n")

def print_field_prompt(section, field, current_value):
    suggestion = get_suggestion(section, field, current_value)
    print(f"\nField: {field}")
    if suggestion:
        print(f"  Suggested: {suggestion}")
    return suggestion

def prompt_fields_in_section(section, section_data):
    # Returns dict of updated field values for this section
    updated = {}
    fields = list(section_data.keys())
    num_fields = len(fields)
    i = 0
    while i < num_fields:
        field = fields[i]
        current_value = section_data[field]
        suggestion = print_field_prompt(section, field, current_value)
        print("\nOptions:")
        print("  [Enter]  - Accept suggested/default value")
        print("  [.]      - Skip this field")
        print("  [d]      - Use all defaults for this section")
        print("  [s]      - Skip the rest of this section")
        print("  [q]      - Quit")
        user_input = input(f"Enter value for '{field}': ").strip()
        if user_input.lower() == 'q':
            print("Quitting prompt builder.")
            exit(0)
        elif user_input.lower() == 's':
            print(f"Skipping the rest of section '{section}'.")
            # Fill remaining fields with their current values
            for rem_field in fields[i:]:
                updated[rem_field] = section_data[rem_field]
            break
        elif user_input.lower() == 'd':
            print(f"Using suggested/default values for all fields in section '{section}'.")
            for rem_field in fields[i:]:
                val = get_suggestion(section, rem_field, section_data[rem_field])
                updated[rem_field] = val
            break
        elif user_input == '.':
            updated[field] = section_data[field]
            i += 1
            continue
        elif user_input == '':
            updated[field] = suggestion
        else:
            updated[field] = user_input
        i += 1
    return updated


def main():
    input_filename = "/base.json"
    output_filename = "prompt_basic.json"

    if not os.path.exists(input_filename):
        print(f"Input file '{input_filename}' not found.")
        return

    data = load_json(input_filename)

    # Sections to include in simplified prompt
    sections_to_edit = []
    if 'subject' in data:
        sections_to_edit.append('subject')
    if 'character' in data:
        sections_to_edit.append('character')
    key_sections = ['composition', 'setting', 'lighting', 'style', 'rendering', 'colorPlate']
    for sec in key_sections:
        if sec in data:
            sections_to_edit.append(sec)

    print("\nWelcome to the Step-by-Step Prompt Builder!")
    print("You will be guided through each section. Type 'q' to quit at any time.\n")

    for section in sections_to_edit:
        section_data = data.get(section, {})
        if not isinstance(section_data, dict):
            continue
        print_section_header(section)
        updated_fields = prompt_fields_in_section(section, section_data)
        data[section].update(updated_fields)

    save_json(data, output_filename)
    print(f"\nSimplified prompt saved to '{output_filename}'.")

if __name__ == "__main__":
    main()
