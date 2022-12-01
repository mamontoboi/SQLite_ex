"""
---------------Використання змінних як параметри Select-запиту---------------

Часто є необхідність передати змінну до SELECT-запиту для перевірки певної умови.
Припустимо, програма хоче зробити запит для отримання інформації про розробників, використовуючи їх id. Для цього
потрібен запит із параметрами. Це такий запит, де всередині використовуються заповнювачі (?) на місці параметрів, які
потім замінюються реальними значеннями.

cursor.execute("SELECT salary FROM sqlitedb_developers WHERE id = "ID із програми")

"""
import sqlite3


def get_developer_info(id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Підключений до SQLite")

        sql_select_query = """SELECT * FROM sqlitedb_developers WHERE id = ?"""
        cursor.execute(sql_select_query, (id,))  # id in form of tuple... Hmmm...
        records = cursor.fetchall()
        print("Виведення ID ", id)

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


get_developer_info(2)
