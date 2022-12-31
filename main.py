import random
import json
from json import JSONDecodeError

import pyperclip
from tkinter import *
from tkinter import messagebox

# -----------------------------FIND WEBSITE-------------------------------------- #


def find_website():
    with open("data.json", "r") as data:
        find_key = json.load(data)
        website = website_entry.get()
        try:
            website_key = find_key[website]["email"]
            password_key = find_key[website]["password"]
        except KeyError:
            messagebox.showinfo(title=website, message=f"No data found for this website")
        else:
            messagebox.showinfo(title=website, message=f"Email: {website_key}\nPassword: {password_key}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]

    password_symbols= [random.choice(symbols) for chars in range(random.randint(2, 4))]

    password_numbers = [random.choice(numbers) for chara in range(random.randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(password) == 0 and len(website) == 0:
        messagebox.showinfo(title="Oops!", message="Please do not leave any fields empty")
    elif len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Password field is empty")
    elif len(website) == 0:
        messagebox.showinfo(title="Oops!", message="Website field is empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data:
                    json_data = json.load(data)
            except (FileNotFoundError, JSONDecodeError):
                with open("data.json", "w") as data:
                    json.dump(new_data, data, indent=4)
            else:
                with open("data.json", "w") as data:
                    json_data.update(new_data)
                    json.dump(json_data, data, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=image)
canvas.grid(column=1, row=0)

# ----------------- LABELS ---------------- #

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# ---------------- ENTRIES ----------------- #
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky=W)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky=W)
email_entry.insert(0, "basseygodwin629@gmail.com")

password_entry = Entry(width=25)
password_entry.grid(column=1, row=3, sticky=W)


# ----------------- BUTTONS ---------------- #

generate_password = Button(text="Generate Password", command=password)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky=W)

search_button = Button(text="Search", command=find_website, width=10)
search_button.grid(column=2, row=1, padx=20)

window.mainloop()

