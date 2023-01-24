import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from pprint import pprint

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Sale, Book, Stock, Shop
# {os.getenv("PASS")}

DSN = f'postgresql://postgres:{os.getenv("PASS")}@localhost:5432/books'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

p1 = Publisher(name='Альпина')

p2 = Publisher(name='Питер')

b1 = Book(title="Основы разработки на Python", publisher=p2)
b2 = Book(title="Лабиринты Ехо", publisher=p2)
b3 = Book(title="Зачем нужны эмоции", publisher=p1)
b4 = Book(title='Скотный двор', publisher=p1)

sh1 = Shop(name="Лабиринт")
sh2 = Shop(name="ЕвроБук")

stock1 = Stock(book=b1, shop=sh1, count=204)
stock2 = Stock(book=b1, shop=sh2, count=20)
stock3 = Stock(book=b2, shop=sh2, count=23)
stock4 = Stock(book=b3, shop=sh2, count=29)
stock5 = Stock(book=b4, shop=sh1, count=31)

sale1 = Sale(price=1000, date_sale='2022-09-16', stock=stock1, count=2)
sale2 = Sale(price=1300, date_sale='2022-10-16', stock=stock4, count=2)
sale3 = Sale(price=980, date_sale='2022-09-16', stock=stock2, count=2)

Session = sessionmaker(bind=engine)
session = Session()
session.add_all([p1, p2, b1, b2, b3, b3, sh1, sh2, stock1, stock2, stock3, stock4, stock5, sale1, sale2])
session.commit()


pub_name = 'Питер'

pprint(session.query(Publisher.name, Book.title, Shop.name, Sale.price, Sale.date_sale)
       .join(Book).join(Stock).join(Shop).join(Sale).filter(Publisher.name == pub_name).all())



session.close()
