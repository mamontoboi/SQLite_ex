"""
Використання змінних у запитах для видалення рядка
Здебільшого видаляти рядки з таблиці SQLite потрібно за допомогою ключа, який передається вже під час роботи
програми. Наприклад, коли користувач видаляє підписку, запис про нього потрібно видалити з таблиці.

У таких випадках потрібно використовувати запит із параметрами. У таких запитах на місці майбутніх значень ставляться
заповнювачі (?). Це допомагає видаляти записи, отримуючи значення під час роботи програми, та уникати проблем
SQL-ін'єкцій. Ось приклад із видаленням розробника з id=5.
"""

import sqlite3


def delete_sqlite_record(dev_id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Підключений до SQLite")

        sql_update_query = """DELETE FROM sqlitedb_developers WHERE id = ?"""
        cursor.execute(sql_update_query, (dev_id, ))
        sqlite_connection.commit()
        print("Запис успішно видалено")
        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрито")


delete_sqlite_record(5)

'''
Запит з параметрами використовувався, щоб отримати id розробника під час роботи програми та підставити його на
місце?. Він визначає id запис, який буде видалено.
Після цього створюється кортеж даних за допомогою змінних Python.
Далі DELETE-запит разом із даними передається у метод cursor.execute().
Нарешті, зміни зберігаються у базі даних за допомогою методу commit() класу Connection.
'''