import tkinter as tk

colors = ["blue", "green", "black", "yellow", "magenta", "red"]

root = tk.Tk()

can = tk.Canvas(root, width = 700, height = 700)
can.pack()

for i in range(35, 0, -1):
    can.create_oval(350 - i*10, 350 - i*10, 350+i*10, 350+i*10, fill = colors[i%len(colors)])

root.mainloop()