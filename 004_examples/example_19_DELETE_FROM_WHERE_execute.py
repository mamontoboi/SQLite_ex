"""
Зараз таблиця sqlitedb_developers містить шість рядків, а видалятимемо розробника, чий id дорівнює 6. Ось що для
цього потрібно зробити:

Приєднатися до SQLite з Python;
Створити об'єкт Cursor за допомогою отриманого попереднього кроку об'єкта з'єднання SQLite;
Створити DELETE запит для SQLite. Саме на цьому етапі потрібно знати назви таблиці та колонок;
Виконати DELETE-запиту за допомогою cursor.execute();
Після виконання запиту необхідно закомітити зміни до бази даних;
Закрити з'єднання з базою даних;
Також важливо не забути перехопити винятки, що можуть виникнути;
Зрештою, перевірити результат операції.
"""

import sqlite3


def delete_record():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Підключений до SQLite")

        sql_delete_query = """DELETE FROM sqlitedb_developers WHERE id = 6"""
        cursor.execute(sql_delete_query)
        sqlite_connection.commit()
        print("Запис успішно видалено")
        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрито")


delete_record()

'''
Примітка: якщо виконується кілька операцій видалення, і є необхідність скасувати зміни в разі невдачі
хоча б з одним з них, потрібно використовувати функцію rollback() класу з'єднання для скасування. Цю функцію варто 
застосовувати всередині блоку except.
'''