from tkinter import tk
window = Tk()
window.title("Simply Sweet Cake Shop")
window.minisize(width=500, height=700)
window.configure(bg="rosybrown1")

# our shop's name label
shop_name = Label(text='Welcome to\nSimply Sweet Cake Shop'), font= ("Times New Roman", 20, "bold") bg= "rosybrown1"
shop_name.grid(column=1, row=0)

# intro quote/slogan
quote = Label(text="Simply baked with love",) font=("helv36' = tkFont.Font(family="Helvetica"),size=36,weight="bold"))
quote.grid(column=1, row=2)

# type of cake label
cakes_label = Label(Label(text='Choose the type of cake yod would like'), font= ('helv36' = tkFont.Font(family="Helvetica"),size=36,weight="bold"))
window.mainloop()




