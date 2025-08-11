import psycopg2
from psycopg2.extras import RealDictCursor
class Database:
    def __init__(self, host='localhost', dbname='SchoolManagement',
                  user='postgres', password='root', port=5432):
        self.conn = psycopg2.connect(
            host = host,
            database = dbname,
            user = user,
            password = password,
            port = port
        )
        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)
    def execute(self, query, params=None):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetchall(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def fetchone(self, query, params = None):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()

d = Database()
# d.execute('INSERT INTO classes VALUES(DEFAULT, %s, %s, %s)', ('dovom', 2020, 'this is class dovaom'))
print(d.fetchone('select * from classes where name=%s', ('aval',)))
