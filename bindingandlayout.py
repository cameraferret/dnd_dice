import tkinter as tk


def printName(event):
    print("hello world")


root = tk.Tk()

# button_1 = tk.Button(root, text="Print message", command=printName)
button_1 = tk.Button(root, text="Print message")
button_1.bind("<Button-1>", printName)
button_1.pack()

root.mainloop()
