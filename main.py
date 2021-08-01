import tkinter as tk
from tkinter import END, messagebox
from pass_gen import generate

# ---------------------------- COLORS ------------------------------------------#
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
    website = input_web.get()
    login = input_login.get()
    password = input_password.get()

    if website == '' or login == '' or password == '':
        messagebox.showinfo(title='Uncompleted Form', message='The form is uncompleted. \nPlease fill all the camps and'
                                                              ' try again.')
    else:
        user_confirm = messagebox.askyesno(title=input_web, message=f'Is your data correct? \nLocation: {website} \nLogin: {login} '
                                                                    f'\nPasscode: {password}')
        if user_confirm:
            website = input_web.get()
            login = input_login.get()
            password = input_password.get()
            warning_label.config(text='')
            """
            If you want to change the data file name, substitute the 'data.txt' by the name you want. Also remember to 
            change the 'data.txt' file manually in the application files, or else you will create one new data file.
            """
            with open(file='data.txt', mode='a') as data_file:
                data_file.write(f'{website} | {login} | {password}\n')
                warning_label.config(text='Data saved successfully!')
                input_web.delete(first=0, last=END)
                input_password.delete(first=0, last=END)


# ---------------------------- UI SETUP ------------------------------- #
main_screen = tk.Tk()
main_screen.config(padx=35, pady=40, bg=RED)
main_screen.title('Password Manager')

logo = tk.PhotoImage(file='logo.png')

canvas = tk.Canvas(width=200, height=200, bg=RED, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=2, row=1)

indicator_web = tk.Label(text='Website:', fg=LIGHT_COLOR2, bg=RED, font=('Comic Sans', 15))
indicator_web.grid(column=1, row=2)

input_web = tk.Entry(width=47)
input_web.grid(column=2, row=2, columnspan=2)
input_web.focus()

indicator_login = tk.Label(text='Email/Username:', fg=LIGHT_COLOR2, bg=RED, font=('Comic Sans', 15))
indicator_login.grid(column=1, row=3)

input_login = tk.Entry(width=47)

'''
    You can change the email below to your main email or add a "#" to the beginning of the line to comment it and the
    program will automatically ignore the command line.
'''
input_login.insert(END, string='example@gmail.com')


input_login.grid(column=2, row=3, columnspan=2)

indicator_password = tk.Label(text='Password:', fg=LIGHT_COLOR2, bg=RED, font=('Comic Sans', 15))
indicator_password.grid(column=1, row=4)

input_password = tk.Entry(width=26)
input_password.grid(column=2, row=4)

generate_password_btn = tk.Button(text='Generate Password', fg=RED, bg=LIGHT_COLOR1, highlightthickness=0)
generate_password_btn.config(command=password_fill)
generate_password_btn.grid(column=3, row=4)

add_btn = tk.Button(text='Add Password', width=45, fg=RED, bg=LIGHT_COLOR1, highlightthickness=0)
add_btn.config(command=save)
add_btn.grid(column=2, row=5, columnspan=2)

warning_label = tk.Label(fg=LIGHT_COLOR2, bg=RED, text='')
warning_label.grid(column=2, row=6, columnspan=2)

main_screen.mainloop()
