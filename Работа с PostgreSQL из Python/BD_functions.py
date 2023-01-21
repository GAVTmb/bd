import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import psycopg2

# Функция, создающая структуру БД (таблицы)!
def create_db(cur):
    cur.execute("""
            DROP TABLE Phone_number;
            DROP TABLE Client;
        """)
    cur.execute("CREATE TABLE IF NOT EXISTS Client("
                "id SERIAL PRIMARY KEY, "
                "first_name VARCHAR(30) NOT NULL, "
                "last_name VARCHAR(30) NOT NULL, "
                "email VARCHAR(60) NOT NULL UNIQUE);")

    cur.execute("CREATE TABLE IF NOT EXISTS Phone_number("
                "id SERIAL PRIMARY KEY, "
                "phone_number VARCHAR(10), "
                "Client_id INTEGER REFERENCES Client(id));")


# Функция, позволяющая добавить нового клиента!+
def add_client(cur, first_name, last_name, email, phone_number=None):
    cur.execute("INSERT INTO Client(first_name, last_name, email)"
                " VALUES(%s, %s, %s) RETURNING id;", (first_name, last_name, email))
    client_id = cur.fetchone()[0]
    if phone_number is None:
        pass
    else:
        add_phone(cur, client_id, phone_number)


# Функция, позволяющая добавить телефон для существующего клиента!+
def add_phone(cur, client_id, phone_number):
    cur.execute("INSERT INTO Phone_number(phone_number, Client_id) "
                "VALUES(%s, %s);", (phone_number, client_id))
    conn.commit()


# Функция, позволяющая изменить данные о клиенте!
def change_client(cur, client_id, what_to_change, change_to):
    if what_to_change in ('first_name', 'last_name', 'email'):
        cur.execute(f"UPDATE Client SET {what_to_change}=%s "
                    "WHERE id=%s;", (change_to, client_id))
    elif what_to_change in ('phone_number'):
        cur.execute("UPDATE Phone_number "
                    "SET phone_number=%s WHERE client_id=%s;", (change_to, client_id))

# Функция, позволяющая удалить телефон для существующего клиента!+
def delete_phone(cur, client_id, phone_number):
    cur.execute("DELETE FROM Phone_number WHERE phone_number=%s;", (phone_number,))


# Функция, позволяющая удалить существующего клиента!+
def delete_client(cur, client_id):
    cur.execute("DELETE FROM Phone_number WHERE Client_id=%s;", (client_id,))
    conn.commit()
    cur.execute("DELETE FROM Client WHERE id=%s;", (client_id,))


# Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
def find_client(cur, search_data):
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
    with conn.cursor() as cur:
        # create_db(cur)
        # add_client(cur, 'ivan', 'poludurok', 'povelitel_kisok2005@mail.ru', '9204930010')
        # add_client(cur, 'lena', 'golovaсh', 'golovachlena@yandex.ru')
        # add_client(cur, 'ivan', 'ivanov', 'ivan_ivanov@mail.ru', '9674956012')
        # add_phone(cur, 2, '9156696610')
        # change_client(cur, 1, 'first_name', 'vasgen')
        # delete_phone(cur, 2, '9156696610')
        # delete_client(cur, 2)}
        find_client(cur, 'ivan')


        # cur.execute("SELECT Client.id, first_name, last_name, email, phone_number FROM Client "
        #             "LEFT JOIN Phone_number ON Phone_number.Client_id=Client.id;")
        # r = cur.fetchall()
        # for q in r:
        #     print(q)
conn.close()