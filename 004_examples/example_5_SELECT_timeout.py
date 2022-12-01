"""
Буває таке, що є кілька підключень до баз даних SQLite і одне з них виконує певні зміни.
Для цього підключення потрібне блокування блокування - база даних блокується доти, доки транзакція не буде
завершено.

Параметр тайм-аут, який задається при підключенні, визначається, як довго з'єднання очікуватиме очікування
блокування перед поверненням винятків.

За промовчанням значення цього параметра дорівнює 5.0 (5 секунд). Його не потрібно ставити, тому що це значення за
промовчанням.
Таким чином, підключення до бази даних з Python, якщо відповідь не буде отримано протягом 5 секунд, знайти
виняток. Однак параметр можна встановити в функції sqlite3.connect.
"""

import sqlite3


def read_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db', timeout=20)
        cursor = sqlite_connection.cursor()
        print("Підключений до SQLite")

        sqlite_select_query = """SELECT count(*) from sqlitedb_developers"""
        cursor.execute(sqlite_select_query)
        total_rows = cursor.fetchone()
        print("Всього рядків: ", total_rows)
        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при підключенні до sqlite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрито")


read_sqlite_table()
