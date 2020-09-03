# Respond to a key without the need to press enter
import tkinter as tk  # on python 2.x use "import Tkinter as tk"


def keypress(event):
    if event.keysym == "Escape":
        root.destroy()
    x = event.char
    if x == "w":
        print("W pressed")
    elif x == "a":
        print("A pressed")
    elif x == "s":
        print("S pressed")
    elif x == "d":
        print("D pressed")
    else:
        print(x)


root = tk.Tk()
print("Press a key (Escape key to exit):")
root.bind_all("<Key>", keypress)
# don't show the tk window
# root.withdraw()
root.mainloop()
