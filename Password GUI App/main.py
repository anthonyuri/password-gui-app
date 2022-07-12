from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
        email = data[website]["email"]
        password = data[website]["password"]

    except FileNotFoundError:
        error = messagebox.showinfo(title="Error", message=f"No details for the website exists.")
    except KeyError:
        error = messagebox.showinfo(title="Error", message=f"No Data File Found.")
    else:
        data_display = messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password} ")








# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for c in range(randint(8, 10))]
    symbols_list = [choice(symbols) for c in range(randint(2, 4))]
    numbers_list = [choice(numbers) for c in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    emailUser = emailUser_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": emailUser,
            "password": password
        }
    }

    if website == "" or emailUser == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="website", message=f"These are the details entered: \nEmail: {emailUser} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    #Reading old data
                    data = json.load(data_file)
                    #Updating old data with new data
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", "w") as data_file:
                    #savings updated data
                    json.dump(data, data_file, indent=4)
            finally:
                    website_entry.delete(0, END)
                    pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)
# window.geometry("400x400")

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1, sticky="EW")

#labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="EW")

emailUser_label = Label(text="Email/Username:")
emailUser_label.grid(row=2, column=0, sticky="EW")

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0, sticky="EW")


#entrys
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, sticky="EW")

emailUser_entry = Entry(width=35)
emailUser_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
emailUser_entry.insert(0, "umasgupta@gmail.com")
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1, sticky="EW")

#buttons

search = Button(text="Search", command=find_password)
search.grid(row=1, column=2, sticky="EW")

create_pass = Button(text="Generate Password", command=generate_password)
create_pass.grid(row=3, column=2, sticky="EW")

add = Button(text="Add", width=36, command=save_data)
add.grid(row=4, column=1, columnspan=2, sticky="EW")







window.mainloop()