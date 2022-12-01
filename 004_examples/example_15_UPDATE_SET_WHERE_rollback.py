"""
Зараз таблиця sqlitedb_developers містить шість рядків, тому оновимо зарплату розробника з ID 4. Для виконання запиту
UPDATE з Python потрібно виконати наступні кроки:

Спочатку потрібно встановити SQLite-з'єднання з Python.
Далі необхідно створити об'єкт cursor за допомогою об'єкта з'єднання.
Після цього створити запит UPDATE. Для цього потрібно знати назви таблиці та колонки, яку потрібно оновити.
Далі запит виконується за допомогою cursor.execute().
Після успішного завершення запиту потрібно не забути закомітити зміни до бази даних.
З'єднання з базою даних закривається.
Також важливо не забути перехоплювати всі винятки SQLite.
Нарешті, потрібно переконатися, що операція пройшла успішно, отримавши дані таблиці.
"""

import sqlite3


def update_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Підключений до SQLite")

        sql_update_query = """UPDATE sqlitedb_developers SET salary = 10000 WHERE id = 4"""
        cursor.execute(sql_update_query)
        sqlite_connection.commit()
        print("Запис успішно оновлено")
        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрито")


update_sqlite_table()

# Примітка: якщо виконується операція масового оновлення і є необхідність відкотити зміни у разі помилки хоча б при
# одному, потрібно використовувати функцію rollback() класу connection. Її необхідно застосувати у блоці except
