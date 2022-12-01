"""
Використання змінних у запиті INSERT
Іноді в колонку таблиці слід вставити значення змінної Python. Цією змінною може бути будь-що: ціле число,
рядок, число з плаваючою точкою, datetime. Наприклад, під час реєстрації користувач вводить свої дані. Їх і можна взяти
вставити до таблиці SQLite.

Для цього є запит із параметрами. Він дозволяє використовувати змінні Python на місці заповнювачів (?) у запиті
"""

import sqlite3


def insert_varible_into_table(name, email, join_date, salary):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Підключений до SQLite")
        # ігнорування при додаванні помилки та продовження додавання запису
        sqlite_insert_with_param = """INSERT OR IGNORE INTO sqlitedb_developers
                              (name, email, joining_date, salary)
                              VALUES (?, ?, ?, ?);"""

        # заміна значень у таблиці щоразу, коли запис вже існує
        """sqlite_insert_with_param = INSERT or REPLACE INTO sqlitedb_developers
                                      (name, email, joining_date, salary)
                                      VALUES (?, ?, ?, ?);
        """
        data_tuple = (name, email, join_date, salary)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()
        print("Змінні Python успішно вставлені в таблицю sqlitedb_developers")
        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрито")


insert_varible_into_table('Viktoria', 's_dom34@gmail.com', '2020-11-19', 6000)
insert_varible_into_table('Valentin', 'exp3@gmail.com', '2020-11-23', 6500)

# Таблиця sqlitedb_developers після вставки змінної Python як значення колонки. Перевірити результат можна,
# отримавши дані з таблиці.
