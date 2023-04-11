from tkinter import *
import subprocess

class WelcomePage:
    def __init__(self, master):
        self.master = master
        master.title("Simply Sweet Bakeshop")

        # Create the welcome label
        self.welcome_label = Label(master, text="Hi there! Welcome To Simply Sweet Bakeshop", font=("Arial", 20))
        self.welcome_label.pack(pady=50)
        self.welcome_label.config(bg='LightPink1', fg="white")

        # Create the start order button
        self.start_order_button = Button(master, text="Start Order", font=("Arial", 18), command=self.start_order)
        self.start_order_button.pack(pady=20)
        self.start_order_button.config(fg='LightPink1')

    def start_order(self):
         #create_new_window()
        proc=subprocess.Popen(["python", "Cake_details code.py"])
        #close the current GUI
        root.destroy()
        # allows the new_gui to stay
        proc.wait()


root = Tk()
root.geometry("700x300")
root.config(bg='LightPink1')
welcome = WelcomePage(root)
root.mainloop()