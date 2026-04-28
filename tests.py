from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Grid с весами")
root.geometry("800x600")
root.resizable(True,True)


# Создаём основную рамку
main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0, sticky="nsew")

# НАСТРАИВАЕМ ВЕСА (очень важно!)
root.grid_rowconfigure(0, weight=1)     # 1-я строка может растягиваться
root.grid_columnconfigure(0, weight=1)  # 1-я колонка может растягиваться

# Холст внутри рамки
canvas = Canvas(main_frame, bg="white")
canvas.grid(row=0, column=0, sticky="nsew")

# Настраиваем веса для рамки
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

root.mainloop()