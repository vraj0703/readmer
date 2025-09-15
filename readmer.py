import sys
import os
import subprocess
import time

# --- Configuration ---
OLLAMA_MODEL = "phi3"

def gather_code_from_path(target_path):
    """
    Gathers all source code from a given file or directory.

    Returns:
        A dictionary where keys are file paths and values are file contents.
    """
    all_code = {}
    supported_extensions = ('.py', '.js', '.ts', '.go', '.rs', '.java', '.dart', '.html', '.css')

    if os.path.isfile(target_path):
        if target_path.endswith(supported_extensions):
            print(f"📄 Reading single file: {target_path}")
            with open(target_path, 'r', encoding='utf-8') as f:
                all_code[target_path] = f.read()
    elif os.path.isdir(target_path):
        print(f"📁 Reading all files in directory: {target_path}")
        for root, _, files in os.walk(target_path):
            for file in files:
                if file.endswith(supported_extensions):
                    file_path = os.path.join(root, file)
                    print(f"   - Reading {file_path}")
                    with open(file_path, 'r', encoding='utf-8') as f:
                        all_code[file_path] = f.read()
    return all_code

def generate_readme(all_code, readme_format):
    """
    Calls Ollama with the entire codebase to generate a README.md file.
    """
    combined_code = ""
    for path, content in all_code.items():
        relative_path = os.path.basename(path)
        combined_code += f"---\n"
        combined_code += f"File: {relative_path}\n"
        combined_code += f"---\n"
        combined_code += f"```\n{content}\n```\n\n"

    prompt = f"""
    As an expert technical writer, your task is to create a high-quality README.md file
    for the following codebase.

    Analyze all the provided code files to deeply understand the project's purpose,
    key features, structure, and how to use it.

    The README.md file MUST strictly follow this format and structure:
    --- FORMAT START ---
    {readme_format}
    --- FORMAT END ---

    Here is the entire codebase, with each file clearly marked:
    --- CODEBASE START ---
    {combined_code}
    --- CODEBASE END ---

    Generate ONLY the complete README.md file in Markdown format. Do not include
    any other text or explanations in your response.
    """

    try:
        command = ['ollama', 'run', OLLAMA_MODEL, prompt]
        print("\n🤖 Asking Ollama to generate the README. This may take a few minutes for large projects...")
        start_time = time.time()

        result = subprocess.run(
            command, capture_output=True, text=True, check=True,
            timeout=600,  # 10-minute timeout for potentially large projects
            encoding='utf-8'
        )

        duration = time.time() - start_time
        print(f"✅ Ollama generation finished in {duration:.2f} seconds.")
        return result.stdout.rstrip()

    except subprocess.TimeoutExpired:
        print(f"❌ Error: Ollama command timed out after 10 minutes.")
        return None
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return None


def main():
    """
    The main function to drive the script.
    """
    if len(sys.argv) != 2:
        print("Usage: python readmer.py <path_to_file_or_folder>")
        sys.exit(1)

    target_path = sys.argv[1]

    if not os.path.exists(target_path):
        print(f"Error: The path '{target_path}' does not exist.")
        sys.exit(1)

    try:
        with open('format.txt', 'r', encoding='utf-8') as f:
            readme_format = f.read()
    except FileNotFoundError:
        print("Error: `format.txt` not found. Please create it to define your README structure.")
        sys.exit(1)

    # Step 1: Gather all the code
    all_code = gather_code_from_path(target_path)

    if not all_code:
        print("⚠️ No supported code files found to generate a README from.")
        sys.exit(0)

    # Step 2: Generate the README content
    readme_content = generate_readme(all_code, readme_format)

    # Step 3: Save the README.md file
    if readme_content:
        output_path = ""
        if os.path.isdir(target_path):
            output_path = os.path.join(target_path, 'README.md')
        else: # It's a file
            output_path = os.path.join(os.path.dirname(target_path), 'README.md')

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print(f"\n✨ Successfully created README.md at: {output_path}")
    else:
        print("\n❌ Failed to generate README.md content.")

if __name__ == "__main__":
    main()