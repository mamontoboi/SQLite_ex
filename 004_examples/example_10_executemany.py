"""
У попередньому прикладі для вставки одного запису в таблицю використовувався метод execute() об'єкта cursor, але іноді
потрібно вставити кілька рядків.

Наприклад, при читанні файлу, наприклад CSV, може знадобитися додати всі записи з нього до таблиці SQLite. Разом
виконання запиту INSERT для кожного запису, можна виконати всі операції на один запит. Додати кілька записів у
таблицю SQLite можна за допомогою методу executemany() об'єкта cursor.

Цей метод приймає два аргументи: запит SQL та список записів.
"""

import sqlite3


def insert_multiple_records(records):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Підключений до SQLite")
        # Інструкція SQLite INSERT містить запит із параметрами, де на місці кожного значення стоїть
        # знак запитання.
        sqlite_insert_query = """INSERT INTO sqlitedb_developers
                                 (name, email, joining_date, salary)
                                 VALUES (?, ?, ?, ?);"""
        # Далі в таблицю вставляються кілька записів
        cursor.executemany(sqlite_insert_query, records)  # receives several entries in form of list
        sqlite_connection.commit()
        # Кількість вставлених рядків використається метод cursor.rowcount.
        print("Записи успішно вставлені в таблицю sqlitedb_developers", cursor.rowcount)
        # Зберігаємо зміни до БД
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрито")


# Після підключення до бази даних готується список записів для вставлення таблиці.
# Кожна з них — це лише рядок.
records_to_insert = [('Jaroslav', 'idebylos22@gmail.com', '2020-11-14', 8500),
                     ('Timofei', 'ullegyddom33m@gmail.com', '2020-11-15', 6600),
                     ('Nikita', 'aqillyss55o@gmail.com', '2020-11-27', 7400)]

insert_multiple_records(records_to_insert)
