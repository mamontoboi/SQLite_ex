"""
-----------------Оновлення кількох рядків SQLite-таблиці------------------------

В останньому прикладі використовувався метод execute() об'єкта cursor для оновлення одного значення, але іноді в
додатках Python потрібно оновити кілька рядків. Наприклад, потрібно збільшити зарплату більшості розробників на 20%.
Одночасно виконання операції UPDATE щоразу для кожного запису можна виконати масове оновлення в один запит.
За допомогою методу cursor.executemany() можна змінити кілька записів у таблиці SQLite в один запит.

Метод cursor.executemany(query, seq_param) приймає два аргументи: SQL-запит та список записів для оновлення.
"""

import sqlite3


def update_multiple_records(record_list):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_update_query = """UPDATE sqlitedb_developers SET salary = ? WHERE id = ?"""
        cursor.executemany(sqlite_update_query, record_list)
        sqlite_connection.commit()
        print("Записів", cursor.rowcount, ". Успішно оновлені")
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрито")


records_to_update = [(9700, 4), (7800, 5), (8400, 6)]
update_multiple_records(records_to_update)

'''
Після підключення до таблиці SQLite готується SQLite-запит із двома заповнювачами (колонки salary та id), а також 
список записів для оновлення у форматі кортежу.
Кожен елемент – це кортеж кожного запису. Кожен кортеж містить два значення: зарплату та id розробника.
Функція cursor.executemany(sqlite_update_query, record_list) викликається оновлення кількох рядків таблиці SQLite.
Щоб дізнатися, скільки записів було змінено, використовується функція cursor.rowcount. Нарешті, дані зберігаються
до бази даних за допомогою методу commit класу connection
'''