import tkinter as tk
from tkinter import ttk, messagebox
import database

class LogiXApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LogiX - Tkinter + SQLite3 User Login App")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        database.setup_tables()
        self.home_screen()

    def home_screen(self):
        self.clear_window()
        frame = tk.Frame(self.root, bg="LightBlue")
        frame.pack(fill="both", expand=True)
        
        tk.Button(frame, text="Login", command=self.login_screen, font=("Calibri", 14)).place(x=220, y=150, width=100, height=30)
        tk.Button(frame, text="Register", command=self.register_screen, font=("Calibri", 14)).place(x=330, y=150, width=100, height=30)

    def register_screen(self):
        self.clear_window()
        frame = tk.Frame(self.root, bg="LightBlue")
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Username", bg="LightBlue").place(x=180, y=120)
        tk.Label(frame, text="Password", bg="LightBlue").place(x=180, y=160)
        tk.Label(frame, text="CN", bg="LightBlue").place(x=180, y=200)

        username = tk.StringVar()
        password = tk.StringVar()
        cn = tk.StringVar()

        tk.Entry(frame, textvariable=username).place(x=280, y=120)
        tk.Entry(frame, textvariable=password, show="*").place(x=280, y=160)
        tk.Entry(frame, textvariable=cn).place(x=280, y=200)

        def register():
            if username.get() and password.get():
                database.insert_user(username.get(), password.get(), cn.get())
                messagebox.showinfo("Success", "User Registered!")
                self.home_screen()
            else:
                messagebox.showwarning("Error", "All fields required!")

        tk.Button(frame, text="Register", command=register).place(x=260, y=250, width=100)
        tk.Button(frame, text="Back", command=self.home_screen).place(x=20, y=350, width=80)

    def login_screen(self):
        self.clear_window()
        frame = tk.Frame(self.root, bg="LightBlue")
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Username", bg="LightBlue").place(x=180, y=150)
        tk.Label(frame, text="Password", bg="LightBlue").place(x=180, y=190)

        username = tk.StringVar()
        password = tk.StringVar()

        tk.Entry(frame, textvariable=username).place(x=280, y=150)
        tk.Entry(frame, textvariable=password, show="*").place(x=280, y=190)

        def login():
            user = database.validate_user(username.get(), password.get())
            if user:
                self.dashboard()
            else:
                messagebox.showerror("Error", "Invalid username or password")

        tk.Button(frame, text="Login", command=login).place(x=260, y=230, width=100)
        tk.Button(frame, text="Back", command=self.home_screen).place(x=20, y=350, width=80)

    def dashboard(self):
        self.clear_window()
        nb = ttk.Notebook(self.root)
        nb.pack(fill="both", expand=True)
        
        # Tabs (Insert, View, Search, Update, Delete)
        from sections import insert_tab, view_tab, search_tab, update_tab, delete_tab
        insert_tab(nb)
        view_tab(nb)
        search_tab(nb)
        update_tab(nb)
        delete_tab(nb)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

