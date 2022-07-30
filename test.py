from RegisterGUI import RegisterGUI
from tkinter import *
from tkinter import ttk

WINDOW_TITLE = 'Password Manager'



def main(): 
    root = Tk()
    root.title(WINDOW_TITLE)
    root.geometry("400x400")
    root.minsize(400, 400)
    root.maxsize(400, 400)
    mainframe = ttk.Frame(root, padding=50)
    mainframe.grid()

    register = RegisterGUI(mainframe)

    root.mainloop()

if __name__ == '__main__':
    main()