import tkinter as tk
import random as rnd
root = tk.Tk()  # making the window

diceValue = tk.IntVar()
temp = tk.IntVar()


def rollDice(d_sides):
    diceValue.set(rnd.randint(1, d_sides))


def test(event):
    print(dex.get())


# Frames
topFrame = tk.Frame(root)
bottomFrame = tk.Frame(root)

# widgets and buttons wooo
D20 = tk.Button(topFrame, text="D20", fg="Red", command=lambda: rollDice(20))
D12 = tk.Button(topFrame, text="D12", fg="Green", command=lambda: rollDice(12))
D10 = tk.Button(topFrame, text="D10", fg="Blue", command=lambda: rollDice(10))
D8 = tk.Button(topFrame, text="D8", fg="Purple", command=lambda: rollDice(8))
D6 = tk.Button(topFrame, text="D6", fg="gray26", command=lambda: rollDice(6))
D4 = tk.Button(topFrame, text="D4", fg="orangered4", command=lambda: rollDice(4))
Coin = tk.Button(topFrame, text="Coin Flip", fg="gray25", command=lambda: rollDice(2))


# Labels
dexLabel= tk.Label(bottomFrame, text="Dex:")
dex = tk.Entry(bottomFrame)
dice = tk.Label(bottomFrame, textvariable=diceValue)

dex.bind("<Return>", test)

# packing
topFrame.pack()
bottomFrame.pack(side=tk.BOTTOM)
D20.grid(row=1, column=2, padx=5, pady=5)
D12.grid(row=1, column=1, padx=5, pady=5)
D10.grid(row=1, column=0, padx=5, pady=5)

D8.grid(row=0, column=3, padx=4)
D6.grid(row=0, column=2, padx=4)
D4.grid(row=0, column=1, padx=4)
Coin.grid(row=0, column=0, padx=4)

dice.grid(row=0, column=3, padx=5, pady=4)
dexLabel.grid(row=0)
dex.grid(row=0, column=2)


root.mainloop()  # haaa, forgot // isn't a comment in python. //Makes the app run wooo
