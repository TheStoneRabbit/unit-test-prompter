🎨📁✍️📝📄✨

# README

## Overview
This Python script is designed to allow users to select multiple files via a graphical interface, read their contents, and format them into a structured text block. The formatted text includes the name of each selected file and its content, which is then copied to the clipboard for easy pasting elsewhere.

## Dependencies
To run this script, you will need the following Python packages:
- **PyQt5**: Provides the GUI functionality for file selection.
- **pyperclip**: Used to copy the formatted text to the system clipboard.

You can install these libraries using pip:
```bash
pip install PyQt5 pyperclip
```

## How It Works
1. **File Selection**: When the script is executed, a file dialog window opens, allowing the user to select multiple files from their system.
2. **File Reading**: The content of each selected file is read.
3. **Text Formatting**: The name and content of each file are structured into a Markdown-like format.
4. **Clipboard Copying**: The final formatted text is automatically copied to the system clipboard.

## Example Output
After selecting files, the following formatted output will be generated and copied:

```
Below are the files you need to analyze.

filename1.txt: 
(Content)
```



## Usage
1. Run the script using Python:
    ```bash
    python unit-test-prompter.py
    ```
2. A file dialog will open. Select one or more files.
3. Once files are selected, the content will be read and copied in a structured format.
4. Simply paste the copied text wherever needed.

### OR:

Use the binary file found in the `dist` folder. This executable file can be run directly without the need for Python or any dependencies.

## License
Feel free to modify and use this script according to your needs!

## Notes
- The script supports text-based files only.
- Ensure you have write permission for the system clipboard to allow `pyperclip` to function correctly.

Enjoy! 🎉

