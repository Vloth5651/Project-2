from tkinter import *
from PIL import ImageTk, Image
import subprocess
import sqlite3

# Muktika


# List of options
cake_type = ["Chocolate", "Red Velvet", "Cheesecake", "Vanilla", "Ice Cream"]
cake_size = ["S", "M", "L", "XL"]
cake_filling = ["Buttercream", "Caramel", "Chocolate", "Cream Cheese", "White Chocolate Ganache"]
cake = ["0.jpg", "1.jpg", "2.jpg", "3.jpg", "4.jpg"]

class Cake_details:
    def __init__(self, master):
        self.master = master
        master.title("Cake Order Form")
        
        
        # Cake Details Frame
        self.frame = LabelFrame(master, padx=5, pady=5, bg='LightPink1')
        self.frame.pack(padx=10, pady=10, expand=True, fill=BOTH)
        
        self.frame.config(font=("Helvetica", 12), width=20)
        
        # Frame Column Config
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)        
        
        """-------------------------------------------------------------------"""
        
        # Cake Type Details
        self.type_label = Label(self.frame, text="Choose a cake :", bg='LightPink1')
        self.type_label.grid(row=0, column=0)
        self.type_label.config(font=("Helvetica", 12))
        
        # Cake Type variable to hold the option
        self.type_menu = StringVar(self.frame)
        self.type_menu.set("     ")
        
        # The OptionMenu widget -- Cake Type
        caketype_menu = OptionMenu(self.frame, self.type_menu, *cake_type)
        caketype_menu.grid(row=1, column=0, ipadx=35)
        caketype_menu.config(font=("Helvetica", 12))
        
        """-------------------------------------------------------------------"""
        
        # Cake Size Details
        self.size_label = Label(self.frame, text="Cake Size :", bg='LightPink1')
        self.size_label.grid(row=0, column=1)
        self.size_label.config(font=("Helvetica", 12))
        
        # Cake Size variable to hold the option
        self.size_menu = StringVar(self.frame)
        self.size_menu.set("     ")        
        
        # The OptionMenu widget -- Cake Size
        cakesize_menu = OptionMenu(self.frame, self.size_menu, *cake_size)
        cakesize_menu.grid(row=1, column=1, ipadx=35)
        cakesize_menu.config(font=("Helvetica", 12))
        
        """-------------------------------------------------------------------"""
        
        # Cake Filling Details
        self.filling_label = Label(self.frame, text="Cake Filling :", bg='LightPink1')
        self.filling_label.grid(row=0, column=2)
        self.filling_label.config(font=("Helvetica", 12))
        
        # Cake Filling variable to hold the option
        self.filling_menu = StringVar(self.frame)
        self.filling_menu.set("     ")        
        
        # The OptionMenu widget -- Cake Filling
        cakefilling_menu = OptionMenu(self.frame, self.filling_menu, *cake_filling)
        cakefilling_menu.grid(row=1, column=2, ipadx=35)
        cakefilling_menu.config(font=("Helvetica", 12)) 
        
        """-------------------------------------------------------------------"""
        
        self.l_label = Label(self.frame, text="---------------------------------", bg='LightPink1', fg="LightPink1")
        self.l_label.grid(row=3, column=1, ipady=10)
        
        """-------------------------------------------------------------------"""  
        
        # Additional decorations
        self.deco_label = Label(self.frame, text="Additional Decoration", bg='LightPink1')
        self.deco_label.grid(row=4, column=0, ipady=5)
        self.deco_label.config(font=("Helvetica", 12))
        
        self.deco_text = Text(self.frame, width=40, height=14)
        default_msg1 = "Enter any additional decorations you would like added here"
        self.deco_text.insert(END, default_msg1)
        self.deco_text.grid(row=5, column=0)
        
        """-------------------------------------------------------------------"""  
        
        # Additional information
        self.info_label = Label(self.frame, text="Additional Information", bg='LightPink1')
        self.info_label.grid(row=4, column=2, ipady=5)
        self.info_label.config(font=("Helvetica", 12))
        
        self.info_text = Text(self.frame, width=40, height=14)
        default_msg2 = "Enter any additional information that need to be considered"
        self.info_text.insert(END, default_msg2)
        self.info_text.grid(row=5, column=2)         
        
        """-------------------------------------------------------------------"""
        
        # Save button and Spaces
        self.l_label = Label(self.frame, text="---------------------------------", bg='LightPink1', fg="LightPink1")
        self.l_label.grid(row=7, column=1, ipady=10)   
        
        self.l_label = Label(self.frame, text="---------------------------------", bg='LightPink1', fg="LightPink1")
        self.l_label.grid(row=8, column=1, ipady=10)
        
        self.l_label = Label(self.frame, text="---------------------------------", bg='LightPink1', fg="LightPink1")
        self.l_label.grid(row=9, column=1, ipady=10)        
        
        save_button = Button(self.frame, text="Save", command=self.save_value)
        save_button.grid(row=10, column=1, ipadx=10) 
        
        """-------------------------------------------------------------------"""
        
        self.button_next = Button(self.frame, text="Next", command=self.open_contact_window)
        self.button_next.grid(row=10, column=2, sticky=E, ipadx=10)        
        
        """-------------------------------------------------------------------"""
        
        # Define Cake images option in the dropdown
        self.cake_img = []  # empty list to store the image paths
        for img in cake:
            self.cake_img.append(ImageTk.PhotoImage(Image.open(img).resize((300, 220))))  # add resized image to the list
            
        # Create OptionMenu for selecting cake image
        self.img_var = StringVar(self.frame)
        self.img_var.set("0")  # default value
        self.img_dropdown = OptionMenu(self.frame, self.img_var, "0", "1", "2", "3", "4", command=self.update_image)
        self.img_dropdown.grid(row=6, column=1, ipadx=10)
        
        # create frames for images
        self.img_label = Label(self.frame, text="Reference Image", bg='LightPink1')
        self.img_label.grid(row=4, column=1)
        self.img_label.config(font=("Helvetica", 12))
        self.img_frame = Frame(self.frame, width=380, height=300)
        self.img_frame.grid(row=5, column=1)
        self.label = Label(self.img_frame, image=self.cake_img[0], bg='LightPink1')  # set the default image to the first image in the list
        self.label.grid(row=5, column=1)
        
    def update_image(self, option):
        index = int(option)
        self.label.config(image=self.cake_img[index])  # update the image displayed in the label
        
        
        """-------------------------------------------------------------------"""        
        
    def save_value(self):
        
        selected_type = self.type_menu.get()
        selected_size = self.size_menu.get()
        selected_filling = self.filling_menu.get()
        selected_img = self.img_var.get()
        
        if (self.deco_text.get("1.0", "end-1c") == "Enter any additional decorations you would like added here") or (self.deco_text.get("1.0", "end-1c") == None):
            selected_deco = 'NULL'
        else:
            selected_deco = self.deco_text.get("1.0", "end-1c")
            
        if (self.info_text.get("1.0", "end-1c") == "Enter any additional information that need to be considered") or (self.info_text.get("1.0", "end-1c") == None):
            selected_info = 'NULL'
        else:
            selected_info = self.info_text.get("1.0", "end-1c")        
        
        # SQLite database and table
        conn = sqlite3.connect("cakeorder_db.db")
        c = conn.cursor()
        c.execute("INSERT INTO cake_details (size, type, filling, additional_decorations, additional_info, reference_image) VALUES (?, ?, ?, ?, ?, ?)", (selected_size, selected_type, selected_filling, selected_deco, selected_info, selected_img))

        conn.commit()
        conn.close()
        
        """-------------------------------------------------------------------"""
        
    def open_contact_window(self):
        #create_new_window()
        proc=subprocess.Popen(["python", "main.py"])
        #close the current GUI
        root.destroy()
        # allows the new_gui to stay
        proc.wait()
        
        
        


root = Tk()
root.geometry("1100x600")
cake = Cake_details(root)
root.mainloop()
