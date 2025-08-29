def modify_file(input_file, output_file):
    """
    Reads a file, modifies its content (uppercase + line numbers),
    and writes the modified content into a new file.
    """
    try:
        with open(input_file, "r") as f:
            lines = f.readlines()

        # Modify content: add line numbers and convert to uppercase
        modified_lines = [f"{i+1}: {line.upper()}" for i, line in enumerate(lines)]

        with open(output_file, "w") as f:
            f.writelines(modified_lines)

        print(f"✅ File modified successfully and saved as '{output_file}'")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")