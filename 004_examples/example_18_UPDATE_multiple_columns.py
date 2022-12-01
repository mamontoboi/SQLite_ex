"""
Оновлення кількох колонок SQLite
Можна оновити кілька колонок SQLite в один запит. Для цього потрібно лише підготувати запит із параметрами
та заповнювачами.
"""

import sqlite3


def update_multiple_columns(dev_id, salary, email):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Підключений до SQLite")

        sqlite_update_query = """UPDATE sqlitedb_developers SET salary = ?, email = ? WHERE id = ?"""
        column_values = (salary, email, dev_id)
        cursor.execute(sqlite_update_query, column_values)
        sqlite_connection.commit()
        print("Декілька стовпців успішно оновлено")
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрито")


update_multiple_columns(3, 2500, 'bec9988@gmail.com')
