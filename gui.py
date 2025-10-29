from tkinter import *
from tkinter import messagebox, ttk
import sqlite3

root = Tk()
root.geometry('600x400')
root.resizable(0, 0)
root.title('Home Page')

frame55 = None


def screen():
    ntb = ttk.Notebook(root)

    def demo(event):
        if ntb.index('current') == 5:
            home()

    ntb.bind('<<NotebookTabChanged>>', demo)
    ntb.place(x=0, y=0, width=600, height=400)

    bginsertion(ntb)
    showall(ntb)
    search(ntb)
    update(ntb)
    delete(ntb)
    logout(ntb)


def bginsertion(ntb):
    f4 = Frame(bg='LightBlue')
    ntb.add(f4, text='Insert')

    m = StringVar()
    n = StringVar()
    o = StringVar()
    p = StringVar()
    q = StringVar()

    Label(f4, font=('Calibri', 15), text='Enter Roll No.', bg='LightBlue', fg='Red').place(x=150, y=50)
    Entry(f4, font=('Calibri', 15), textvariable=m).place(x=300, y=50, width=100)

    Label(f4, font=('Calibri', 15), text='Enter Name', bg='LightBlue', fg='Red').place(x=150, y=100)
    Entry(f4, font=('Calibri', 15), textvariable=n).place(x=300, y=100, width=100)

    Label(f4, font=('Calibri', 15), text='Enter Phy.', bg='LightBlue', fg='Red').place(x=150, y=150)
    Entry(f4, font=('Calibri', 15), textvariable=o).place(x=300, y=150, width=100)

    Label(f4, font=('Calibri', 15), text='Enter Chem.', bg='LightBlue', fg='Red').place(x=150, y=200)
    Entry(f4, font=('Calibri', 15), textvariable=p).place(x=300, y=200, width=100)

    Label(f4, font=('Calibri', 15), text='Enter Maths.', bg='LightBlue', fg='Red').place(x=150, y=250)
    Entry(f4, font=('Calibri', 15), textvariable=q).place(x=300, y=250, width=100)

    def datainsertion():
        conn = sqlite3.connect('demo.db')
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS ins (
                URNO TEXT PRIMARY KEY,
                UNAME TEXT,
                UPHY TEXT,
                UCHE TEXT,
                UMATHS TEXT
            )
        """)
        cur.execute("INSERT INTO ins VALUES (?, ?, ?, ?, ?)", (m.get(), n.get(), o.get(), p.get(), q.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo('Title', 'Data Inserted')
        m.set('')
        n.set('')
        o.set('')
        p.set('')
        q.set('')
        showalldata(frame55)

    Button(f4, font=('Calibri', 15), text='Insert Data', bg='LightBlue', fg='Red', command=datainsertion).place(
        x=250, y=300, width=120, height=30
    )


def showall(ntb):
    f5 = Frame(bg='LightBlue')
    ntb.add(f5, text='ShowAll')
    global frame55
    frame55 = f5
    showalldata(f5)


def showalldata(f5):
    for widget in f5.winfo_children():
        widget.destroy()

    headers = ['Roll No.', 'Name', 'Phy.', 'Chem.', 'Maths']
    for i, text in enumerate(headers):
        Label(f5, font=('Arial', 12), text=text, bg='LightBlue', fg='Red').place(x=i * 120, y=0, width=120)

    conn = sqlite3.connect('demo.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ins (URNO TEXT PRIMARY KEY, UNAME TEXT, UPHY TEXT, UCHE TEXT, UMATHS TEXT)")
    cur.execute("SELECT * FROM ins")
    rows = cur.fetchall()
    conn.close()

    y = 50
    for row in rows:
        for i, val in enumerate(row):
            Label(f5, text=val, font=('Arial', 12), bg='LightBlue', fg='Red').place(x=i * 120, y=y)
        y += 30


def search(ntb):
    f6 = Frame(bg='LightBlue')
    ntb.add(f6, text='Search')

    s1 = StringVar()

    Label(f6, font=('Arial', 12), text='Roll No.', bg='LightBlue', fg='Red').place(x=100, y=50, width=120)
    Entry(f6, font=('Calibri', 15), textvariable=s1).place(x=230, y=50, width=100)

    def searched():
        conn = sqlite3.connect('demo.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM ins WHERE URNO=?", (s1.get(),))
        result = cur.fetchone()
        conn.close()

        if result:
            labels = ['Name', 'Phy', 'Chem', 'Maths']
            for i, text in enumerate(labels):
                Label(f6, text=f"{text}: {result[i+1]}", font=('Calibri', 15), bg='LightBlue', fg='Red').place(
                    x=200, y=100 + 50 * i
                )
        else:
            messagebox.showinfo('Title', 'Roll No. not found')

    Button(f6, text='Search', font=('Calibri', 15), command=searched).place(x=350, y=50, width=100, height=30)


def update(ntb):
    f7 = Frame(bg='LightBlue')
    ntb.add(f7, text='Update')

    s2 = StringVar()

    Label(f7, font=('Arial', 12), text='Roll No.', bg='LightBlue', fg='Red').place(x=100, y=50, width=120)
    Entry(f7, font=('Calibri', 15), textvariable=s2).place(x=230, y=50, width=100)

    def updated():
        conn = sqlite3.connect('demo.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM ins WHERE URNO=?", (s2.get(),))
        record = cur.fetchone()
        conn.close()

        if not record:
            messagebox.showinfo('Title', 'Roll No. not found')
            return

        s3, s4, s5, s6 = StringVar(value=record[1]), StringVar(value=record[2]), StringVar(value=record[3]), StringVar(value=record[4])

        fields = [('Name', s3), ('Phy', s4), ('Chem', s5), ('Maths', s6)]
        for i, (label, var) in enumerate(fields):
            Label(f7, text=f'{label}:', font=('Calibri', 15), bg='LightBlue', fg='Red').place(x=200, y=100 + 50 * i)
            Entry(f7, font=('Calibri', 15), textvariable=var).place(x=350, y=100 + 50 * i)

        def updatedata2():
            conn = sqlite3.connect('demo.db')
            cur = conn.cursor()
            cur.execute("""
                UPDATE ins SET UNAME=?, UPHY=?, UCHE=?, UMATHS=? WHERE URNO=?
            """, (s3.get(), s4.get(), s5.get(), s6.get(), s2.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo('Title', 'Data Updated')
            showalldata(frame55)

        Button(f7, text='Update', font=('Calibri', 15), command=updatedata2).place(x=250, y=325, width=120, height=30)

    Button(f7, text='Retrieve', font=('Calibri', 15), command=updated).place(x=350, y=50, width=100, height=30)


def delete(ntb):
    f8 = Frame(bg='LightBlue')
    ntb.add(f8, text='Delete')

    s1 = StringVar()

    Label(f8, font=('Arial', 12), text='Roll No.', bg='LightBlue', fg='Red').place(x=100, y=50, width=120)
    Entry(f8, font=('Calibri', 15), textvariable=s1).place(x=230, y=50, width=100)

    def deletion():
        conn = sqlite3.connect('demo.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM ins WHERE URNO=?", (s1.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo('Title', 'Data deleted')
        showalldata(frame55)
        s1.set('')

    Button(f8, text='Delete', font=('Calibri', 15), command=deletion).place(x=350, y=50, width=100, height=30)


def logout(ntb):
    f9 = Frame(bg='LightBlue')
    ntb.add(f9, text='LogOut')


def home():
    f1 = Frame(bg='LightBlue')
    f1.place(x=0, y=0, width=600, height=400)

    Button(f1, text='Login', font=('Calibri', 15), command=login).place(x=220, y=100, width=100, height=30)
    Button(f1, text='Register', font=('Calibri', 15), command=regis).place(x=330, y=100, width=100, height=30)


def login():
    f2 = Frame(bg='LightBlue')
    f2.place(x=0, y=0, width=600, height=400)

    d = StringVar()
    e = StringVar()

    Label(f2, text='Enter Name:', bg='LightBlue', fg='Red').place(x=200, y=100)
    Entry(f2, font=('Calibri', 15), textvariable=d).place(x=320, y=100, width=120)

    Label(f2, text='Enter Password:', bg='LightBlue', fg='Red').place(x=200, y=150)
    Entry(f2, font=('Calibri', 15), textvariable=e, show='*').place(x=320, y=150, width=120)

    def login1():
        conn = sqlite3.connect('demo.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS regis (UNAME TEXT, UPASS TEXT, CN TEXT)")
        cur.execute("SELECT * FROM regis WHERE UNAME=? AND UPASS=?", (d.get(), e.get()))
        result = cur.fetchone()
        conn.close()
        if result:
            screen()
        else:
            messagebox.showinfo('Title', 'Invalid username or password')

    Button(f2, text='Login', font=('Calibri', 15), command=login1).place(x=250, y=200, width=100, height=30)
    Button(f2, text='Home', font=('Calibri', 15), command=home).place(x=20, y=350, width=100, height=30)
    Button(f2, text='Registration', font=('Calibri', 15), command=regis).place(x=480, y=350, width=120, height=30)


def regis():
    f3 = Frame(bg='LightBlue')
    f3.place(x=0, y=0, width=600, height=400)

    a = StringVar()
    b = StringVar()
    c = StringVar()

    Label(f3, text='Enter Name:', bg='LightBlue', fg='Red').place(x=200, y=100)
    Entry(f3, font=('Calibri', 15), textvariable=a).place(x=320, y=100, width=120)

    Label(f3, text='Enter Password:', bg='LightBlue', fg='Red').place(x=200, y=150)
    Entry(f3, font=('Calibri', 15), textvariable=b, show='*').place(x=320, y=150, width=120)

    Label(f3, text='Enter CN:', bg='LightBlue', fg='Red').place(x=200, y=200)
    Entry(f3, font=('Calibri', 15), textvariable=c).place(x=320, y=200, width=120)

    def registring():
        conn = sqlite3.connect('demo.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS regis (UNAME TEXT, UPASS TEXT, CN TEXT)")
        cur.execute("INSERT INTO regis VALUES (?, ?, ?)", (a.get(), b.get(), c.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo('Title', 'User Registered')
        a.set('')
        b.set('')
        c.set('')

    Button(f3, text='Register', font=('Calibri', 15), command=registring).place(x=250, y=250, width=120, height=30)
    Button(f3, text='Home', font=('Calibri', 15), command=home).place(x=20, y=350, width=100, height=30)
    Button(f3, text='Login', font=('Calibri', 15), command=login).place(x=480, y=350, width=120, height=30)


# Start application
home()
root.mainloop()
