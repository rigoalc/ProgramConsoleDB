import sqlite3
class Signup:
    def __init__(self):
        self.conn = sqlite3.connect('my_data.db')
        self.c = self.conn.cursor()
    def setup(self):
        # Fix this CREATE TABLE statement
        self.c.execute("CREATE TABLE userage (age integer, name text)")
        self.conn.commit()
    def show(self):
        for row in self.c.execute("SELECT age FROM user"): 
            print (row)
    def add_user(self, name, age):
        self.c.execute("INSERT INTO userid VALUES('age', 'name')")
    def close(self):
        self.c.close()
    
v = Signup()
v.setup()
v.add_user("Ron", 78)
print("All:")
v.show_all()
v.close()

    
