import tkinter as tk
from random import *

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(x, y, color):
    canvas.create_rectangle(x, y, x+1, y+1, fill = color)

def ecran_aleatoire():
    for i in range(256):
        for j in range(256):
            draw_pixel(i, j, get_color(randint(0, 255), randint(0, 255), randint(0, 255)))

root = tk.Tk()
root.title("LESSSGOOOOOOOOOOOOOO BABYYY")

canvas = tk.Canvas(root, bg = "black", width = 256, height = 256)
rd_button = tk.Button(root, text =  "Aléatoire", command = ecran_aleatoire)
deg0 = tk.Button(root, text = "Dégradé gris")
deg1 = tk.Button(root, text = "Dégradé 2D")

rd_button.grid(row = 0, column = 0)
deg0.grid(row = 1, column = 0)
deg1.grid(row = 2, column = 0)
canvas.grid(row = 0, rowspan = 3, column = 1)

root.mainloop()