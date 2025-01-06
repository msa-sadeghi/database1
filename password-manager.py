import sqlite3
import getpass

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


import string
import random
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)
# def generate_strong_password(length = 12):
#     pass

# generate_strong_password()

#TODO   جدول ماشین
# نام
# مدل
# سال ساخت
# رنگ
# همه ماشین های مدل 1400 به بعد را استخراج کنید