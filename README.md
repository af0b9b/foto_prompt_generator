# foto_prompt_generator
prompt generator from Gemini 
# Interactive Prompt Builder

[![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
Tools for interactively building and editing JSON prompts for AI image generation.

This repository contains two interactive Python scripts that guide you through **creating and refining JSON prompt files**, starting from predefined schemas (`base.json` or `prompt_v1.json`).  
Each tool saves a **new, customized output file** without altering your source files.

---

## Features
- Load a **base JSON schema** as the starting structure.
- Navigate **sections and nested fields** interactively.
- Edit **scalars, lists, and dictionaries** with type preservation.
- **Accept, skip, or override** suggested values for each field.
- Save results into **`prompt_basic.json`** or **`prompt_prof_output.json`**.

---

## Scripts Overview

### `build_prompt_base.py`
- **Input:** `base.json`  
- **Output:** `prompt_basic.json`  
- **Use Case:** Build a simple, structured prompt based on a lightweight schema.

### `build_prompt_v_1_prof.py`
- **Input:** `prompt_v1.json`  
- **Output:** `prompt_prof_output.json`  
- **Use Case:** Edit and refine **advanced prompts (schema v1.1)** with deeper control over nested structures.

---

## Quick Start

1. **Clone or download** this repository.
2. Make sure you have **Python 3.7+** installed.
3. Place your schema file (`base.json` or `prompt_v1.json`) in the same directory as the script.
4. Run one of the scripts:
   ```bash
   python build_prompt_base.py
   python build_prompt_v_1_prof.py
   ```
   
5.	Follow the interactive prompts:
	•	Select a section to edit.
	•	Drill down into nested dictionaries or lists.
	•	Accept, modify, or skip each value.

6.	The customized prompt will be saved automatically as:
	•	prompt_basic.json (for the base builder)
	•	prompt_prof_output.json (for the advanced builder)

⸻

Requirements:

	•	Python 3.7 or newer.
	•	A valid input file:
	•	base.json (for the basic builder)
	•	prompt_v1.json (for the professional builder)
	•	Terminal or command-line access.

⸻

Notes

	•	These tools are intended for manual, interactive use — they are not designed for batch automation.
	•	Your input files are never overwritten; all changes are saved to new output files.
	•	Always back up your input schema before heavy edits.

⸻

License

This repository is released under the MIT License.
You are free to modify and use these scripts for personal or commercial projects.




