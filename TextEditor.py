import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Python Text Editor")

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
        file_menu.add_command(label='Open', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=root.quit)
        self.menu.add_cascade(label='File', menu=file_menu)

        # Edit Menu
        edit_menu = tk.Menu(self.menu, tearoff=False)
        edit_menu.add_command(label='Undo', command=self.text_area.edit_undo)
        edit_menu.add_command(label='Redo', command=self.text_area.edit_redo)
        edit_menu.add_command(label='Insert Text', command=self.insert_text)
        edit_menu.add_command(label='Delete Selection', command=self.delete_selection)
        edit_menu.add_command(label='Find & Replace', command=self.find_replace)
        edit_menu.add_command(label='Highlight Selection', command=self.highlight_selection)
        self.menu.add_cascade(label='Edit', menu=edit_menu)

        # Configure text tag for highlighting
        self.text_area.tag_configure("highlight", background="yellow")

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

    def insert_text(self):
        text_to_insert = simpledialog.askstring("Insert", "Enter text to insert:")
        if text_to_insert:
            try:
                self.text_area.insert(tk.INSERT, text_to_insert)
            except Exception as e:
                messagebox.showerror("Error", f"Insert failed: {e}")

    def delete_selection(self):
        try:
            self.text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)
        except tk.TclError:
            messagebox.showinfo("Delete", "No text selected to delete.")

    def highlight_selection(self):
        try:
            self.text_area.tag_add("highlight", tk.SEL_FIRST, tk.SEL_LAST)
        except tk.TclError:
            messagebox.showinfo("Highlight", "No text selected to highlight.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
