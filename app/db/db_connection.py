import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

class DbConnection:
    _instance = None

    @staticmethod
    def get_instance():
        if DbConnection._instance is None or DbConnection._instance.closed:
            DbConnection._instance = psycopg.connect(
                host=os.getenv("DB_HOST"),
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD")
            )
            print('Connected to the PostgreSQL server.')
        return DbConnection._instance

def connect():
    """ Connect to the PostgreSQL database server """
    return DbConnection.get_instance()
