"""
Database schema introspection and Python class generation utility.

This script connects to a PostgreSQL database, inspects the 'public' schema
to retrieve table names and their column definitions (names and data types).
It then generates Python class files, one for each table, into a specified
output directory. These classes are structured to represent database records,
including an __init__ method with type-hinted arguments corresponding to
table columns, a `table_name` class attribute, and a `to_dict()` method
for easy serialization.

The generated classes are intended to be used with a generic CRUD operations
layer, facilitating interaction with the database.

Attributes:
    OUTPUT_DIR (str): The directory where generated Python class files will be stored.
"""

import sys
import os

# Allow imports when running script from within the project directory
[sys.path.append(i) for i in ['.', '..']]  #pylint: disable=expression-not-assigned

from app.db.db_connection import connect  # pylint: disable=wrong-import-position

OUTPUT_DIR = "../app/db/records"  # Specify the directory to store the generated files

def get_table_names():
    """
    Retrieves a list of table names from the 'public' schema of the database.

    Connects to the database, queries the information_schema.tables for
    base tables in the 'public' schema.

    Returns:
        list[str]: A list of table names. Returns an empty list if the
                   database connection fails or no tables are found.
    """
    conn = connect()
    if not conn:
        return []
    with conn.cursor() as cur:
        cur.execute("""
            SELECT table_name FROM information_schema.tables
            WHERE table_schema = 'public' AND table_type = 'BASE TABLE';
        """)
        tables = [row[0] for row in cur.fetchall()]
    conn.close()
    return tables

def get_columns_for_table(table_name):
    """
    Retrieves column names and their data types for a specified table.

    Connects to the database and queries information_schema.columns for
    the given table in the 'public' schema.

    Args:
        table_name (str): The name of the table to inspect.

    Returns:
        list[tuple[str, str]]: A list of tuples, where each tuple contains
                                (column_name, data_type). Returns an empty
                                list if the connection fails or an error occurs.
    """
    conn = connect()
    if not conn:
        return []
    with conn.cursor() as cur:
        cur.execute("""
            SELECT column_name, data_type FROM information_schema.columns
            WHERE table_name = %s AND table_schema = 'public';
        """, (table_name,))
        columns = cur.fetchall()
    conn.close()
    return columns

def generate_crud_class(table_name, columns):
    """
    Generates Python code for a class representing a database table.

    The generated class includes:
    - A `table_name` class attribute.
    - An `__init__` method with arguments for each column, type-hinted
      based on PostgreSQL data types, and defaulting to None.
    - A `to_dict()` method to serialize the object's attributes.

    Args:
        table_name (str): The name of the database table.
        columns (list[tuple[str, str]]): A list of (column_name, postgresql_data_type)
                                         tuples for the table.

    Returns:
        str: A string containing the Python code for the generated class.
    """
    # Helper function to map PostgreSQL types to Python types
    def pg_type_to_py(pg_type: str) -> str:
        """
        Maps PostgreSQL data types to Python type hints.

        Args:
            pg_type (str): The PostgreSQL data type string (e.g., 'integer', 'text').

        Returns:
            str: The corresponding Python type hint string (e.g., 'int', 'str').
                 Defaults to 'str' for unrecognized PostgreSQL types.
        """
        mapping = {
            'integer': 'int',
            'bigint': 'int',
            'smallint': 'int',
            'serial': 'int',
            'bigserial': 'int',
            'real': 'float',
            'double precision': 'float',
            'numeric': 'float',
            'boolean': 'bool',
            'text': 'str',
            'varchar': 'str',
            'character varying': 'str',
            'date': 'str',
            'timestamp': 'str',
            'timestamp without time zone': 'str',
            'timestamp with time zone': 'str',
            'json': 'dict',
            'jsonb': 'dict',
        }
        return mapping.get(pg_type, 'str')

    class_name = table_name.capitalize()
    init_args = ', '.join([
        f"{col[0]}: {pg_type_to_py(col[1])} = None" for col in columns
    ])
    assignments = '\n        '.join([f"self.{col[0]} = {col[0]}" for col in columns])
    code = f"""class {class_name}:
    table_name = "{table_name}"

    def __init__(self, {init_args}):
        {assignments}

    def to_dict(self):
        return {{
            {', '.join([f'"{col[0]}": self.{col[0]}' for col in columns])}
        }}
"""
    return code

def main():
    """
    Main execution function for this script.
    """
    # Ensure the output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    tables = get_table_names()
    for table in tables:
        columns = get_columns_for_table(table)
        crud_code = generate_crud_class(table, columns)
        file_path = os.path.join(OUTPUT_DIR, f"{table}.py")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(crud_code)
    print(f"CRUD classes have been written to `{OUTPUT_DIR}`.")

if __name__ == "__main__":
    main()
