import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

class DBConnection:
    _instance = None

    @staticmethod
    def get_instance():
        if DBConnection._instance is None or DBConnection._instance.closed:
            DBConnection._instance = psycopg.connect(
                host=os.getenv("HOST"),
                dbname=os.getenv("DBNAME"),
                user=os.getenv("USER"),
                password=os.getenv("PASSWORD")
            )
            print('Connected to the PostgreSQL server.')
        return DBConnection._instance

def main():
    print("Hallo, willkommen zu deinem Python-Programm!")

def connect():
    """ Connect to the PostgreSQL database server """
    return DBConnection.get_instance()

if __name__ == "__main__":
    main()
    connect()
