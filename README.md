# 🐍 Towel Extreme Renamer 

Towel Extreme Renamer (TER) is a Python-powered tool that simplifies the process of renaming files and directories in bulk. It also allows replacing words within the files. Built with simplicity in mind, TER features a friendly GUI for a smooth user experience.

## 💻 Easy Installation

1. Go to the project page on GitHub.
2. Navigate to the "Releases" section.
3. Look for the latest release and download the `.app` file.
4. Open the downloaded `.app` file to run the software. 

And you're done! No technical skills required!

## 🌟 Features

1. **🏷️ Bulk Renaming**: Rename all files and directories in a chosen path with ease.
2. **📝 Text Replacement**: Replace occurrences of a word within files.
3. **🚀 PyInstaller Compatibility**: Ready for bundling into an executable using PyInstaller.
4. **🖥️ Easy-to-Use GUI**: A simple graphical interface powered by Tkinter makes TER a breeze to use.

## 🚀 How to Use

**Let's get renaming in just three steps!**

1. Run the script or launch the downloaded .app file.
2. 🔍 Browse for the directory where you want to perform renaming.
3. 🖊️ Fill in the "Old Word" (the word you want to replace) and the "New Word" (the word you want to replace it with), then hit the "Rename" button. Done!

## 💼 PyInstaller Bundling (For Developers)

If you want to bundle TER into a standalone executable, you can use PyInstaller. Here's how:

1. Install PyInstaller, if you don't have it already. Open your terminal and type:

   ```bash
   pip install pyinstaller
   ```

2. Navigate to the project directory. 

3. Bundle `rename-gui.py` into a standalone executable using the command:

   ```bash
   pyinstaller --onefile --windowed rename-gui.py
   ```

## ⚠️ Dependencies (For Developers)

TER relies on Python's built-in modules:

- **Tkinter**: Powers the GUI.
- **os**: Enables interactions with the operating system, including renaming files and directories.
- **re**: Helps with regular expressions and text replacements.

## 💌 Support and Contribution

Stumbled upon a bug or have an idea to improve TER? Feel free to raise an issue or contribute directly with a pull request. Your contributions are always appreciated!
