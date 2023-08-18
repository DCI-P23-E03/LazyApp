from tkinter import *
from tkinter import filedialog

root = Tk()

root.title("Lazy Application")
root.config(background="lavender")

label_file_explorer = Label(
    root,
    text="Lazy Application Letter Generator",
    font=("Arial", 20, "bold"),
    width=100,
    height=2,
    fg="purple",
    bg="lavender",
)
label_file_explorer.pack(pady=10)


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

root.geometry("800x600")
root.mainloop()