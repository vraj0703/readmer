# Codebase Project: Readmer Script for Documentation Generation

## Overview
This project provides a script named `readmer` that automates the process of gathering all source code from files and directories within a specified path, combining it into one document to generate a README.md file using Ollama's text-to-English model as prompted by an expert technical writer with predefined instructions in "format.txt". The purpose is for users who need a simple yet comprehensive summary of their codebase encapsulated within the generated `README.md`.

## Key Features
- **Code Aggregation:** Collects and combines source code from various programming languages into one README document, including but not limited to Python (.py), JavaScript (.js), TypeScript (.ts), Go (.go), Rust (.rs), Dart (.dart), HTML (.html), CSS (.css).
- **README.md Generation:** Utilizes Ollama with a predefined prompt from the "format.txt" file, allowing users to dynamically specify how they want their README document's content and structure represented based on collected code snippets.
- **User Friendly Interface:** Takes input via command line arguments for path specification only; does not require advanced programming knowledge or installation of Ollama CLI tools beyond what is necessary in the script itself (Python, subprocess). Users simply need to specify a filepath and run `readmer`.py with it as an argument.
- **Language Support:** The code supports multiple languages which enhances its utility for diverse development environments while ensuring inclusivity of different programming practices reflected within the generated README document.

## Tech Stack & Dependencies
- **Language:** Python 3 (as per `import sys` at the beginning)
- **Key Libraries/Frameworks:** The script uses standard libraries such as `os`, `subprocess`, and third-party Ollama model for language translation. Users must have access to an internet connection, since it relies on querying a remote server (Ollama). It assumes that users already installed the necessary CLI tools required by Ollama (`ollama` command) as per their official installation guide or documentation.

## Getting Started

### Prerequisites
- Python 3 environment set up, with `subprocess`, and an internet connection to query external services (Ollama server). Installation of the latest Ollama CLI tool is recommended before running this script as it relies on these tools. Ensure that you have a recent installation for better compatibility: https://ollamallet.org/download
- The "format.txt" file, which defines how users want their README to be structured and written (e.g., with code blocks, descriptions). This should include clear instructions on what content goes where in the generated `README`.

### How to Run
1. Create a text file named "format.txt" within the same directory as your script (`readmer.py`), ensuring that it defines how you wish for your README's structure and contents, including placeholders like `---\nFile: {relative_path}\n---\n`.
2. Place all source code files in a single folder or across multiple directories within the same parent directory as `readmer.py`. The script supports nested directories but not recursive search beyond immediate children folders of the specified path to maintain simplicity and control over generated content structure.
3. Open your command line interface (CLI) terminal application on Windows, macOS, or Linux/Unix systems.
4. Navigate into the directory containing both `readmer.py` script and codebase you wish to document using: 
   ```bash
   cd path_to_directory_with_script_and_codebase
   ```
5. Execute the Readmer Script by providing your target file or folder's absolute or relative path as an argument, replacing `path_to_file_or_folder` with the correct directory location: 
   ```bash
   python readmer.py [target_directory]
   ```
6. Once executed successfully without any errors and assuming Ollama responded within its timeout of up to 10 minutes, a README document should be created in place for that target path containing the aggregated code snippets structured as per "format.txt".

## Codebase Structure Overview
The main file is `readmer.py`, which includes functions and logic required to: read source files from specified paths, gather their content into a dictionary with relative paths mapped to contents (`gather_code_from_path`), compose README content based on that collection via the Ollama model through command line interaction in `generate_readme()`, save this composed document as "README.md" (if any), and handle miscellaneous tasks such as prerequisite checks, main function logic (`main()`). The expected output is a single README file named after project directory structure or the specific path provided if not nested within directories without an accompanying `.gitignore` directive to prevent untracked content inclusion.

Please note that `generate_readme()` relies on Ollama, which itself expects commands in JSON format and responds accordingly; hence users must predefine their structure intent via "format.txt". This script does not directly incorporate the generated README but generates it by capturing output from an external service (`OLLAMA_MODEL`).

--- CODEBASE END ---