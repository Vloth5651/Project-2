from tkinter import ttk
from tkinter import *
from tkcalendar import *
import tkinter.font
from tkinter import messagebox

from tkinter import PhotoImage


window = tkinter.Tk()
window.title("Let's get started!")
window.minsize(width=500, height=700)
window.configure(bg="LightPink1")
#filename=PhotoImage(file="cakes.jpeg")

# creating main frame
main_frame= Frame(root)
main_frame.pack(fill=BOTH, expand=1)

#SCROLLBAR (created using a codemy YouTube tutorial)

# creating a canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTh, expand=1)

# Adding a scrollbar to the canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scroolbar.pack(side=RIGHT, fill=Y)

# configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure()

# create another frame inside the canvas
second_frame = Frame(my_canvas)

# add that new frame to a window in the canvas
my_canvas.create_window((0,0), window= second_frame, anchor= "nw")

frame = tkinter.Frame(window)
frame.pack()

# shop name
#shop_intro = Label(text= "Simply Start your order.", font= ("Helvetica", 20, "bold"), bg='tomato')
#shop_intro.grid(column=1, row=0)

# shop quote
##quote = Label(text= "Currently serving multiple locations at 3 cities in the GTA!", font= ("Helvetica", 20, "bold"), bg='tomato')
#quote.grid(column=1, row=0)


# saving user's personal info
customer_info_frame =tkinter.LabelFrame(frame, text= "Order Information")
customer_info_frame.grid(row=0, column=0, padx=20, pady=20)

name_label = tkinter.Label(customer_info_frame, text="Order Name")
name_label.grid(row=0, column=0)
address_label = tkinter.Label(customer_info_frame, text= "Order Method")
address_label.grid(row=0, column=1)

name_entry = tkinter.Entry(customer_info_frame)
name_entry.grid(row=1, column=0)

# choosing order method
method_label = tkinter.Label(customer_info_frame, text="Order Method")
method_combobox = ttk.Combobox(customer_info_frame, values=["Delivery", "Pickup"])
method_label.grid(row=0, column=1)
method_combobox.grid(row=1, column=1)

# choosing city
city_label = tkinter.Label(customer_info_frame, text="Choose Your City")
city_combobox = ttk.Combobox(customer_info_frame, values=["Mississauga", "Oakville", "Brampton"])
city_label.grid(row=2, column=0)
city_combobox.grid(row=3, column=0)

#saving address details

address_frame =tkinter.LabelFrame(frame, text= "Delivery Details")
address_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)


#street and house/unit number
street_label = tkinter.Label(address_frame, text="Street Address")
street_label.grid(row=1, column=0)

# postal code entry
street_entry = tkinter.Entry(address_frame)
street_entry.grid(row=2, column=0)

postal_label = tkinter.Label(address_frame, text="Postal Code")
postal_label.grid(row=1, column=1)

postal_entry = tkinter.Entry(address_frame)
postal_entry.grid(row=2, column=1)

# billing address
billing_label = tkinter.Label(address_frame, text= "Billing Address")
billing_check = tkinter.Checkbutton(address_frame, text="Same as Delivery Address")
billing_label.grid(row=3, column=0)
billing_check.grid(row=4, column=0)

# contact details frame

contact_frame =tkinter.LabelFrame(frame, text= "Contact Details")
contact_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)

# phone number entry
phone_label =tkinter.Label(contact_frame, text= "Phone Number")
phone_label.grid(row=3, column=0)

phone_entry = tkinter.Entry(contact_frame)
phone_entry.grid(row=4, column=0)

# email address entry
email_label = tkinter.Label(contact_frame, text= "Email Address")
email_label.grid(row=5, column=0, padx= 20, pady =20)

email_entry = tkinter.Entry(contact_frame)
email_entry.grid(row=6, column=0)

# date and time
date_info_frame =tkinter.LabelFrame(frame, text= "Date and Time")
date_info_frame.grid(row=3, column=0, sticky= "news", padx=20, pady=20)

cal= Calendar(date_info_frame, selectmode="day", year=2020, month=5, day=22 )
cal.pack(pady=20)

# choose date from calendar, (using Tkinter's built in calendar widget)
def grab_date():
    my_label.config(text=cal.get_date())

my_button =Button(date_info_frame, text= "Select Date", command= grab_date)
my_button.pack(pady=20)

# choose time
time_info_frame =tkinter.LabelFrame(frame, text= "Contact Details")
time_info_frame.grid(row=4, column=0, sticky="news", padx=20, pady=20)

time_label =tkinter.Label(time_info_frame, text= "Timing")
time_label.grid(row=4, column=1)

time = tkinter.Entry(time_info_frame)
time.grid(row=4, column=1)

Button(base, text="Submit", width=10).place(x=200,y=400)
base.mainloop()




def on_close():
    response=messagebox.askyesno('Exit Form','Are you sure you want to leave without submitting your order?')
    if response:
        window.destroy()


window.protocol('WM_DELETE_WINDOW',on_close)

#submit button

def callback():
    print "Sweet! You've submitted your Order"

SaveButton = Button(top, text="Save Details", width=10, command=callback)
SaveButton.grid(row=1, column=1)



window.mainloop()












