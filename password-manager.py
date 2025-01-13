import sqlite3
import getpass
import string
import random
import secrets
from cryptography.fernet import Fernet



# enc_key = Fernet.generate_key()
enc_key = b'T2fk_JJX_JcHKaHAkdC0vKwDmjThCJ-6hWV1rr005fQ='
f = Fernet(enc_key)



conn = sqlite3.connect('password_manager.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS password(
    id integer,
    website text,
    username text,
    password text
)
               ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS user(
    id integer,
    username text,
    password text
)
               ''')

def register_user():
    id = int(input("enter your id: "))
    username = input("enter your username: ")
    password = getpass.getpass("enter your password: ")
    encr_pass = f.encrypt(password.encode()).decode()
    cursor.execute("""INSERT INTO user(id,username, password) VALUES (?,?,?)
                   """,(id,username, encr_pass))
    
    conn.commit()


def login():
    global username
    username = input("enter your username: ")
    password = getpass.getpass("enter your password: ")
    cursor.execute('''SELECT * FROM user WHERE username=? 
                   ''', (username,))
    user = cursor.fetchone()
    if user:
        decrypted_password = f.decrypt(user[2].encode()).decode()
        if password  == decrypted_password:
            print("Login Success") 
            return True
    
    print("Login Failed!")  
    return False 



def generate_strong_password(length = 12):
    pool = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(pool) for _ in range(length))
    return password
    


def change_password():
    if not login():
        return 
    new_password = getpass.getpass("enter the new password: ")
    if not new_password:
        new_password = generate_strong_password()
        print(f"new strong password is {new_password}")
        
    encrypted_pass = f.encrypt(new_password.encode()).decode()
    cursor.execute("""
                   UPDATE user SET password=? WHERE username=?
                   """, (encrypted_pass, username))
    conn.commit()
    print("your password changed  successfully")
    
        
change_password()       
    