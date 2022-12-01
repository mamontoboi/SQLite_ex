"""
Використання Python у запиті UPDATE
Більшість часу оновлення таблиці необхідно виконати за допомогою використання наявних при роботі програм. Наприклад,
коли користувачі оновлюють свій профіль через графічний інтерфейс, необхідно оновити задані зображення
складена таблиця.

У таких випадках рекомендується використовувати запит із параметрами. Такі запити використовують заповнювачі (?) прямо
всередині SQL-інструкцій. Це допомагає використовувати значення, а також запобігати ін'єкції SQL.
"""

import sqlite3


def update_sqlite_table(dev_id, salary):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Підключений до SQLite")

        sql_update_query = """UPDATE sqlitedb_developers SET salary = ? WHERE id = ?"""
        data = (salary, dev_id)
        cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        print("Запис успішно оновлено")
        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрито")


update_sqlite_table(3, 7500)

'''
Запит з параметрами був використаний для того, щоб отримати значення під час роботи програми та встановити їх на місця
наповнювачів. У цьому випадку один з них відповідає за стовпчик «salary», а другий – стовпчик id.
Після цього готується кортеж із даними із двох змінних Python у визначеному порядку. Цей кортеж разом із запитом
передається у метод cursor.execute(). Важливо, що у разі порядок змінних у кортежі грає значення.
Наприкінці зміни закріплюються за допомогою методу commit класу connection.
'''