import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# -------password generator-----#

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '=']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# -----save ------#
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="please make sure you havent left empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# --------------Search-----------------#
def find_password():
    website = website_entry.get()
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        if website in data:
            email=data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \n Password:{password}")



# -----UI set UP--------------#

window = Tk()
window.title("Password Manager")
window.config(padx=10, pady=10)

canvas = Canvas(height=240, width=240)
logo_img = PhotoImage(file="download.png")
canvas.create_image(120, 120, image=logo_img)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="website")
website_label.grid(row=1, column=0)
email_label = Label(text="email")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1)
website_entry.focus()
Search = Button(text="Search", width=14, command=find_password)
Search.grid(row=1, column=2, columnspan=2)
email_entry = Entry(width=59)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=40)
password_entry.grid(row=3, column=1)

# buttons
Generate = Button(text="Generate password", width=14, command=generate_password)
Generate.grid(row=3, column=2)
add_button = Button(text="Add", width=48, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
