import sqlite3

connection = sqlite3.connect("test1.db")

cursor = connection.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS student(
                   name text,
                   age int,
                   class_number int
               )
               """)

for i in range(4):
    name = input("enter a name: ")
    age = int(input("enter an age: "))
    class_number = int(input("enter a number: "))
    cursor.execute("""
                   INSERT INTO student(name, age, class_number)
                   VALUES (?,?,?)
                   """,(name, age, class_number))
    connection.commit()