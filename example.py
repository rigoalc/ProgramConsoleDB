import sqlite3
class Vegetables:
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()
    def setup(self):
        # Fix this CREATE TABLE statement
        self.c.execute("CREATE TABLE vegetable (quantity integer, name text)")
        self.conn.commit()
    def show_all(self):
        # Fix this SELECT statement
        for row in self.c.execute("SELECT * FROM vegetable"):
            print(row)
    def add_vegetable(self, name, quantity):
        # Fix this statement
        self.c.execute("INSERT INTO vegetable VALUES (?, ?)", [quantity, name])
    def find_vegetable(self, name):
        # Fix this SELECT statement
        self.c.execute("SELECT * FROM vegetable")
        row = self.c.fetchone() # Get first row
        return row
    def close(self):
        self.conn.close()

v = Vegetables()
v.setup()
print("Carrot:", v.find_vegetable("Carrot"))
v.add_vegetable("Carrot", 42)
print("Carrot:", v.find_vegetable("Carrot"))
v.add_vegetable("Broccoli", 1)
v.add_vegetable("Zucchini", 0)
print("All:")
v.show_all()
v.close()