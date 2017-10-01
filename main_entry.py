from tkinter import *
from tkinter import ttk

TMP_HEIGHT_PERC = 60
TMP_WIDTH_PERC = 80

root = Tk()
root.title("Initial Program")

# Acquire the size of screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

screen_width = screen_width * (TMP_WIDTH_PERC / 100)
screen_height = screen_height * (TMP_HEIGHT_PERC / 100)

back_frame = ttk.Frame(root, width=400, height=200)

back_frame.configure(width=screen_width)
back_frame.configure(height=screen_height)
back_frame.configure(relief='sunken')
back_frame.configure(borderwidth="25")

# root.grid(column=0, row=0)
back_frame.grid(column=0, row=0, columnspan=3, rowspan=2)

root.mainloop()
