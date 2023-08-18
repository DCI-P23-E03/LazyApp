from tkinter import *
from tkinter import filedialog

root = Tk()

root.title("Lazy Application Letter Generator")
root.config(background="lavender")

def browseFiles():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select File",
        filetypes=(("Text files", "*.txt*"), ("all files", "*.*")),
    )
    #label_file_explorer.configure(text="File Opened: " + filename)

def clear_default_text(event):
    if text_field.get("1.0", "end-1c") == "Paste the job advertisement here.":
        text_field.delete("1.0", "end-1c")
        text_field.config(fg="#000000")

def restore_default_text(event):
    if text_field.get("1.0", "end-1c") == "":
        text_field.insert("1.0", "Paste the job advertisement here.")
        text_field.config(fg="#808080")

text_field = Text(
    root,
    width=80,
    height=15,
    bg="#f6f6f5",
    fg="#808080",
    font=("Arial", 12)
)
text_field.insert("1.0", "Paste the job advertisement here.")
text_field.bind("<FocusIn>", clear_default_text)
text_field.bind("<FocusOut>", restore_default_text)
text_field.pack(pady=10)


button_browse_file = Button(
    root,
    text="Import your CV",
    command=browseFiles,
    bg="lavender",
    fg="purple",
    height=2,
    width=35,
    font=("Arial", 12),
)
button_browse_file.pack(pady=10)

button_generate = Button(
    root,
    text="Generate Application Letter",
    font=("Arial", 15, "bold"),
    height=2,
    width=35,
    bg="lavender",
    fg="purple",
)
button_generate.pack(pady=20)

root.geometry("800x600")
root.mainloop()