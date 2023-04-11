from tkinter import ttk
from tkinter import *
import tkinter.font
from tkinter import messagebox


window = tkinter.Tk()
window.title("Ready to Pay?")
window.minsize(width=500, height=700)
window.configure(bg="LightPink1")

frame = tkinter.Frame(window)
frame.pack()

img = PhotoImage(file='cake.gif')
Label(window, image=img, bg='white').place(x=300, y=300)


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
expiry_number = tkinter.Label(payment_info_frame, text= "Expiry")
expiry_number.grid(row=9, column=0)

expiry_number_entry = tkinter.Entry(payment_info_frame)
expiry_number_entry.grid(row=10, column=0)

Button(window, text="Submit Order", width=10).place(x=200,y=400)
window.mainloop()


window.mainloop()