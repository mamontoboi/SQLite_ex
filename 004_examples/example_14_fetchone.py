"""
Отримання одного рядка з таблиці
Коли потрібно отримати один рядок із таблиці SQLite, варто використовувати метод fetchone() класу cursor. Цей метод
необхідний у випадках, коли відомо, що запит поверне один рядок.

cursor.fetchone() отримує лише наступний рядок із результату. Якщо рядків немає, то повертається None.
"""

import sqlite3


def read_single_row(developer_id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Підключений до SQLite")

        sqlite_select_query = """SELECT * FROM sqlitedb_developers WHERE id = ?"""
        cursor.execute(sqlite_select_query, (developer_id, ))
        print("Читання одного рядка\n")
        record = cursor.fetchone()
        print("ID:", record[0])
        print("Ім'я:", record[1])
        print("Пошта:", record[2])
        print("Доданий:", record[3])
        print("Зарплата:", record[4])

        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрито")


read_single_row(3)
