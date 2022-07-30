from tkinter import *
from tkinter import ttk, filedialog
import tkinter
import os
import re

WINDOW_TITLE = 'Password Manager'
MASTER_FILE = 'masterpassword.txt'
CREATE_MASTER_TEXT = 'Create master password'
CONFIRM_MASTER_TEXT = 'Confirm master password'
PASSWORD_NOT_SECURE_WARNING = 'Password should have atleast 12 characters, atleast one UPPERCASE letter and atleast two special characters: ~!@#$%^&*()+=\{\}:;<>-?'
PASSWORD_DONT_MATCH_WARNING = 'Passwords do not match'

root = Tk()
root.title(WINDOW_TITLE)
root.geometry("400x400")
root.minsize(400, 400)
root.maxsize(400, 400)
mainframe = ttk.Frame(root, padding=50)
mainframe.grid()


# Label for error messages at the bottom
error_label = ttk.Label(mainframe, text='', wraplength=250)
error_label.grid(column=0, row=7, pady=(30, 0))

isLoggedIn = False
firstUse = True

#print(os.path.dirname(os.path.realpath(__file__)))

if os.path.exists(MASTER_FILE):
    firstUse = False

def createMaster(password, password_confirm):
    global isLoggedIn
    
    if password == password_confirm:
        print('Passwords match')
        isStrongPassword = checkStrongPassword(password)
        if isStrongPassword:
            isLoggedIn = True
            loggedIn()
            pass
        else:
            error_label.configure(text=PASSWORD_NOT_SECURE_WARNING)
            pass
    else:
        error_label.configure(text=PASSWORD_DONT_MATCH_WARNING)
        print('Passwords do not match')


def checkStrongPassword(password: str):
    minTwoNumbers_Pattern = re.compile(".*([0-9]).*([0-9]).*")
    minTwoSpecialCharacters_Pattern = re.compile(".*[`.~!@#$%^&*()+=\{\}:;<>-?].*[`.~!@#$%^&*()+=\{\}:;<>-?].*")
    
    # Is all lowercase
    if password.islower():
        print('is full owercase')
        return False
    # Is only numbers
    if password.isdecimal():
        print('is fully decimal')
        return False
    # Has less than 12 characters
    if len(password) < 12:
        print('less than 12 chars')
        return False
    # has not atleast 2 special characters
    if not minTwoSpecialCharacters_Pattern.match(password):
        print('Has no 2 special chars')
        return False
    # has not atleast 2 numbers
    if not minTwoNumbers_Pattern.match(password):
        print('has no 2 numbers')
        return False

    return True

def ToggleShowPassword(checkbox_value, entry, entry_confirm):
    if checkbox_value == 1:
        entry.configure(show='')
        entry_confirm.configure(show='')
    else:
        entry.configure(show='*')
        entry_confirm.configure(show='*')



def register():
    # Create master password label
    create_master_label = ttk.Label(mainframe, text=CREATE_MASTER_TEXT)
    create_master_label.grid(column=0, row=0, pady=5)

    # Create master password entry
    create_master_entry_text = StringVar()
    create_master_entry = ttk.Entry(mainframe, width=50, textvariable=create_master_entry_text, show='*')
    create_master_entry.grid(column=0, row=1, pady=(0, 15))

    # Create master password CONFIRM label
    create_master_confirm_label = ttk.Label(mainframe, text=CONFIRM_MASTER_TEXT)
    create_master_confirm_label.grid(column=0, row=3, pady=5)

    # Create master password CONFIRM entry
    create_master_entry_confirm_text = StringVar()
    create_master_entry_confirm = ttk.Entry(mainframe, width=50, textvariable=create_master_entry_confirm_text, show='*')
    create_master_entry_confirm.grid(column=0, row=4)

    # Creater master password button
    create_master_button = ttk.Button(mainframe, text="Create Password", command=lambda: createMaster(create_master_entry_text.get(), create_master_entry_confirm_text.get()))
    create_master_button.grid(column=0, row=5, pady=(20, 0))

    cb_val = IntVar()
    cb_val.set(0)
    password_checkbox = ttk.Checkbutton(mainframe, variable=cb_val, text='Show password', command=lambda: ToggleShowPassword(cb_val.get(), create_master_entry, create_master_entry_confirm))
    password_checkbox.grid(column=0, row=6, pady=(20,0))

def loggedIn():
    label = ttk.Label(mainframe, text="Hello World")
    label.grid(column=0, row=0)

if firstUse == True:
    register()
else:
    loggedIn()


root.mainloop()

