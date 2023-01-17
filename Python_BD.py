
import psycopg2

conn = psycopg2.connect(database='client', user='postgres', password=77851100)

with conn.cursor() as cur:
    cur.execute("""
        DROP TABLE Phone_number;
        DROP TABLE Name;
    """)


    cur.execute("""
            CREATE TABLE IF NOT EXISTS Name(
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(30) NOT NULL,
                last_name VARCHAR(30) NOT NULL,
                email VARCHAR(60) NOT NULL
                );
    """)

    cur.execute("""
            CREATE TABLE IF NOT EXISTS Phone_number(
                id SERIAL PRIMARY KEY,
                phone_number VARCHAR(10) UNIQUE,
                Name_id INTEGER REFERENCES Name(id)
                );
    """)
    conn.commit()

    cur.execute("""
            INSERT INTO Name(first_name, last_name, email)
            VALUES('ivan', 'ivanov', 'ivan_ivanov@mail.ru'),
                  ('petr', 'petrov', 'petr_petrov@gmail.com'),
                  ('vladlena', 'ilyina', 'vl_il@yandex.ru');
    """)

    cur.execute("""
            INSERT INTO Name(first_name, last_name, email)
            VALUES('ivan', 'poludurok', 'povelitel_kisok2005@mail.ru'),
                  ('lena', 'golovaсh', 'golovachlena@yandex.ru'),
                  ('edward', 'zadripysh', 'edward_zad@gmail.com'),
                  ('venya', 'petushkov', 'petushok09@mail.ru');
    """)

    cur.execute("""
                INSERT INTO Phone_number(phone_number, Name_id)
                VALUES('9304956773', 7), ('9204930011', 1), ('9321123587', 1), ('9674956013', 5),
                      ('9674956012', 2), ('9156696510', 3), ('9102346751', 4), ('9156696610', 5);
        """)

    cur.execute("""DELETE FROM Phone_number WHERE Name_id = 1;""")

    cur.execute("""
            SELECT * FROM Name
            LEFT JOIN Phone_number ON Name.id = Phone_number.Name_id;
    """)

    r = cur.fetchall()
    for q in r:
        print(q)

    # cur.execute("""
    #            SELECT * FROM Phone_number;
    #    """)
    # w = cur.fetchall()
    # for i in w:
    #     print(i)

conn.close()


# phone = '9674956012'
#     insert = f'INSERT INTO Phone_number(phone_number, Name_id) VALUES({phone}, 7);'
#     cur.execute(insert)
#     conn.commit()