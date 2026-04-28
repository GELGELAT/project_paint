from tkinter import *
from tkinter import ttk

root = Tk()
root.title("рисАвАлкА")
root.geometry("400x400")

canvas = Canvas(root, width=400, height=400)
canvas.grid(row=0, column=0)

drawing = False
last_x = 0
last_y = 0

def start_draw(event):
    global drawing
    global last_x
    global last_y
    canvas.create_oval(event.x, event.y, event.x, event.y,width=4, fill="black")
    drawing = True
    last_x = event.x
    last_y = event.y

def draw(event):
    global last_x
    global last_y
    if drawing:
        canvas.create_line(last_x , last_y , event.x , event.y ,width=5, fill="black")
        last_x = event.x
        last_y = event.y

def stop_draw(event):
    global drawing
    drawing = False



canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_draw)









root.mainloop()