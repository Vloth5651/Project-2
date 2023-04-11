from Tkinter import *
import Tkinter as tk
master = tk.Tk()
bgimg= tk.PhotoImage(file = "welcome.png")
#Specify the file name present in the same directory or else
#specify the proper path for retrieving the image to set it as background image.
limg= Label(master, i=bgimg)
limg.pack()
master.mainloop()

Button(window, text="Get Started!", width=30).place(x=200,y=400)
window.mainloop()