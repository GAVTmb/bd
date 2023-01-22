import psycopg2
from pprint import pprint
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def create_db(cur):
    cur.execute("DROP TABLE Phone_number; "
                "DROP TABLE Client;")

    cur.execute("CREATE TABLE IF NOT EXISTS Client("
                "id SERIAL PRIMARY KEY, "
                "first_name VARCHAR(30) NOT NULL, "
                "last_name VARCHAR(30) NOT NULL, "
                "email VARCHAR(60) NOT NULL UNIQUE);")

    cur.execute("CREATE TABLE IF NOT EXISTS Phone_number("
                "id SERIAL PRIMARY KEY, "
                "phone_number VARCHAR(10) UNIQUE, "
                "Client_id INTEGER REFERENCES Client(id));")


# Функция, позволяющая добавить нового клиента!
def add_client(cur, first_name, last_name, email):
    cur.execute("INSERT INTO Client(first_name, last_name, email)"
                " VALUES(%s, %s, %s) RETURNING id;", (first_name, last_name, email))
    client_id = cur.fetchone()[0]
    conn.commit()
    return client_id


# Функция, позволяющая добавить телефон для существующего клиента!
def add_phone(cur, client_id, phone_number):
    cur.execute("INSERT INTO Phone_number(phone_number, Client_id) "
                "VALUES(%s, %s);", (phone_number, client_id))
    conn.commit()


# Функция, позволяющая изменить данные о клиенте!
def change_client(conn, cur, client_id, first_name=None, last_name=None, email=None, phone_number=None):
    cur.execute("UPDATE Client "
                "SET first_name=%s, last_name=%s, email=%s "
                "WHERE id=%s;", (first_name, last_name, email, client_id))
    cur.execute("UPDATE Phone_number "
                "SET phone_number=%s WHERE client_id=%s;", (phone_number, client_id))

# Функция, позволяющая удалить телефон для существующего клиента!
def delete_phone(cur, client_id, phone_number):
    cur.execute("DELETE FROM Phone_number WHERE phone_number=%s;", (phone_number,))

# Функция, позволяющая удалить существующего клиента
def delete_client(cur, client_id):
    cur.execute("DELETE FROM Phone_number WHERE Client_id=%s;", (client_id,))
    conn.commit()
    cur.execute("DELETE FROM Client WHERE id=%s;", (client_id,))

# Функции, позволяющие найти клиента по его данным (имени, фамилии, email-у или телефону)
def find_client(cur, search_data):
    q = search_data.split()
    q.reverse()
    for i in q:
        p_n = search_by_phone_number(cur, i)
        e = search_by_email(cur, i)
        l_n = search_by_last_name(cur, i)
        n = search_by_name(cur, i)
        if len(p_n) >= 1:
            return p_n
            # break
        elif len(e) >= 1:
            return e
            # break
        elif len(l_n) >= 1:
            return l_n[0]
        elif len(n) >= 1:
            return n
        else:
            print('НЕТ')

# Функции, позволяющие найти клиента по его имени
def search_by_name(cur, search_data):
    cur.execute("SELECT Client.id, first_name, last_name, email, phone_number FROM Client "
                "LEFT JOIN Phone_number ON Phone_number.Client_id=Client.id "
                "WHERE first_name=%s;", (search_data, ))
    result = cur.fetchall()
    return result

# Функции, позволяющие найти клиента по его фамилии
def search_by_last_name(cur, search_data):
    cur.execute("SELECT Client.id, first_name, last_name, email, phone_number FROM Client "
                "LEFT JOIN Phone_number ON Phone_number.Client_id=Client.id "
                "WHERE last_name=%s;", (search_data,))
    result = cur.fetchall()
    return result

# Функции, позволяющие найти клиента по его email
def search_by_email(cur, search_data):
    cur.execute("SELECT Client.id, first_name, last_name, email, phone_number FROM Client "
                "LEFT JOIN Phone_number ON Phone_number.Client_id=Client.id "
                "WHERE email=%s;", (search_data,))
    result = cur.fetchall()
    return result

# Функции, позволяющие найти клиента по его номеру телефона
def search_by_phone_number(cur, search_data):
    cur.execute("SELECT Client.id, first_name, last_name, email, phone_number FROM Client "
                "LEFT JOIN Phone_number ON Phone_number.Client_id=Client.id "
                "WHERE phone_number LIKE %s;", (search_data,))
    result = cur.fetchall()
    return result

def all_clients ():
    cur.execute("SELECT Client.id, first_name, last_name, email, phone_number FROM Client "
                "LEFT JOIN Phone_number ON Phone_number.Client_id=Client.id;")
    pprint(cur.fetchall())


with psycopg2.connect(database='client', user='postgres', password=os.getenv('PASS')) as conn:
    with conn.cursor() as cur:
        while True:
            enter_the_command = input('Введите команду: ').lower()
            if enter_the_command == '1':
                create_db(cur)
            elif enter_the_command == '2':
                first_name = input('Введите имя: ').lower()
                last_name = input('Введите фамилию: ').lower()
                email = input('Введите электронную почту: ').lower()
                phone_number = input('Введите номер телефона: +7 ')
                if len(phone_number) == 0:
                    add_client(cur, first_name, last_name, email)
                else:
                    client_id = add_client(cur, first_name, last_name, email)
                    add_phone(cur, client_id, phone_number)
            elif enter_the_command == '3':
                search_data = input('Введите данные клиента которому добавляем телефон: ').lower()
                phone_number = input('Введите номер телефона: +7').lower()
                result = find_client(cur, search_data)
                client_id = result[0][0]
                add_phone(cur, client_id, phone_number)
            elif enter_the_command == '4':
                change_client(cur, client_id, first_name=None, last_name=None, email=None, phone_number=None)
            elif enter_the_command == '5':
                delete_phone(cur, client_id, phone_number)
            elif enter_the_command == '6':
                delete_client(cur, client_id)
            elif enter_the_command == '7':
                search_data = input('Введите данные клиента(именя, фамилию, email или телефон(без +7)): ').lower()
                pprint(find_client(cur, search_data))
            elif enter_the_command == '0':
                all_clients()
            elif enter_the_command == 'stop':
                print('Программа завершена. Досвидания!')
                break
            else:
                print('Вы ввели не верную команду, попробуйте снова!')

conn.close()
