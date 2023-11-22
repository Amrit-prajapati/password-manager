from tkinter import *
import random2 as random
from tkinter import messagebox

#  Window creation 
window  = Tk()
window.title("Password Manager")
window.config(padx = 50 , pady = 50)
window.minsize(height = 280, width = 450)
window.maxsize(height = 280, width = 450)

# saving details
def savdetails():
    if (webInput.get() and emailInput.get() and passinput.get()):
        is_ok = messagebox.askokcancel(title = webInput.get() , message = f"Do you want to save the following details as \n Website : {webInput.get()} \n Email: {emailInput.get()} \n Password : {passinput.get()}")
        if is_ok == True:
            with open("data.txt" , "a") as file:
                file.write(f"{webInput.get()} | {emailInput.get()} | {passinput.get()} \n")        
            webInput.delete(0, END)
            emailInput.delete(0, END)
            passinput.delete(0, END)

# random password genetator
letters = ['a','b','c','d','e', 'f', 'g', 'h' , 'i' , 'j' , 'k', 'l', 'm' , 'n' ,'o' , 'p' , 'q' ,'r', 's' ,'t' ,'u', 'v', 'w' , 'x' , 'y' ,'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
digits = ["1","2","3","4","5","6","7","8","9"]
characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ")", "-", "_", "+", "-", "/", '|']
def createpass():
    passinput.delete(0, END)
    password_letter = [random.choice(letters) for _ in range (random.randint(8, 10))]
    password_digits = [random.choice(digits) for _ in range(random.randint(2, 5))]
    password_cha = [random.choice(characters) for _ in range(random.randint(2, 5))]
    endpassarr = password_cha + password_letter + password_digits
    random.shuffle(endpassarr)
    endpass = ""
    for i in endpassarr:
        endpass += (i)
    passinput.insert(0, endpass)


# Canvas Creation  
img = PhotoImage(file = "lock.png")
canvas = Canvas(height = 100, width = 100)
canvas.create_image(50,50, image = img)
canvas.grid(row = 0, column = 1)

#  GUI creation
website_label = Label(text="Website")
webInput =  Entry(width= 35)
webInput.focus()
email_label = Label(text = "Email / Username" )
emailInput = Entry(width=35)
password_label = Label(text = "Password" )
passinput = Entry(width=35)
generatepassword = Button(text = "Generate Password" , width=14 , command = createpass)
addbtn = Button(text = "Add", width=36 , command = savdetails)
website_label.grid(row = 1, column= 0)
webInput.grid(row = 1 , column = 1, columnspan = 2) 
email_label.grid(row = 2, column =0)
emailInput.grid(row = 2, column = 1, columnspan = 2)
password_label.grid(row = 3, column =0)
passinput.grid(row = 3, column =1 , columnspan =2)
generatepassword.grid(row = 3, column = 2)
addbtn.grid(row = 4, column = 1 , columnspan = 2)
window.mainloop()
