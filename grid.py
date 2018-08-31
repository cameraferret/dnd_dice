import tkinter as tk

root = tk.Tk()

lable_1 = tk.Label(root, text="Name")
lable_2 = tk.Label(root, text="Password")

entry_1 = tk.Entry(root)
entry_2 = tk.Entry(root, show='*')


lable_1.grid(row=0, sticky=tk.E)
lable_2.grid(row=1, sticky=tk.E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = tk.Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)


root.mainloop()
