"""
Перевизначення існуючих функцій SQLite
Іноді потрібно перевизначити існуючі функції. Наприклад, при поверненні імені користувача необхідно, щоб
воно було у верхньому регістрі.
Як демонстрацію конвертуємо вбудовану в SQLite функцію LOWER в UPPER, щоб при її виклику вона перетворювала
вхідні дані у верхній регістр.
Створимо нове визначення функції lower() за допомогою методу connection.create_function(). Таким чином, ми
перезаписуємо вже існуючу реалізацію функції lower().
"""
import sqlite3


def lower(string):
    return str(string).upper()


def get_developer_name(dev_id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Підключений до SQLite")

        sqlite_connection.create_function("lower", 1, lower)
        select_query = "SELECT lower(name) FROM sqlitedb_developers WHERE id = ?"
        cursor.execute(select_query, (dev_id,))
        name = cursor.fetchone()
        print("Ім'я розробника", name)
        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрито")


get_developer_name(1)
