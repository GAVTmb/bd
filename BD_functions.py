import psycopg2

# Функция, создающая структуру БД (таблицы)!
def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
                DROP TABLE Phone_number;
                DROP TABLE Client;
            """)
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS Client(
                        id SERIAL PRIMARY KEY,
                        first_name VARCHAR(30) NOT NULL,
                        last_name VARCHAR(30) NOT NULL,
                        email VARCHAR(60) NOT NULL UNIQUE
                        );
            """)
        conn.commit()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS Phone_number(
                        id SERIAL PRIMARY KEY,
                        phone_number VARCHAR(10),
                        Client_id INTEGER REFERENCES Client(id)
                        );
            """)
        conn.commit()

# Функция, позволяющая добавить нового клиента!
def add_client(conn, first_name, last_name, email, phone_number=None):
    with conn.cursor() as cur:
        execute_client = f"INSERT INTO Client(first_name, last_name, email)" \
                        f" VALUES('{first_name}', '{last_name}', '{email}');"
        cur.execute(execute_client)
        conn.commit()
        cur.execute("""SELECT id FROM Client WHERE email=%s;""", (f'{email}',))
        client_id = cur.fetchone()[0]
        insert_phone = f"INSERT INTO Phone_number(phone_number, Client_id) VALUES('{phone_number}', {client_id});"
        cur.execute(insert_phone)
        conn.commit()
        with conn.cursor() as cur:
            cur.execute("""SELECT * FROM Client;""")
            print(cur.fetchall())
            cur.execute("""SELECT * FROM Phone_number;""")
            print(cur.fetchall())

# Функция, позволяющая добавить телефон для существующего клиента!
def add_phone(conn, client_id, phone_number):
    with conn.cursor() as cur:
        insert_phone = f"INSERT INTO Phone_number(phone_number, Client_id) VALUES('{phone_number}', {client_id});"
        cur.execute(insert_phone)
        conn.commit()
        with conn.cursor() as cur:
            cur.execute("""SELECT * FROM Client;""")
            print(cur.fetchall())
            cur.execute("""SELECT * FROM Phone_number;""")
            print(cur.fetchall())

# Функция, позволяющая изменить данные о клиенте!
def change_client(conn, client_id, first_name=None, last_name=None, email=None, phone_number=None):
    pass

# Функция, позволяющая удалить телефон для существующего клиента!
def delete_phone(conn, client_id, phone_number):
    with conn.cursor() as cur:
        delete_phone = f"DELETE FROM Phone_number WHERE phone_number = '{phone_number}';"
        cur.execute(delete_phone)
        conn.commit()
        with conn.cursor() as cur:
            cur.execute("""SELECT * FROM Client;""")
            print(cur.fetchall())
            cur.execute("""SELECT * FROM Phone_number;""")
            print(cur.fetchall())


# Функция, позволяющая удалить существующего клиента
def delete_client(conn, client_id):
    with conn.cursor() as cur:
        delete_phone = f"DELETE FROM Phone_number WHERE Client_id = {client_id};"
        cur.execute(delete_phone)
        conn.commit()
        delete_client = f"DELETE FROM Client WHERE id = {client_id};"
        cur.execute(delete_client)
        conn.commit()

# Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    pass


with psycopg2.connect(database='client', user='postgres', password=77851100) as conn:
    pass
    # create_db(conn)
    # add_client(conn, 'ivan', 'poludurok', 'povelitel_kisok2005@mail.ru', '9204930011')
    # add_client(conn, 'lena', 'golovaсh', 'golovachlena@yandex.ru')
    # add_phone(conn, 2, '9156696610')
    # delete_phone(conn, 2, '9156696610')
    # delete_client(conn, 2)

conn.close()