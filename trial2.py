from tkinter import *
from tkinter import messagebox, ttk
import sqlite3

myroot = Tk()
myroot.geometry('600x400')
myroot.resizable(0, 0)
myroot.title('Home Page')

myframe55 = None


def myscreen():
    myntb = ttk.Notebook(myroot)

    def mydemo(event):
        if myntb.index('current') == 5:
            myhome()

    myntb.bind('<<NotebookTabChanged>>', mydemo)
    myntb.place(x=0, y=0, width=600, height=400)

    bginsertion(myntb)
    myshowall(myntb)
    mysearch(myntb)
    myupdate(myntb)
    mydelete(myntb)
    mylogout(myntb)


def bginsertion(ntb):
    myf4 = Frame(bg='LightBlue')
    ntb.add(myf4, text='MyInsert')

    m = StringVar()
    n = StringVar()
    o = StringVar()
    p = StringVar()
    q = StringVar()

    Label(myf4, font=('Calibri', 15), text='Enter Roll No.', bg='LightBlue', fg='Red').place(x=150, y=50)
    Entry(myf4, font=('Calibri', 15), textvariable=m).place(x=300, y=50, width=100)

    Label(myf4, font=('Calibri', 15), text='Enter Name', bg='LightBlue', fg='Red').place(x=150, y=100)
    Entry(myf4, font=('Calibri', 15), textvariable=n).place(x=300, y=100, width=100)

    Label(myf4, font=('Calibri', 15), text='Enter Phy.', bg='LightBlue', fg='Red').place(x=150, y=150)
    Entry(myf4, font=('Calibri', 15), textvariable=o).place(x=300, y=150, width=100)

    Label(myf4, font=('Calibri', 15), text='Enter Chem.', bg='LightBlue', fg='Red').place(x=150, y=200)
    Entry(myf4, font=('Calibri', 15), textvariable=p).place(x=300, y=200, width=100)

    Label(myf4, font=('Calibri', 15), text='Enter Maths.', bg='LightBlue', fg='Red').place(x=150, y=250)
    Entry(myf4, font=('Calibri', 15), textvariable=q).place(x=300, y=250, width=100)

    def mydatainsertion():
        conn = sqlite3.connect('mydemo.db')
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
        myshowalldata(myframe55)

    Button(myf4, font=('Calibri', 15), text='Insert Data', bg='LightBlue', fg='Red', command=mydatainsertion).place(
        x=250, y=300, width=120, height=30
    )


def myshowall(ntb):
    myf5 = Frame(bg='LightBlue')
    ntb.add(myf5, text='MyShowAll')
    global myframe55
    myframe55 = myf5
    myshowalldata(myf5)


def myshowalldata(myf5):
    for widget in myf5.winfo_children():
        widget.destroy()

    headers = ['Roll No.', 'Name', 'Phy.', 'Chem.', 'Maths']
    for i, text in enumerate(headers):
        Label(myf5, font=('Arial', 12), text=text, bg='LightBlue', fg='Red').place(x=i * 120, y=0, width=120)

    conn = sqlite3.connect('mydemo.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ins (URNO TEXT PRIMARY KEY, UNAME TEXT, UPHY TEXT, UCHE TEXT, UMATHS TEXT)")
    cur.execute("SELECT * FROM ins")
    rows = cur.fetchall()
    conn.close()

    y = 50
    for row in rows:
        for i, val in enumerate(row):
            Label(myf5, text=val, font=('Arial', 12), bg='LightBlue', fg='Red').place(x=i * 120, y=y)
        y += 30


def mysearch(ntb):
    myf6 = Frame(bg='LightBlue')
    ntb.add(myf6, text='MySearch')

    s1 = StringVar()

    Label(myf6, font=('Arial', 12), text='Roll No.', bg='LightBlue', fg='Red').place(x=100, y=50, width=120)
    Entry(myf6, font=('Calibri', 15), textvariable=s1).place(x=230, y=50, width=100)

    def searched():
        conn = sqlite3.connect('mydemo.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM ins WHERE URNO=?", (s1.get(),))
        result = cur.fetchone()
        conn.close()

        if result:
            labels = ['Name', 'Phy', 'Chem', 'Maths']
            for i, text in enumerate(labels):
                Label(myf6, text=f"{text}: {result[i+1]}", font=('Calibri', 15), bg='LightBlue', fg='Red').place(
                    x=200, y=100 + 50 * i
                )
        else:
            messagebox.showinfo('Title', 'Roll No. not found')

    Button(myf6, text='Search', font=('Calibri', 15), command=searched).place(x=350, y=50, width=100, height=30)


def myupdate(ntb):
    myf7 = Frame(bg='LightBlue')
    ntb.add(myf7, text='MyUpdate')

    s2 = StringVar()

    Label(myf7, font=('Arial', 12), text='Roll No.', bg='LightBlue', fg='Red').place(x=100, y=50, width=120)
    Entry(myf7, font=('Calibri', 15), textvariable=s2).place(x=230, y=50, width=100)

    def updated():
        conn = sqlite3.connect('mydemo.db')
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
            Label(myf7, text=f'{label}:', font=('Calibri', 15), bg='LightBlue', fg='Red').place(x=200, y=100 + 50 * i)
            Entry(myf7, font=('Calibri', 15), textvariable=var).place(x=350, y=100 + 50 * i)

        def updatedata2():
            conn = sqlite3.connect('mydemo.db')
            cur = conn.cursor()
            cur.execute("""
                UPDATE ins SET UNAME=?, UPHY=?, UCHE=?, UMATHS=? WHERE URNO=?
            """, (s3.get(), s4.get(), s5.get(), s6.get(), s2.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo('Title', 'Data Updated')
            myshowalldata(myframe55)

        Button(myf7, text='Update', font=('Calibri', 15), command=updatedata2).place(x=250, y=325, width=120, height=30)

    Button(myf7, text='Retrieve', font=('Calibri', 15), command=updated).place(x=350, y=50, width=100, height=30)


def mydelete(ntb):
    myf8 = Frame(bg='LightBlue')
    ntb.add(myf8, text='MyDelete')

    s1 = StringVar()

    Label(myf8, font=('Arial', 12), text='Roll No.', bg='LightBlue', fg='Red').place(x=100, y=50, width=120)
    Entry(myf8, font=('Calibri', 15), textvariable=s1).place(x=230, y=50, width=100)

    def mydeletion():
        conn = sqlite3.connect('mydemo.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM ins WHERE URNO=?", (s1.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo('Title', 'Data deleted')
        myshowalldata(myframe55)
        s1.set('')

    Button(myf8, text='Delete', font=('Calibri', 15), command=mydeletion).place(x=350, y=50, width=100, height=30)


def mylogout(ntb):
    myf9 = Frame(bg='LightBlue')
    ntb.add(myf9, text='MyLogOut')


def myhome():
    myf1 = Frame(bg='LightBlue')
    myf1.place(x=0, y=0, width=600, height=400)

    Button(myf1, text='Login', font=('Calibri', 15), command=mylogin).place(x=220, y=100, width=100, height=30)
    Button(myf1, text='Register', font=('Calibri', 15), command=myregis).place(x=330, y=100, width=100, height=30)


def mylogin():
    myf2 = Frame(bg='LightBlue')
    myf2.place(x=0, y=0, width=600, height=400)

    d = StringVar()
    e = StringVar()

    Label(myf2, text='Enter Name:', bg='LightBlue', fg='Red').place(x=200, y=100)
    Entry(myf2, font=('Calibri', 15), textvariable=d).place(x=320, y=100, width=120)

    Label(myf2, text='Enter Password:', bg='LightBlue', fg='Red').place(x=200, y=150)
    Entry(myf2, font=('Calibri', 15), textvariable=e, show='*').place(x=320, y=150, width=120)

    def login1():
        conn = sqlite3.connect('mydemo.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS regis (UNAME TEXT, UPASS TEXT, CN TEXT)")
        cur.execute("SELECT * FROM regis WHERE UNAME=? AND UPASS=?", (d.get(), e.get()))
        result = cur.fetchone()
        conn.close()
        if result:
            myscreen()
        else:
            messagebox.showinfo('Title', 'Invalid username or password')

    Button(myf2, text='Login', font=('Calibri', 15), command=login1).place(x=250, y=200, width=100, height=30)
    Button(myf2, text='Home', font=('Calibri', 15), command=myhome).place(x=20, y=350, width=100, height=30)
    Button(myf2, text='Registration', font=('Calibri', 15), command=myregis).place(x=480, y=350, width=120, height=30)


def myregis():
    myf3 = Frame(bg='LightBlue')
    myf3.place(x=0, y=0, width=600, height=400)

    a = StringVar()
    b = StringVar()
    c = StringVar()

    Label(myf3, text='Enter Name:', bg='LightBlue', fg='Red').place(x=200, y=100)
    Entry(myf3, font=('Calibri', 15), textvariable=a).place(x=320, y=100, width=120)

    Label(myf3, text='Enter Password:', bg='LightBlue', fg='Red').place(x=200, y=150)
    Entry(myf3, font=('Calibri', 15), textvariable=b, show='*').place(x=320, y=150, width=120)

    Label(myf3, text='Enter CN:', bg='LightBlue', fg='Red').place(x=200, y=200)
    Entry(myf3, font=('Calibri', 15), textvariable=c).place(x=320, y=200, width=120)

    def registring():
        conn = sqlite3.connect('mydemo.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS regis (UNAME TEXT, UPASS TEXT, CN TEXT)")
        cur.execute("INSERT INTO regis VALUES (?, ?, ?)", (a.get(), b.get(), c.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo('Title', 'User Registered')
        a.set('')
        b.set('')
        c.set('')

    Button(myf3, text='Register', font=('Calibri', 15), command=registring).place(x=250, y=250, width=120, height=30)
    Button(myf3, text='Home', font=('Calibri', 15), command=myhome).place(x=20, y=350, width=100, height=30)
    Button(myf3, text='Login', font=('Calibri', 15), command=mylogin).place(x=480, y=350, width=120, height=30)


# Start application
myhome()
myroot.mainloop()
