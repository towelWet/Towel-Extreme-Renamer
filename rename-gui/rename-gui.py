import os
import re
import tkinter as tk
from tkinter import filedialog

def browse_directory():
    directory = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(tk.END, directory)

def rename_words_in_files(path, old_word, new_word):
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r+") as f:
                    content = f.read()
                    content_new = re.sub(old_word, new_word, content, flags=re.IGNORECASE)
                    if content != content_new:
                        f.seek(0)
                        f.write(content_new)
                        f.truncate()
            except UnicodeDecodeError:
                print(f"Skipped binary file: {filepath}")
            except FileNotFoundError:
                print(f"Skipped file (no longer exists): {filepath}")

def rename_files_dirs_gui():
    path = path_entry.get()
    old_word = old_word_entry.get()
    new_word = new_word_entry.get()

    rename_words_in_files(path, old_word, new_word)

    for root, dirs, files in os.walk(path, topdown=False):
        for dir in dirs:
            if old_word.lower() in dir.lower():
                new_dir = re.sub(old_word, new_word, dir, flags=re.IGNORECASE)
                old_dir_path = os.path.join(root, dir)
                new_dir_path = os.path.join(root, new_dir)
                try:
                    os.rename(old_dir_path, new_dir_path)
                except Exception as e:
                    print(f"Failed to rename directory {old_dir_path} to {new_dir_path}. Error: {e}")

        for file in files:
            if old_word.lower() in file.lower():
                new_file = re.sub(old_word, new_word, file, flags=re.IGNORECASE)
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, new_file)
                try:
                    os.rename(old_file_path, new_file_path)
                except Exception as e:
                    print(f"Failed to rename file {old_file_path} to {new_file_path}. Error: {e}")

root = tk.Tk()

path_label = tk.Label(root, text="Path")
path_label.pack()
path_entry = tk.Entry(root)
path_entry.pack()

browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.pack()

old_word_label = tk.Label(root, text="Old Word")
old_word_label.pack()
old_word_entry = tk.Entry(root)
old_word_entry.pack()

new_word_label = tk.Label(root, text="New Word")
new_word_label.pack()
new_word_entry = tk.Entry(root)
new_word_entry.pack()

rename_button = tk.Button(root, text="Rename", command=rename_files_dirs_gui)
rename_button.pack()

root.mainloop()
