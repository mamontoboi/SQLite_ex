"""
--------------Вставка/отримання об'єкта DateTime--------------

Зазвичай при виконанні запиту на вставку об'єкта datetime модуль sqlite3 у Python конвертує його у рядковий формат.
Те саме відбувається при отриманні даних з таблиці - вони повертаються у рядковому форматі.
"""

import sqlite3
import datetime


def add_developer(dev_id, name, joining_date):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_create_table_query = '''CREATE TABLE new_developers (
                                       id INTEGER PRIMARY KEY,
                                       name TEXT NOT NULL,
                                       joiningDate timestamp);'''

        cursor.execute(sqlite_create_table_query)

        # вставити дані розробника
        sqlite_insert_with_param = """INSERT INTO new_developers
                          ('id', 'name', 'joiningDate')
                          VALUES (?, ?, ?);"""

        data_tuple = (dev_id, name, joining_date)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()
        print("Розробник успішно доданий\n")

        # отримати дані розробника
        sqlite_select_query = """SELECT name, joiningDate FROM new_developers WHERE id = ?"""
        cursor.execute(sqlite_select_query, (1,))
        records = cursor.fetchall()

        for row in records:
            developer = row[0]
            joining_date = row[1]
            print(developer, "приєднався", joining_date)
            print("тип дати", type(joining_date))
        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрито")


add_developer(1, 'Mark', datetime.datetime.now())

