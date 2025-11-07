"""
LogiX Student Management System
Entry point of the application
"""
from tkinter import Tk
from src.gui import create_home_screen


def main():
    root = Tk()
    root.geometry('600x400')
    root.resizable(0, 0)
    root.title('LogiX')
    
    create_home_screen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
