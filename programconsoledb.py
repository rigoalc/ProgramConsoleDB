import sqlite3

def create_tables(conn, c):
    c.execute("CREATE TABLE IF NOT EXISTS fruit (name text, quantity integer)")

    c.execute("INSERT INTO fruit VALUES ('Apple', 0), ('Orange', 0)")
    conn.commit()
    
