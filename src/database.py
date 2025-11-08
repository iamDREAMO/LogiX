"""
LogiX Database Module
Handles SQLite3 database setup and queries
"""
import sqlite3

DB_NAME = 'demo.db'

# ==================== Table Setup ====================
def create_tables():
    """Create necessary tables if they don't exist"""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    
    # Students table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll_no TEXT PRIMARY KEY,
            name TEXT,
            phys TEXT,
            chem TEXT,
            maths TEXT
        )
    """)
    
    # Users/Registration table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT,
            password TEXT
        )
    """)
    
    conn.commit()
    conn.close()

# ==================== Student Operations ====================
def insert_student(roll_no, name, phys, chem, maths):
    """Insert a new student record"""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    
    create_tables()
    cur.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", 
                (roll_no, name, phys, chem, maths))
    
    conn.commit()
    conn.close()
    return True

def get_all_students():
    """Retrieve all student records"""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    
    create_tables()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    
    conn.close()
    return rows

def search_student(roll_no):
    """Search for a student by roll number"""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM students WHERE roll_no=?", (roll_no,))
    result = cur.fetchone()
    
    conn.close()
    return result

def update_student(roll_no, name, phys, chem, maths):
    """Update student information"""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    
    cur.execute("""
        UPDATE students SET name=?, phys=?, chem=?, maths=? WHERE roll_no=?
    """, (name, phys, chem, maths, roll_no))
    
    conn.commit()
    conn.close()
    return True

def delete_student(roll_no):
    """Delete a student record"""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    
    cur.execute("DELETE FROM students WHERE roll_no=?", (roll_no,))
    
    conn.commit()
    conn.close()
    return True

# ==================== User Authentication ====================
def register_user(username, password):
    """Register a new user"""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    
    create_tables()
    cur.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    
    conn.commit()
    conn.close()
    return True

def validate_login(username, password):
    """Validate user login credentials"""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    
    create_tables()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cur.fetchone()
    
    conn.close()
    return result is not None