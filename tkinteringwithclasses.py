import tkinter as tk


class BuckysButtons:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.printButton = tk.Button(frame, text="Print message", command=self.printMessage)
        self.printButton.pack(side=tk.LEFT)

        self.quitButton = tk.Button(frame, text="quit", command=frame.quit)
        self.quitButton.pack(side=tk.LEFT)

    def printMessage(self):
        print("wowzers")


root = tk.Tk()
b = BuckysButtons(root)
root.mainloop()