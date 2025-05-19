import psycopg

from main import connect

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
    # Hilfsfunktion zur Typzuordnung
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
    # Typannotationen für __init__ und create
    init_args = ', '.join([
        f"{col[0]}: {pg_type_to_py(col[1])} = None" for col in columns
    ])
    fields = ', '.join([col[0] for col in columns])
    create_args = ', '.join([
        f"{col[0]}: {pg_type_to_py(col[1])}" for col in columns
    ])
    assignments = '\n        '.join([f"self.{col[0]} = {col[0]}" for col in columns])
    code = f"""
class {class_name}:
    def __init__(self, {init_args}):
        {assignments}

    @staticmethod
    def create({create_args}) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute(\"INSERT INTO {table_name} ({fields}) VALUES ({', '.join(['%s']*len(columns))}) RETURNING *\", ({fields},))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute(\"SELECT * FROM {table_name} WHERE id = %s\", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{{k}} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f\"UPDATE {table_name} SET {{set_clause}} WHERE id = %s\", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute(\"DELETE FROM {table_name} WHERE id = %s\", (id,))
            conn.commit()
        conn.close()
"""
    return code

def main():
    tables = get_table_names()
    all_code = [
        "import psycopg\n\nfrom main import connect\n"
    ]
    for table in tables:
        columns = get_columns_for_table(table)
        crud_code = generate_crud_class(table, columns)
        all_code.append(crud_code)
    with open("db.py", "w", encoding="utf-8") as f:
        f.write("\n".join(all_code))
    print("CRUD-Klassen wurden in db.py geschrieben.")

if __name__ == "__main__":
    main()

