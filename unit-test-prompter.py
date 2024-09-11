from PyQt5.QtWidgets import QApplication, QFileDialog
import pyperclip


def open_multiple_files():
    app = QApplication([])
    files, _ = QFileDialog.getOpenFileNames(None, "Select Files")
    return files

# Get the selected files
selected_files = open_multiple_files()
start_text = "Below are the files you need to analyze."
# Print the selected file paths
for file in selected_files:
    with open(file, "r") as f:
        data = f.read()
        name = file.split("/")[-1]
        start_text += f"\n{name}: \n\n```\n{data}\n```\n\n"
pyperclip.copy(start_text)