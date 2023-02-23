import tkinter as tk
import random
from math import *

root = tk.Tk()
root.title("TD Python")

canvas = tk.Canvas(root, bg = "black", relief = tk.SUNKEN, borderwidth = 10)

user_color = "blue"

def circle():

    x = random.randint(10, int(canvas["width"]) - int(sqrt(5000)))
    y = random.randint(10, int(canvas["height"]) - int(sqrt(5000)))

    canvas.create_oval(x, y, x + sqrt(5000), y + sqrt(5000), fill = user_color)

def cross():

    x = random.randint(10, int(canvas["width"]) - int(sqrt(5000)))
    y = random.randint(10, int(canvas["height"]) - int(sqrt(5000)))

    canvas.create_line(x, y, x + sqrt(5000), y + sqrt(5000), fill=user_color)
    canvas.create_line(x + sqrt(5000), y, x, y + sqrt(5000), fill=user_color)

def square():

    x = random.randint(10, int(canvas["width"]) - int(sqrt(5000)))
    y = random.randint(10, int(canvas["height"]) - int(sqrt(5000)))

    canvas.create_rectangle(x, y, x + 100, y + 100, fill = user_color)

def ask_color():

    user_color = input("Choississez une couleur : ")

circle_button = tk.Button(root, text = "Cercle", font = ("Comic Sans MS", 16), command=circle)
cross_button = tk.Button(root, text = "Cross",font = ("Comic Sans MS", 16), command = cross)
square_button = tk.Button(root, text = "Carré", font = ("Comic Sans MS", 16), command = square)
color_button = tk.Button(root, text = "Choisir une couleur", font = ("Comic Sans MS", 16), command = ask_color)


color_button.grid(row = 0, column = 1)
circle_button.grid(row = 1, column = 0)
cross_button.grid(row = 2, column = 0)
square_button.grid(row = 3, column = 0)
canvas.grid(row = 1, rowspan = 3, column = 1)


root.mainloop()