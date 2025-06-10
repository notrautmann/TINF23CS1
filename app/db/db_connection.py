"""Provides a singleton PostgreSQL database connection.

This module ensures that only one connection to the PostgreSQL database is
established throughout the application's lifecycle. It retrieves database
credentials from environment variables.
"""

import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

class DbConnection:
    """A singleton class to manage the PostgreSQL database connection."""
    _instance = None

    @staticmethod
    def get_instance():
        """Gets the singleton database connection instance.

        If an instance doesn't exist or the existing connection is closed,
        it creates a new connection.

        Returns:
            psycopg.Connection: The active database connection instance.
        """
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
    """Connect to the PostgreSQL database server.

    A convenience function to get the singleton database connection instance.

    Returns:
        psycopg.Connection: The active database connection instance.
    """
    return DbConnection.get_instance()
