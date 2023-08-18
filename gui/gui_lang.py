from tkinter import *
from tkinter import filedialog

root = Tk()
v = IntVar()
v.set(1)  # initializing the choice

root.title("Lazy Application Letter Generator")
root.config(background="lavender")

languages = [
    ("English", 1),
    ("German", 2),
]

frame_language_browse = Frame(root, background="lavender")
frame_language_browse.pack(pady=10)

frame_language = Frame(frame_language_browse, background="lavender")
Label(
    frame_language,
    text="Choose a language:",
    font=("Arial", 12),
    justify=LEFT,
    fg="purple",
    bg="lavender",
    pady=20
).pack(side=LEFT)

for txt, val in languages:
    Radiobutton(
        frame_language,
        text=txt,
        padx=20,
        variable=v,
        value=val,
        fg="purple",
        bg="lavender",
        font=("Arial", 12),
    ).pack(side=LEFT)

frame_language.pack(pady=10)
root.geometry("800x600")
root.mainloop()