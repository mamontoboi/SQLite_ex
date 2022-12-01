"""
Зазвичай при виконанні запиту на вставку об'єкта datetime модуль sqlite3 у Python конвертує його в рядковий формат.
Те саме відбувається при отриманні даних з таблиці - вони повертаються у рядковому форматі.
"""

import sqlite3


def read_sqlite_table(records):
    try:
        # Встановлення з'єднання з БД
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        # Отримання об'єкта Cursor з об'єкта з'єднання
        cursor = sqlite_connection.cursor()
        print("Підключений до SQLite")
        # Підготовка запиту SELECT для отримання всіх рядків з таблиці sqlitedb_developers. Вона містить п'ять колонок.
        sqlite_select_query = """SELECT * from sqlitedb_developers"""
        cursor.execute(sqlite_select_query)
        # Після успішного виконання запиту використовується метод cursor.fetchall() для всіх (cursor.fetchone()
        # - для одного рядка / cursor.fetchmany(SIZE) - для обмеженої кількості рядків) записів таблиці
        # sqlitedb_developers.
        records = cursor.fetchall()
        print("Усього рядків:  ", len(records))
        print("Виведення кожного рядка")

        # Перебір всіх записів та виведення їх по одному
        for row in records:
            print("ID:", row[0])
            print("Ім'я:", row[1])
            print("Пошта:", row[2])
            print("Доданий:", row[3])
            print("Зарплата:", row[4], end="\n\n")
        # об'єкт Cursor закривається
        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)

    finally:
        # Закриття з'єднання з БД
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрито")


read_sqlite_table(1)

'''
У цьому прикладі прямо відображаються рядок і значення колонки. Якщо вам потрібно використовувати значення колонки у 
своїй програмі, їх можна зберігати в змінні Python. І тому потрібно написати, наприклад, так: name = row[1]
'''