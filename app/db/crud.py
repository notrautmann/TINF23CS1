from app.db.db_connection import connect

def create(obj) -> int:
    conn = connect()
    with conn.cursor() as cur:
        data = {key: value for key, value in obj.to_dict().items() if key != "id"}
        column_names = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        values = tuple(data.values())
        query = f"INSERT INTO {obj.table_name} ({column_names}) VALUES ({placeholders}) RETURNING *"
        cur.execute(query, values)
        result = cur.fetchone()
        conn.commit()
    conn.close()
    return result[0]

def read(cls, id):
    conn = connect()
    with conn.cursor() as cur:
        query = f"SELECT * FROM {cls.table_name} WHERE id = %s"
        cur.execute(query, (id,))
        result = cur.fetchone()
    conn.close()
    return result

def update(cls, id, **kwargs):
    conn = connect()
    with conn.cursor() as cur:
        set_clause = ', '.join([f"{key} = %s" for key in kwargs.keys()])
        values = tuple(kwargs.values()) + (id,)
        query = f"UPDATE {cls.table_name} SET {set_clause} WHERE id = %s"
        cur.execute(query, values)
        conn.commit()
    conn.close()

def delete(cls, id):
    conn = connect()
    with conn.cursor() as cur:
        query = f"DELETE FROM {cls.table_name} WHERE id = %s"
        cur.execute(query, (id,))
        conn.commit()
    conn.close()
