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

p1 = Publisher(name='Альпина',
               books=[Book(title="6 минут: Ежедневник, который изменит вашу жизнь"),
                      Book(title="Тонкое искусство пофигизма: Парадоксальный способ жить счастливо"),
                      Book(title="Думай как математик: Как решать любые проблемы быстрее и эффективнее")])
p2 = Publisher(name='Питер', books=[
    Book(title="Python. Лучшие практики и инструменты"),
    Book(title="Python. Чистый код для продолжающих"),
    Book(title="Основы Data Science и Big Data. Python и наука о данных")])
b1 = Book(title="Паттерны разработки на Python: TDD, DDD и событийно-ориентированная архитектура", publisher=p2)
b2 = Book(title="Лабиринты Ехо", publisher=p2)
b3 = Book(title="Зачем нужны эмоции", publisher=p1)

shop1 = Shop(name="Лабиринт")
stock1 = Stock(book=b1, shop=shop1, count=50)
sale1 = Sale(price=250, stock=stock1, count=25)
stock2 = Stock(book=b3, shop=shop1, count=50)
sale2 = Sale(price=200, stock=stock2, count=15)

shop2 = Shop(name="ЕвроБук")
stock3 = Stock(book=b2, shop=shop2, count=50)
sale3 = Sale(price=250, stock=stock3, count=25)
stock4 = Stock(book=b2, shop=shop2, count=50)
sale4 = Sale(price=300, stock=stock4, count=15)

Session = sessionmaker(bind=engine)
session = Session()
# session.add_all([p1, p2, b1, b2, b3, shop1, shop2, stock1, stock2, stock3, stock4, sale1, sale2, sale3, sale4])
session.commit()

# x = input('Ведите имя писателя или id для вывода: ')
x = 'Альпина'

session.close()