import tkinter as tk
from tkinter import *
import time

# Muktika

# create the root window
root = tk.Tk()

# create a label with the message
label = tk.Label(root, text="Thank you for ordering!", bg='LightPink1', fg='white')
label.pack()
label.config(font=("Helvetica", 30))
label.place(relx=0.5, rely=0.5, anchor="center")

# define a function to close the window after 5 seconds
def close_window():
    time.sleep(1)  # wait for 5 seconds
    root.destroy()  # close the window

# call the close_window function after a short delay
root.after(1000, close_window)
root.geometry("500x200")
root.config(bg='LightPink1')

# start the event loop
root.mainloop()
