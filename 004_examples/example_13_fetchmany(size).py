"""
------------Отримання кількох рядків із таблиці------------

У деяких випадках спроба отримати всі рядки з таблиці займе надто багато часу, особливо якщо їх там тисячі.
Для отримання всіх рядків потрібно більше ресурсів: пам'яті та часу обробки. А для покращення продуктивності у таких
У випадках рекомендується використовувати метод fetchmany(size) класу сursor для отримання фіксованої кількості рядків.
За допомогою cursor.fetchmany(size) можна вказати, скільки рядків потрібно прочитати.
"""

import sqlite3


def read_limited_rows(row_size):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Підключений до SQLite")

        sqlite_select_query = """SELECT * from sqlitedb_developers"""
        cursor.execute(sqlite_select_query)
        print("Читання ", row_size, " рядків")
        records = cursor.fetchmany(row_size)
        print("Виведення кожного рядка\n")

        for row in records:
            print("ID:", row[0])
            print("Ім'я:", row[1])
            print("Пошта:", row[2])
            print("Доданий:", row[3])
            print("Зарплата:", row[4], end="\n\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрито")


read_limited_rows(2)
