from tkinter import *
from PIL import ImageTk, Image
import subprocess

class WelcomePage:
    def __init__(self, master):
        self.master = master
        master.title("Simply Sweet Bakeshop")

        # Set background image
        self.bg_image = ImageTk.PhotoImage(Image.open("welcome.png").resize((400, 300)))
        self.bg_label = Label(master, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        # Create the start order button
        self.start_order_button = Button(master, text="Start Order", font=("Arial", 18), command=self.start_order)
        self.start_order_button.pack(pady=20)
        self.start_order_button.place(relx=0.5, rely=0.8, anchor=CENTER)
        self.start_order_button.config(fg='LightPink1')


    def start_order(self):
         #create_new_window()
        proc=subprocess.Popen(["python", "Cake_details code.py"])
        #close the current GUI
        root.destroy()
        # allows the new_gui to stay
        proc.wait()


root = Tk()
root.geometry("400x300")
root.config(bg='LightPink1')
welcome = WelcomePage(root)
root.mainloop()