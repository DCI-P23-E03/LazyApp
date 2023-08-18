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

text_field = Text(
    root,
    width=80,
    height=15,
    bg="#f6f6f5",
    fg="#808080",
    font=("Arial", 12)
)
text_field.insert("1.0", "YOUR JOB APPLICATION LETTER HERE")

text_field.pack(pady=10)

button_generate = Button(
    root,
    text="Save to PDF",
    font=("Arial", 15, "bold"),
    height=2,
    width=35,
    bg="lavender",
    fg="purple",
)
button_generate.pack(pady=20)

root.geometry("800x600")
root.mainloop()