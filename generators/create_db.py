import sys
import os

# Allow imports when running script from within the project directory
[sys.path.append(i) for i in ['.', '..']]

from app.db.db_connection import connect

OUTPUT_DIR = "../app/db/records"  # Specify the directory to store the generated files

def get_table_names():
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
    # Helper function to map PostgreSQL types to Python types
    def pg_type_to_py(pg_type: str) -> str:
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