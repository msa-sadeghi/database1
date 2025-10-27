import psycopg2
from psycopg2 import pool
from config import DB_CONFIG

class DatabaseManager:
    _instance = None
    _connection_pool = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def initialize_pool(self):
        try:
            self._connection_pool = psycopg2.pool.SimpleConnectionPool(
                minconn = 1, maxconn = 10, **DB_CONFIG
            )
            print("Connection pool created successfully")
        except:
            print("error in creating connection pool")