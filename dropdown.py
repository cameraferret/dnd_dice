import tkinter as tk

def doNothing():
    print("all your base")


root = tk.Tk()

menu = tk.Menu(root)
root.config(menu=menu)

subMenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New project ...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing())

editMenu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

root.mainloop()
