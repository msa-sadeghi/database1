import sqlite3
def select_all():
    query = "SELECT * FROM student"
    cursor.execute(query)
    for student in cursor.fetchall():
        print(student)
    conn.commit()

def insert_into_table(**kwargs):
    # TODO insert new student
    pass

try:
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    # select_all()
    insert_into_table(id=5, name= "sadra", family="vali", email="s@gmail.com")
    
except sqlite3.Error as e:
    print(f"error{e}")
    
