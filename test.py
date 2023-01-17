import psycopg2


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
                        phone_number VARCHAR(10) UNIQUE,
                        Client_id INTEGER REFERENCES Client(id)
                        );
            """)
        conn.commit()
# Функция, позволяющая добавить нового клиента!
def add_client(conn, first_name, last_name, email):
    with conn.cursor() as cur:
        execute_client = f"INSERT INTO Client(first_name, last_name, email)" \
                        f" VALUES('{first_name}', '{last_name}', '{email}');"
        cur.execute(execute_client)
        conn.commit()
        cur.execute("""SELECT id FROM Client WHERE email=%s;""", (f'{email}',))
        client_id = cur.fetchone()[0]
        return client_id

# Функция, позволяющая добавить телефон для существующего клиента!
def add_phone(conn, client_id, phone_number):
    with conn.cursor() as cur:
        insert_phone = f"INSERT INTO Phone_number(phone_number, Client_id) VALUES('{phone_number}', {client_id});"
        cur.execute(insert_phone)
        conn.commit()


# Функция, позволяющая изменить данные о клиенте!
def change_client(conn, client_id, first_name=None, last_name=None, email=None, phone_number=None):
    pass
# Функция, позволяющая удалить телефон для существующего клиента!
def delete_phone(conn, client_id, phone_number):
    pass
# Функция, позволяющая удалить существующего клиента
def delete_client(conn, client_id):
    pass
# Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    print(first_name, last_name, email, phone_number)
    # with conn.cursor() as cur:
    #     cur.execute



with psycopg2.connect(database='client', user='postgres', password=77851100) as conn:
    while True:
        enter_the_command = input('Введите команду: ').lower()
        if enter_the_command == '1':
            create_db(conn)
        elif enter_the_command == '2':
            first_name = input('Введите имя: ').lower()
            last_name = input('Введите фамилию: ').lower()
            email = input('Введите электронную почту: ').lower()
            phone_number = input('Введите номер телефона: +7 ')
            print(len(phone_number))
            if len(phone_number) == 0:
                client_id = add_client(conn, first_name, last_name, email)
            else:
                client_id = add_client(conn, first_name, last_name, email)
                add_phone(conn, client_id, phone_number)

        elif enter_the_command == '3':
            add_phone(conn, client_id, phone_number)
        elif enter_the_command == '4':
            change_client(conn, client_id, first_name=None, last_name=None, email=None, phone_number=None)
        elif enter_the_command == '5':
            delete_phone(conn, client_id, phone_number)
        elif enter_the_command == '6':
            delete_client(conn, client_id)
        elif enter_the_command == '7':
            print('Введите данные клиента(именя, фамилию, email или телефон(без +7)): ')
            first_name = input('Введите имя: ').lower()
            last_name = input('Введите фамилию: ').lower()
            email = input('Введите электронную почту: ').lower()
            phone_number = input('Введите номер телефона: +7 ')
            find_client(conn, first_name, last_name, email, phone_number)
        elif enter_the_command == 'stop':
            print('Программа завершена. Досвидания!')
            break
        else:
            print('Вы ввели не верную команду, попробуйте снова!')

conn.close()
with conn.cursor() as cur:
    cur.execute("""SELECT * FROM Client;""")
    print(cur.fetchall())
    cur.execute("""SELECT * FROM Phone_number;""")
    print(cur.fetchall())