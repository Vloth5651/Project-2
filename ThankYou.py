import tkinter as tk
from PIL import ImageTk, Image
import time

# create the root window
root = tk.Tk()
root.title("Thank you for ordering!")

# Set background image
bg_image = ImageTk.PhotoImage(Image.open("exit.png").resize((400, 300)))
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# define a function to close the window after 2 seconds
def close_window():
    time.sleep(2)  # wait for 2 seconds
    root.destroy()  # close the window

# call the close_window function after a short delay
root.after(1000, close_window)

root.geometry("400x300")
root.config(bg='LightPink1')

# start the event loop
root.mainloop()
