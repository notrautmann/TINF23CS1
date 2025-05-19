import psycopg
import os
from dotenv import load_dotenv


def main():
    print("Hallo, willkommen zu deinem Python-Programm!")

class PostgresConnection:
    """
    Usage:
        db = PostgresSingleton()
        conn = db.connection

        conn is then a psycopg connection object.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            # load .env once, when first instantiating
            load_dotenv(".env")
            cls._instance = super().__new__(cls)
            cls._instance._init_connection()
        return cls._instance

    def _init_connection(self):
        """Initialize the single psycopg connection."""
        try:
            self._conn = psycopg.connect(
                host=os.getenv("HOST"),
                dbname=os.getenv("DBNAME"),
                user=os.getenv("USER"),
                password=os.getenv("PASSWORDS")
            )
            print("Connected to the PostgreSQL server.")
        except (psycopg.DatabaseError, Exception) as error:
            print(f"Connection error: {error}")
            self._conn = None

    @property
    def connection(self):
        """Return the singleton connection (or None if failed)."""
        return self._conn


if __name__ == "__main__":
    main()
    PostgresConnection.connection
