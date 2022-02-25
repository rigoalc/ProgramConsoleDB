import sqlite3
def __init__(self, conn, c):
    c.execute("CREATE TABLE IF NOT EXISTS user (name text, age integer)")
    conn.commit()
    
def print_used(conn, c):
    print(" -- Current fruit in db --")
    
    
