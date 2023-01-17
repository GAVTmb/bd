import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import psycopg2

# Функция, создающая структуру БД (таблицы)!
def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
                DROP TABLE Phone_number;
                DROP TABLE Client;
            """)
        cur.execute("CREATE TABLE IF NOT EXISTS Client("
                    "id SERIAL PRIMARY KEY, "
                    "first_name VARCHAR(30) NOT NULL, "
                    "last_name VARCHAR(30) NOT NULL, "
                    "email VARCHAR(60) NOT NULL UNIQUE);")
        conn.commit()
        cur.execute("CREATE TABLE IF NOT EXISTS Phone_number("
                    "id SERIAL PRIMARY KEY, "
                    "phone_number VARCHAR(10), "
                    "Client_id INTEGER REFERENCES Client(id));")
        conn.commit()

# Функция, позволяющая добавить нового клиента!+
def add_client(conn, first_name, last_name, email, phone_number=None):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO Client(first_name, last_name, email)"
                    " VALUES(%s, %s, %s) RETURNING id;", (first_name, last_name, email))
        client_id = cur.fetchone()[0]
        if phone_number is None:
            pass
        else:
            add_phone(conn, client_id, phone_number)
            conn.commit()

# Функция, позволяющая добавить телефон для существующего клиента!+
def add_phone(conn, client_id, phone_number):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO Phone_number(phone_number, Client_id) "
                    "VALUES(%s, %s);", (phone_number, client_id))
        conn.commit()

# Функция, позволяющая изменить данные о клиенте!
def change_client(conn, client_id, first_name=None, last_name=None, email=None, phone_number=None):
    with conn.cursor() as cur:
        cur.execute("UPDATE Client "
                    "SET first_name=%s, last_name=%s, email=%s "
                    "WHERE id=%s;", (first_name, last_name, email, client_id))
        cur.execute("UPDATE Phone_number "
                    "SET phone_number=%s WHERE client_id=%s;", (phone_number, client_id))
        conn.commit()
# Функция, позволяющая удалить телефон для существующего клиента!+
def delete_phone(conn, client_id, phone_number):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM Phone_number WHERE phone_number=%s;", (phone_number,))
        conn.commit()

# Функция, позволяющая удалить существующего клиента!+
def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM Phone_number WHERE Client_id=%s;", (client_id,))
        conn.commit()
        cur.execute("DELETE FROM Client WHERE id=%s;", (client_id,))
        conn.commit()

# Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
def find_client(conn, search_data):
    with conn.cursor() as cur:
        cur.execute("SELECT Client.id, first_name, last_name, email, phone_number FROM Client "
                    "LEFT JOIN Phone_number ON Phone_number.Client_id=Client.id "
                    "WHERE first_name=%s;", (search_data, ))
        result = cur.fetchall()
        if len(result) > 0:
            print(result)

        cur.execute("SELECT Client.id, first_name, last_name, email, phone_number FROM Client "
                    "LEFT JOIN Phone_number ON Phone_number.Client_id=Client.id "
                    "WHERE last_name=%s;", (search_data,))
        result = cur.fetchall()
        if len(result) > 0:
            print(result)

        cur.execute("SELECT Client.id, first_name, last_name, email, phone_number FROM Client "
                    "LEFT JOIN Phone_number ON Phone_number.Client_id=Client.id "
                    "WHERE email=%s;", (search_data,))
        result = cur.fetchall()
        if len(result) > 0:
            print(result)

        cur.execute("SELECT Client.id, first_name, last_name, email, phone_number FROM Client "
                    "LEFT JOIN Phone_number ON Phone_number.Client_id=Client.id "
                    "WHERE phone_number=%s;", (search_data,))
        result = cur.fetchall()
        if len(result) > 0:
            print(result)

with psycopg2.connect(database='client', user='postgres', password=os.getenv('PASS')) as conn:
    pass
    # create_db(conn)
    # add_client(conn, 'ivan', 'poludurok', 'povelitel_kisok2005@mail.ru', '9204930010')
    # add_client(conn, 'lena', 'golovaсh', 'golovachlena@yandex.ru')
    # add_client(conn, 'ivan', 'ivanov', 'ivan_ivanov@mail.ru', '9674956012')
    # add_phone(conn, 2, '9156696610')
    # change_client(conn, 1, 'edward', 'zadripysh', 'edward_zad@gmail.com', '9204930013')
    # delete_phone(conn, 2, '9156696610')
    # delete_client(conn, 2)
    find_client(conn, 'ivan')

    # with conn.cursor() as cur:
    #     cur.execute("SELECT Client.id, first_name, last_name, email, phone_number FROM Client "
    #                 "LEFT JOIN Phone_number ON Phone_number.Client_id=Client.id;")
    #     r = cur.fetchall()
    #     for q in r:
    #         print(q)
conn.close()