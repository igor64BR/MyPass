import json
import tkinter as tk
from tkinter import END, messagebox
from pass_gen import generate
import json

# ---------------------------- VARIABLES ------------------------------------------#
data_file_location = '/home/baiocco/a100DoC_projects/day-29-MyPass/data.json'
default_login = '@gmail.com'
RED = '#8D2828'
LIGHT_COLOR1 = '#ECEFA4'
LIGHT_COLOR2 = '#D9DD6B'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_fill():
    new_password = generate()

    input_password.delete(first=0, last=END)
    input_password.insert(END, string=new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_web.get().upper()
    login = input_login.get()
    password = input_password.get()
    new_data = {
        website: {
            'login': login,
            'password': password
        }
    }

    if website == '' or login == '' or password == '':
        messagebox.showinfo(title='Uncompleted Form', message='The form is uncompleted. \nPlease fill all the camps and'
                                                              ' try again.')
    else:
        user_confirm = messagebox.askyesno(title=input_web, message=f'Is your data correct? \nLocation: {website} \nLogin: {login} '
                                                                    f'\nPasscode: {password}')
        if user_confirm:
            warning_label.config(text='')

            data = new_data

            try:
                with open(file=data_file_location, mode='r') as data_file:
                    try:
                        data = json.load(fp=data_file)
                        data.update(new_data)
                    except json.JSONDecodeError:
                        pass
            except FileNotFoundError:
                pass
            with open(file=data_file_location, mode='w') as data_file:
                json.dump(obj=data, fp=data_file, indent=4)

            warning_label.config(text='Data saved successfully!')
            input_web.delete(first=0, last=END)
            input_password.delete(first=0, last=END)


# ---------------------------- UI SETUP ------------------------------- #
def search():
    website = input_web.get().upper()
    try:
        with open(file=data_file_location, mode='r') as data_file:
            data = json.load(data_file)
        try:
            login = data[website]['login']
            password = data[website]['password']
            messagebox.showinfo(title=website.title(), message=f'Login: {login} \nPassword: {password}')
        except KeyError:
            messagebox.showinfo(title=website.title(), message='Oops! Apparently there is no website registered with that name')
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title='Oh No!', message='There aren\'t any passwords saved yet. Why don\'t you start '
                                                    'saving now?')


# ---------------------------- UI SETUP ------------------------------- #
main_screen = tk.Tk()
main_screen.config(padx=35, pady=40, bg=RED)
main_screen.title('Password Manager')

logo = tk.PhotoImage(file='/home/baiocco/a100DoC_projects/day-29-MyPass/logo.png')

canvas = tk.Canvas(width=200, height=200, bg=RED, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=2, row=1)

indicator_web = tk.Label(text='Website:', fg=LIGHT_COLOR2, bg=RED, font=('Comic Sans', 15))
indicator_web.grid(column=1, row=2)

input_web = tk.Entry(width=26)
input_web.grid(column=2, row=2)
input_web.focus()

indicator_login = tk.Label(text='Email/Username:', fg=LIGHT_COLOR2, bg=RED, font=('Comic Sans', 15))
indicator_login.grid(column=1, row=3)

input_login = tk.Entry(width=47)

'''
    You can change the email below to your main email or add a "#" to the beginning of the line to comment it and the
    program will automatically ignore the command line.
'''
input_login.insert(END, string=default_login)


input_login.grid(column=2, row=3, columnspan=2)

indicator_password = tk.Label(text='Password:', fg=LIGHT_COLOR2, bg=RED, font=('Comic Sans', 15))
indicator_password.grid(column=1, row=4)

input_password = tk.Entry(width=26)
input_password.grid(column=2, row=4)

generate_password_btn = tk.Button(text='Generate Password', fg=RED, bg=LIGHT_COLOR1, highlightthickness=0, width=16)
generate_password_btn.config(command=password_fill)
generate_password_btn.grid(column=3, row=4)

add_btn = tk.Button(text='Add Password', width=45, fg=RED, bg=LIGHT_COLOR1, highlightthickness=0)
add_btn.config(command=save)
add_btn.grid(column=2, row=5, columnspan=2)

search_btn = tk.Button(text='Search', fg=RED, bg=LIGHT_COLOR1, highlightthickness=0, command=search, width=16)
search_btn.grid(column=3, row=2)

warning_label = tk.Label(fg=LIGHT_COLOR2, bg=RED, text='')
warning_label.grid(column=2, row=6, columnspan=2)

main_screen.mainloop()
