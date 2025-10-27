import sqlite3

def connect_db():
    conn = sqlite3.connect("logix.db")
    return conn

def setup_tables():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        cn TEXT
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        roll_no TEXT PRIMARY KEY,
        name TEXT,
        phy REAL,
        chem REAL,
        maths REAL
    )
    """)
    
    conn.commit()
    conn.close()

def insert_user(username, password, cn):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (username, password, cn))
    conn.commit()
    conn.close()

def validate_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()
    return result

def insert_student(roll_no, name, phy, chem, maths):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", (roll_no, name, phy, chem, maths))
    conn.commit()
    conn.close()

def get_all_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_student(roll_no):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE roll_no=?", (roll_no,))
    result = cursor.fetchone()
    conn.close()
    return result

def update_student(roll_no, name, phy, chem, maths):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students SET name=?, phy=?, chem=?, maths=? WHERE roll_no=?
    """, (name, phy, chem, maths, roll_no))
    conn.commit()
    conn.close()

def delete_student(roll_no):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE roll_no=?", (roll_no,))
    conn.commit()
    conn.close()
