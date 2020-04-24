# GUI interface stuff #
from tkinter import *

root = Tk()
root.title("Charater Quick Draw (CQW)")

frame = LabelFrame(root)
frame.pack()

e = Entry(root, width=90)


mylabel1 = Label(root, text="Charater Quick Draw")
mylabel2 = Label(root, text="(For 5E DND Basic Rules)")

mylabel1.grid(row=1)
mylabel2.grid(row=2)


root.mainloop()

# normal code stuff #