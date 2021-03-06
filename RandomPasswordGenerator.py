import random
from tkinter import *
import string
import pyperclip



def generate_password():
	copyBtn.config(text = "Copy Password")
	password = ' '

	for n in range(5):
		password += random.choice(string.digits)
		password += random.choice(string.ascii_letters)
		password += random.choice(string.punctuation)

	lbl.config(text = password)
	
def copy_password():
	copyBtn.config(text = "Copied!")
	pyperclip.copy(lbl['text'])


root = Tk()
root.title("Password Generator")
root.geometry("250x200")
GPbtn = Button(root, text= "Generate Password", command= generate_password)
GPbtn.place(relx= 0.5, rely= 0.0 , anchor= N )
lbl = Label(root,font=("times",15,"bold"), height =  1, width = 20 ,borderwidth=2, relief ="solid")
lbl.place(relx = 0.5, rely = 0.23, anchor= N)
copyBtn = Button(root, text="Copy Password", height = 1, width = 15, command = copy_password)
copyBtn.place(relx=0.5,rely=0.5, anchor = CENTER)
root.mainloop()
