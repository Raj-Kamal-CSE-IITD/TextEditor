import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Text Editor")

        # Text area
        self.text_area = tk.Text(root, undo=True, wrap='word')
        self.text_area.pack(expand=True, fill='both')

        # Scrollbar
        self.scroll = tk.Scrollbar(self.text_area)
        self.text_area.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.text_area.yview)
        self.scroll.pack(side='right', fill='y')

        # Menu bar
        self.menu = tk.Menu(root)
        self.root.config(menu=self.menu)

        # File Menu
        file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Open', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=root.quit)

        # Edit Menu
        edit_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label='Edit', menu=edit_menu)
        edit_menu.add_command(label='Find & Replace', command=self.find_replace)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(self.text_area.get(1.0, tk.END))
                messagebox.showinfo("Success", "File saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    def find_replace(self):
        find_text = simpledialog.askstring("Find", "Enter text to find:")
        replace_text = simpledialog.askstring("Replace", "Replace with:")

        if find_text and replace_text is not None:
            content = self.text_area.get(1.0, tk.END)
            new_content = content.replace(find_text, replace_text)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, new_content)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
