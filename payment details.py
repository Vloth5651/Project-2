from tkinter import ttk
from tkinter import *
import tkinter.font
from tkinter import messagebox
import subprocess

import sqlite3


window = tkinter.Tk()
window.title("Ready to Pay?")
window.minsize(width=500, height=600)
window.configure(bg="LightPink1")

frame = tkinter.Frame(window)
frame.pack(pady=10)

img = PhotoImage(file='cake.gif').subsample(2, 2)
img_label= Label(window, image=img, bg='white')
img_label.pack(anchor="center", padx=10, pady=10)



# saving payment info
payment_info_frame =tkinter.LabelFrame(frame, text= "Order Information")
payment_info_frame.grid(row=0, column=0, padx=20, pady=20)

# choose card type
card_label = tkinter.Label(payment_info_frame, text="Choose Payment Method")
card_combobox = ttk.Combobox(payment_info_frame, values=["Debit", "Credit"])
card_label.grid(row=1, column=0)
card_combobox.grid(row=2, column=0)

# card name
card_name_label = tkinter.Label(payment_info_frame, text="Name as it appears on Card")
card_name_label.grid(row=3, column=0)

card_name_entry = tkinter.Entry(payment_info_frame)
card_name_entry.grid(row=4, column=0)

# card number
card_number_label = tkinter.Label(payment_info_frame, text= "Card Number")
card_number_label.grid(row=5, column=0)

card_number_entry = tkinter.Entry(payment_info_frame)
card_number_entry.grid(row=6, column=0)

# csv number
csv_number_label = tkinter.Label(payment_info_frame, text= "CSV")
csv_number_label.grid(row=7, column=0)

csv_number_entry = tkinter.Entry(payment_info_frame)
csv_number_entry.grid(row=8, column=0)

# expiry number
expiry_number = tkinter.Label(payment_info_frame, text= "Expiry (format: YYYY-MM-DD)")
expiry_number.grid(row=9, column=0)

expiry_number_entry = tkinter.Entry(payment_info_frame)
expiry_number_entry.grid(row=10, column=0)

def save_details():
    selected_method = card_combobox.get()
    name = card_name_entry.get()
    card_num = int(card_number_entry.get())
    csv_num = int(csv_number_entry.get())
    expiry_date = expiry_number_entry.get()

    # SQLite database and table
    conn = sqlite3.connect("cakeorder_db.db")
    c = conn.cursor()
    c.execute("INSERT INTO payment_details (name, pay_method, card_num, csv, expiry) VALUES (?, ?, ?, ?, ?)", (name, selected_method, card_num, csv_num, expiry_date))
    conn.commit()
    conn.close()

     #create_new_window()
    proc=subprocess.Popen(["python", "ThankYou.py"])
    #close the current GUI
    window.destroy()
    # allows the new_gui to stay
    proc.wait()

submit_button = Button(window, text="Submit Order", width=10, command=save_details)
submit_button.pack(anchor="center")



window.mainloop()


window.mainloop()