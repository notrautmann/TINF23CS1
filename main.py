import psycopg
import psycopg_binary


def main():
    print("Hallo, willkommen zu deinem Python-Programm!")

def connect():
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg.connect(
                    host="ep-bold-mountain-a2qeaem7-pooler.eu-central-1.aws.neon.tech",
                    dbname="TINF_ERP",
                    user="business_logic",
                    password="npg_K7wOZFcHWo1N"
            ) as conn:              
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg.DatabaseError, Exception) as error:
        print(error)


if __name__ == "__main__":
    main()
    connect()