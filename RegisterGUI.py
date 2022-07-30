from tkinter import *
from tkinter import ttk
import re

WINDOW_TITLE = 'Password Manager'
MASTER_FILE = 'masterpassword.txt'
CREATE_MASTER_TEXT = 'Create master password'
CONFIRM_MASTER_TEXT = 'Confirm master password'
PASSWORD_NOT_SECURE_WARNING = 'Password should have atleast 12 characters, atleast one UPPERCASE letter and atleast two special characters: ~!@#$%^&*()+=\{\}:;<>-?'
PASSWORD_DONT_MATCH_WARNING = 'Passwords do not match'

class RegisterGUI(self, ):
    def __init__(self):
        # Label for error messages at the bottom
        error_label = ttk.Label(ttk.Frame, text='', wraplength=250)
        error_label.grid(column=0, row=7, pady=(30, 0))

        # Create master password label
        self.master_label = ttk.Label(ttk.Frame, text=CREATE_MASTER_TEXT)
        self.master_label.grid(column=0, row=0, pady=5)

        # Create master password entry
        self.master_entry_text = StringVar()
        self.master_entry = ttk.Entry(ttk.Frame, width=50, textvariable=self.master_entry_text, show='*')
        self.master_entry.grid(column=0, row=1, pady=(0, 15))

        # Create master password CONFIRM label
        self.master_confirm_label = ttk.Label(ttk.Frame, text=CONFIRM_MASTER_TEXT)
        self.master_confirm_label.grid(column=0, row=3, pady=5)

        # Create master password CONFIRM entry
        self.master_entry_confirm_text = StringVar()
        self.master_entry_confirm = ttk.Entry(ttk.Frame, width=50, textvariable=self.master_entry_confirm_text, show='*')
        self.master_entry_confirm.grid(column=0, row=4)

        # Creater master password button
        self.master_button = ttk.Button(ttk.Frame, text="Create Password", command=self.createMaster)
        self.master_button.grid(column=0, row=5, pady=(20, 0))

        self.checkbox_value = IntVar()
        self.checkbox_value.set(0)
        self.password_checkbox = ttk.Checkbutton(ttk.Frame, variable=self.checkbox_value, text='Show password', command=self.ToggleShowPassword)
        self.password_checkbox.grid(column=0, row=6, pady=(20,0))

    def ToggleShowPassword(self):
        if self.checkbox_value == 1:
            self.master_entry.configure(show='')
            self.master_entry_confirm.configure(show='')
        else:
            self.master_entry.configure(show='*')
            self.master_entry_confirm.configure(show='*')
    
    def createMaster(self):
        password = self.master_entry_text.get()
        password_confirm = self.master_entry_confirm_text.get()

        if password == password_confirm:
            isStrongPassword = self.checkStrongPassword(password)
            
            if isStrongPassword:
                self.login()
            
            else:
                self.error_label.configure(text=PASSWORD_NOT_SECURE_WARNING)
    
        else:
            self.error_label.configure(text=PASSWORD_DONT_MATCH_WARNING)
            print('Passwords do not match')
    
    def checkStrongPassword(self):
        minTwoNumbers_Pattern = re.compile(".*([0-9]).*([0-9]).*")
        minTwoSpecialCharacters_Pattern = re.compile(".*[`.~!@#$%^&*()+=\{\}:;<>-?].*[`.~!@#$%^&*()+=\{\}:;<>-?].*")
        
        password = self.master_entry_text.get()

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
    
    def login(self):
        self.tearDown()
        pass

    def tearDown(self):
        self.master_entry.delete()
        self.master_entry_confirm.delete()
        self.master_label.delete()
        self.master_confirm_label.delete()
        self.password_checkbox.delete()
        self.master_button.delete()
        pass


    