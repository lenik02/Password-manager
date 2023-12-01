from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    input_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    generated_password = "".join(password_list)
    input_password.insert(0, generated_password)
    pyperclip.copy(generated_password)


# Search password
def find_password():
    website = input_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="File", message="File data do not exist")
    else:
        if website in data:
            mail = data[website]["mail"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Mail: {mail}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message="No details for the website exist")


# Save password
def save():
    website = input_website.get()
    mail = input_mail.get()
    password = input_password.get()
    new_data = {
        website: {
            "mail": mail,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Don't leave empty fields")
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
                # write updated data to file
                json.dump(new_data, data_file, indent=4)
        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password generator")
window.config(padx=50, pady=50)
# Canvas with image
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Label Website
label_website = Label(text="Website")
label_website.grid(column=0, row=1)

# Entry website
input_website = Entry(width=21)
input_website.grid(column=1, row=1, columnspan=2, sticky="EW")
input_website.focus()
input_website.get()

# button search
password_button = Button(text="Search", command=find_password)
password_button.grid(column=2, row=1, sticky="EW")

# Label Email
label_website = Label(text="Email/Username")
label_website.grid(column=0, row=2)

# Entry email
input_mail = Entry(width=35)
input_mail.grid(column=1, row=2, columnspan=2, sticky="EW")
input_mail.insert(0, "pipal@mail.com")
input_mail.get()

# Label password
label_password = Label(text="Password")
label_password.grid(column=0, row=3)

# Entry password
input_password = Entry(width=21, highlightthickness=0, )
input_password.grid(column=1, row=3, sticky="EW")
input_password.get()
# button generate password
password_button = Button(text="Generate password", command=generate_password)
password_button.grid(column=2, row=3, sticky="EW")

# button Add
button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
