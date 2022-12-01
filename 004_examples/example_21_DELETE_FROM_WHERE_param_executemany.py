"""
----------------------Операція Delete для видалення кількох рядків--------------------------

Часто доводиться видаляти відразу кілька одночасно.
Замість виконання запиту DELETE кожного разу для кожного запису можна виконати операцію масового видалення в одному
запит. Видалити кілька записів із SQLite-таблиці в один запит можна за допомогою методу cursor.executemany().
Метод cursor.executemany(query, seq_param) приймає два аргументи: SQL-запит та список записів для видалення.
"""

import sqlite3


def delete_multiple_records(ids_list):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Підключений до SQLite")

        sqlite_update_query = """DELETE FROM sqlitedb_developers WHERE id = ?"""
        cursor.executemany(sqlite_update_query, ids_list)
        sqlite_connection.commit()
        print("Видалено записів:", cursor.rowcount)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрито")


ids_to_delete = [(4,), (3,)]
delete_multiple_records(ids_to_delete)

'''
Після з'єднання з базою даних SQLite готується SQL-запит із параметрами та одним заповнювачем. Разом з ним також
передається список id у форматі кортежу.
Кожен елемент списку — це лише кортеж кожного рядка. Кожен кортеж містить ID розробника. У цьому прикладі
три кортежі — тобто три розробники.
Далі викликається cursor.executemany(sqlite_delete_query, ids_list) видалення кількох записів з таблиці. І
запит, і список id передаються cursor.executemany() як аргументи.
Щоб побачити кількість порушених записів, можна використати метод cursor.rowcount. Зрештою, зміни зберігаються
до бази даних за допомогою методу commit класу Connection.
'''