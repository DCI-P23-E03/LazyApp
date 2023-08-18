from tkinter import *
from tkinter import filedialog

root = Tk()

root.title("Lazy Application Letter Generator")
root.config(background="lavender")

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