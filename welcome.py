from tkinter import *

root = Tk()
root.title("Welcome")
root.geometry("500x600")

# Define image
bg = PhotoImage(file= "images/welcome.png")

# create a label
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth= 1, relheight=1)

root.mainloop()