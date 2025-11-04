"""
LogiX GUI Module
Contains all Tkinter GUI components
"""
from tkinter import *
from tkinter import messagebox, ttk
import database as db

# Global reference to the ShowAll frame for refreshing
frame_showall = None

# ==================== Main Application Screen ====================
def create_main_screen(root):
    """Create the main notebook interface with all tabs"""
    ntb = ttk.Notebook(root)
    
    def on_tab_change(event):
        if ntb.index('current') == 5:  # Logout tab
            create_home_screen(root)
    
    ntb.bind('<<NotebookTabChanged>>', on_tab_change)
    ntb.place(x=0, y=0, width=600, height=400)
    
    # Add all tabs
    create_insert_tab(ntb)
    create_showall_tab(ntb)
    create_search_tab(ntb)
    create_update_tab(ntb)
    create_delete_tab(ntb)
    create_logout_tab(ntb)

# ==================== Insert Tab ====================
def create_insert_tab(ntb):
    """Create the Insert student data tab"""
    f4 = Frame(bg='LightBlue')
    ntb.add(f4, text='Insert')
    
    # Input variables
    roll_no = StringVar()
    name = StringVar()
    phy = StringVar()
    chem = StringVar()
    maths = StringVar()
    
    # Labels and Entries
    Label(f4, font=('Cambria', 15), text='Enter Roll No.', bg='LightBlue', fg='Red').place(x=150, y=50)
    Entry(f4, font=('Cambria', 15), textvariable=roll_no).place(x=300, y=50, width=100)
    
    Label(f4, font=('Cambria', 15), text='Enter Name', bg='LightBlue', fg='Red').place(x=150, y=100)
    Entry(f4, font=('Cambria', 15), textvariable=name).place(x=300, y=100, width=100)
    
    Label(f4, font=('Cambria', 15), text='Enter Phy.', bg='LightBlue', fg='Red').place(x=150, y=150)
    Entry(f4, font=('Cambria', 15), textvariable=phy).place(x=300, y=150, width=100)
    
    Label(f4, font=('Cambria', 15), text='Enter Chem.', bg='LightBlue', fg='Red').place(x=150, y=200)
    Entry(f4, font=('Cambria', 15), textvariable=chem).place(x=300, y=200, width=100)
    
    Label(f4, font=('Cambria', 15), text='Enter Maths.', bg='LightBlue', fg='Red').place(x=150, y=250)
    Entry(f4, font=('Cambria', 15), textvariable=maths).place(x=300, y=250, width=100)
    
    def insert_data():
        try:
            db.insert_student(roll_no.get(), name.get(), phy.get(), chem.get(), maths.get())
            messagebox.showinfo('Success', 'Data Inserted')
            
            # Clear fields
            roll_no.set('')
            name.set('')
            phy.set('')
            chem.set('')
            maths.set('')
            
            # Refresh ShowAll tab
            refresh_showall()
        except Exception as e:
            messagebox.showerror('Error', f'Failed to insert data: {str(e)}')
    
    Button(f4, font=('Cambria', 15), text='Insert Data', bg='LightBlue', fg='Red', 
           command=insert_data).place(x=250, y=300, width=120, height=30)

# ==================== ShowAll Tab ====================
def create_showall_tab(ntb):
    """Create the ShowAll students tab"""
    global frame_showall
    f5 = Frame(bg='LightBlue')
    ntb.add(f5, text='ShowAll')
    frame_showall = f5
    
    display_all_students(f5)

def display_all_students(frame):
    """Display all student records in the frame"""
    # Clear existing widgets
    for widget in frame.winfo_children():
        widget.destroy()
    
    # Headers
    headers = ['Roll No.', 'Name', 'Phy.', 'Chem.', 'Maths']
    for i, text in enumerate(headers):
        Label(frame, font=('Arial', 12, 'bold'), text=text, bg='LightBlue', 
              fg='Red').place(x=i * 120, y=0, width=120)
    
    # Fetch and display data
    rows = db.get_all_students()
    y = 50
    for row in rows:
        for i, val in enumerate(row):
            Label(frame, text=val, font=('Arial', 12), bg='LightBlue', 
                  fg='Red').place(x=i * 120, y=y)
        y += 30

def refresh_showall():
    """Refresh the ShowAll tab"""
    global frame_showall
    if frame_showall:
        display_all_students(frame_showall)

# ==================== Search Tab ====================
def create_search_tab(ntb):
    """Create the Search student tab"""
    f6 = Frame(bg='LightBlue')
    ntb.add(f6, text='Search')
    
    roll_no = StringVar()
    
    Label(f6, font=('Arial', 12), text='Roll No.', bg='LightBlue', 
          fg='Red').place(x=100, y=50, width=120)
    Entry(f6, font=('Cambria', 15), textvariable=roll_no).place(x=230, y=50, width=100)
    
    def search_student():
        # Clear previous results
        for widget in f6.winfo_children():
            if widget.winfo_y() >= 100:
                widget.destroy()
        
        result = db.search_student(roll_no.get())
        
        if result:
            labels = ['Name', 'Phy', 'Chem', 'Maths']
            for i, text in enumerate(labels):
                Label(f6, text=f"{text}: {result[i+1]}", font=('Cambria', 15), 
                      bg='LightBlue', fg='Red').place(x=200, y=100 + 50 * i)
        else:
            messagebox.showinfo('Not Found', 'Roll No. not found')
    
    Button(f6, text='Search', font=('Cambria', 15), 
           command=search_student).place(x=350, y=50, width=100, height=30)

# ==================== Update Tab ====================
def create_update_tab(ntb):
    """Create the Update student tab"""
    f7 = Frame(bg='LightBlue')
    ntb.add(f7, text='Update')
    
    roll_no = StringVar()
    
    Label(f7, font=('Arial', 12), text='Roll No.', bg='LightBlue', 
          fg='Red').place(x=100, y=50, width=120)
    Entry(f7, font=('Cambria', 15), textvariable=roll_no).place(x=230, y=50, width=100)
    
    def retrieve_student():
        # Clear previous fields
        for widget in f7.winfo_children():
            if widget.winfo_y() >= 100:
                widget.destroy()
        
        record = db.search_student(roll_no.get())
        
        if not record:
            messagebox.showinfo('Not Found', 'Roll No. not found')
            return
        
        # Create input fields with existing data
        name = StringVar(value=record[1])
        phy = StringVar(value=record[2])
        chem = StringVar(value=record[3])
        maths = StringVar(value=record[4])
        
        fields = [('Name', name), ('Phy', phy), ('Chem', chem), ('Maths', maths)]
        
        for i, (label, var) in enumerate(fields):
            Label(f7, text=f'{label}:', font=('Cambria', 15), bg='LightBlue', 
                  fg='Red').place(x=200, y=100 + 50 * i)
            Entry(f7, font=('Cambria', 15), textvariable=var).place(x=350, y=100 + 50 * i)
        
        def update_data():
            try:
                db.update_student(roll_no.get(), name.get(), phy.get(), chem.get(), maths.get())
                messagebox.showinfo('Success', 'Data Updated')
                refresh_showall()
            except Exception as e:
                messagebox.showerror('Error', f'Failed to update data: {str(e)}')
        
        Button(f7, text='Update', font=('Cambria', 15), 
               command=update_data).place(x=250, y=325, width=120, height=30)
    
    Button(f7, text='Retrieve', font=('Cambria', 15), 
           command=retrieve_student).place(x=350, y=50, width=100, height=30)

# ==================== Delete Tab ====================
def create_delete_tab(ntb):
    """Create the Delete student tab"""
    f8 = Frame(bg='LightBlue')
    ntb.add(f8, text='Delete')
    
    roll_no = StringVar()
    
    Label(f8, font=('Arial', 12), text='Roll No.', bg='LightBlue', 
          fg='Red').place(x=100, y=50, width=120)
    Entry(f8, font=('Cambria', 15), textvariable=roll_no).place(x=230, y=50, width=100)
    
    def delete_student():
        try:
            db.delete_student(roll_no.get())
            messagebox.showinfo('Success', 'Data deleted')
            roll_no.set('')
            refresh_showall()
        except Exception as e:
            messagebox.showerror('Error', f'Failed to delete data: {str(e)}')
    
    Button(f8, text='Delete', font=('Cambria', 15), 
           command=delete_student).place(x=350, y=50, width=100, height=30)

# ==================== Logout Tab ====================
def create_logout_tab(ntb):
    """Create the Logout tab"""
    f9 = Frame(bg='LightBlue')
    ntb.add(f9, text='LogOut')

# ==================== Home Screen ====================
def create_home_screen(root):
    """Create the home/welcome screen"""
    f1 = Frame(bg="#F0F8FF")
    f1.place(x=0, y=0, width=600, height=400)
    
    Label(f1, text='LogiX - Student \nRecords Manager', 
          font=('Cambria', 25, 'bold'), justify = 'center', 
          bg="#F0F8FF", fg= "#9F00FF").pack(pady= 50)
    
    Button(f1, text='Login', font=('Cambria', 15), fg= "White", bg= "#9F00FF",
           command=lambda: create_login_screen(root)).place(x=200, y=200, width=95, height=40)
    Button(f1, text='Register', font=('Cambria', 15), fg= "White", bg= "#9F00FF",
           command=lambda: create_register_screen(root)).place(x=300, y=200, width=100, height=40)

# ==================== Login Screen ====================
def create_login_screen(root):
    """Create the login screen"""
    f2 = Frame(bg="#F0F8FF")
    f2.place(x=0, y=0, width=600, height=400)
    
    username = StringVar()
    password = StringVar()
    
    Label(f2, text='Login', font=('Cambria', 25, 'bold'), justify = CENTER, 
          bg="#F0F8FF", fg= "#9F00FF").place(x=260, y=30)
    
    Label(f2, text='Enter Name:', bg="#F0F8FF", fg="#9F00FF", 
          font=('Cambria', 12)).place(x=100, y=100)
    Entry(f2, bg= "#F1F0EE",font=('Cambria', 12), 
          textvariable=username).place(x=250, y=100, width=250, height= 35)
    
    Label(f2, text='Enter Password:', bg="#F0F8FF", fg="#9F00FF", 
          font=('Cambria', 12)).place(x=100, y=150)
    Entry(f2, bg= "#F1F0EE",font=('Cambria', 12), 
          textvariable=password, show='*').place(x=250, y=150, width=250, height=35)
    
    def perform_login():
        if db.validate_login(username.get(), password.get()):
            create_main_screen(root)
        else:
            messagebox.showerror('Login Failed', 'Invalid username or password')
    
    Button(f2, text='Login', font=('Cambria', 15), fg="White", bg="#9F00FF", justify= CENTER,
           command=perform_login).place(x=250, y=230, width=100, height=35)
    Button(f2, text='Home', font=('Cambria', 15), fg="White", bg="#9F00FF",
           command=lambda: create_home_screen(root)).place(x=25, y=350, width=100, height=35)
    Button(f2, text='Registration', font=('Cambria', 15), fg="White", bg="#9F00FF",
           command=lambda: create_register_screen(root)).place(x=425, y=350, width=150, height=35)

# ==================== Register Screen ====================
def create_register_screen(root):
    """Create the registration screen"""
    f3 = Frame(bg="#F0F8FF")
    f3.place(x=0, y=0, width=600, height=400)
    
    username = StringVar()
    password = StringVar()
    contact = StringVar()
    
    Label(f3, text='Register', font=('Cambria', 25, 'bold'),justify = CENTER, 
        bg="#F0F8FF", fg= "#9F00FF").place(x=245, y=30)
    
    Label(f3, text='Enter Name:', bg="#F0F8FF", fg="#9F00FF").place(x=200, y=100)
    Entry(f3, bg= "#F1F0EE", font=('Cambria', 12), 
          textvariable=username).place(x=320, y=100, width=120)
    
    Label(f3, text='Enter Password:', bg="#F0F8FF", fg="#9F00FF").place(x=200, y=150)
    Entry(f3, bg= "#F1F0EE", font=('Cambria', 12), 
          textvariable=password, show='*').place(x=320, y=150, width=120)
    
    Label(f3, text='Enter CN:', bg="#F0F8FF", fg="#9F00FF").place(x=200, y=200)
    Entry(f3, bg= "#F1F0EE", font=('Cambria', 12), 
          textvariable=contact).place(x=320, y=200, width=120)
    
    def perform_registration():
        try:
            db.register_user(username.get(), password.get(), contact.get())
            messagebox.showinfo('Success', 'User Registered')
            username.set('')
            password.set('')
            contact.set('')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to register: {str(e)}')
    
    Button(f3, text='Register', font=('Cambria', 15),  bg="#9F00FF", fg="White",
           command=perform_registration).place(x=250, y=250, width=120, height=35)
    Button(f3, text='Home', font=('Cambria', 15),  bg="#9F00FF", fg="White",
           command=lambda: create_home_screen(root)).place(x=25, y=350, width=100, height=35)
    Button(f3, text='Login', font=('Cambria', 15),  bg="#9F00FF", fg="White",
           command=lambda: create_login_screen(root)).place(x=480, y=350, width=120, height=35)