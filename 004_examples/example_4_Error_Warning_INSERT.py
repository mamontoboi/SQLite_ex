"""
sqlite3.Warning. Підклас Exception. Його можна ігнорувати, якщо потрібно, щоб воно не зупиняло виконання.
sqlite3.Error. Базовий клас інших винятків модуля sqlite3. Підклас Exception.
sqlite3.DatabaseError. Виняток, який повертається при помилках бази даних. Наприклад, якщо спробувати відкрити файл
як базу sqite3, хоча він не є, то повернеться помилка «sqlite3.DatabaseError: file is encrypted or is not a
database».
sqlite3.IntegrityError. Підклас DatabaseError. Ця помилка повертається, коли стосуються відносини в базі,
наприклад, наприклад, не відбувається перевірка зовнішнього ключа.
sqlite3.ProgrammingError. Підклас DatabaseError. Ця помилка виникає через помилки програміста: створення таблиці з
ім'ям, яке вже зайняте, синтаксична помилка у SQL-запитах.
sqlite3.OperationalError. Підклас DatabaseError. Цю помилку неможливо контролювати. Вона з'являється у ситуаціях,
які стосуються роботи бази даних, наприклад, обрив з'єднання, непрацюючий сервер, проблеми з джерелом даних та
так далі.
sqlite3.NotSupportedError. Цей виняток з'являється під час спроби використовувати непідтримувану базу даних API.
Приклад: виклик методу rollback() для з'єднання, яке не підтримує транзакцію. Виклик комміту після команди
створення таблиці.
Таким чином, рекомендується завжди писати код управління базою даних у блоці try, щоб була можливість перехоплювати
винятки та вживати дій, які допоможуть впоратися з ними.
"""

import sqlite3
import traceback
import sys

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("База даних підключена до SQLite")

    sqlite_insert_query = """INSERT INTO unknown_table_1
                          (id, text)  VALUES  (1, 'Демо текст')"""

    count = cursor.execute(sqlite_insert_query)
    sqlite_connection.commit()
    print("Запис успішно вставлено до таблиці sqlitedb_developers ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Неможливо вставити дані в таблицю sqlite")
    print("Клас виключення: ", error.__class__)
    print("Виключення", error.args)
    print("Друк подробиць виключення SQLite: ")
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("З'єднання з SQLite закрито")
