"""
---------------Створення або перевизначення SQL-функцій у SQLite---------------

У таких базах даних, як MySQL, MSSQL і PostgreSQL, є можливість створювати функції і процедури, що зберігаються, але у
SQLite такої можливості немає. Таким чином, CREATE FUNCTION та CREATE PROCEDURE з цією базою даних не працюватимуть.
У цьому матеріалі розглянемо, як створювати чи перевикористовувати SQL-функції з Python.

C API бази даних SQLite дає можливість створювати функції користувача або перевизначати поведінку існуючих.
Модуль sqlite3 - це лише оболонка для цього C API, яка надає можливість створювати або перевизначати
SQLite-функції з Python.

У певних випадках виникає необхідність здійснювати певні речі під час виконання SQL-запиту, особливо, якщо
це оновлення чи отримання даних. У таких випадках на допомогу приходять функції користувача. Наприклад, при
отримання імені користувача потрібно, щоб воно повернулося у верхньому регістрі.

У SQLite є безліч вбудованих функцій: LENGTH, LOWER, UPPER, SUBSTR, REPLACE та інші. Додамо до цього списку TOTITLE
для конвертації будь-якого рядка і в рядок із великими літерами.

Функція приймає три аргументи:

name - ім'я функції
num_params – кількість параметрів, які функція приймає
func — функція Python, яка викликається всередині запиту
Ця функція створює функцію користувача, яку можна використовувати в інструкціях SQL, посилаючись на її name.

Примітка: якщо в якості параметра num_params передати значення -1, то функція прийматиме будь-яку кількість
аргументів. connection.create_function() може повертати будь-які типи, що підтримуються SQLite: bytes, str, int, float та
None.

Створимо нову функцію SQLite за допомогою connection.create_function().
"""

import sqlite3


# Приймає рядок як вхідне значення і конвертує його в рядок із великими літерами
def _to_title_case(string):
    return str(string).title()


def get_developer_name(dev_id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Підключений до SQLite")
        # Після цього викликається create_function із класу connection. У неї передаються три аргументи: назва функції,
        # кількість параметрів, які прийматиме _to_title_case та функція Python, яка буде викликатися як
        # SQL-функція.
        # Після цього функція TOTITLECASE викликається у запиті SELECT для отримання імені розробника у вигляді рядка з
        # великими літерами
        sqlite_connection.create_function("TOTILECASE", 1, _to_title_case)
        select_query = "SELECT TOTILECASE(name) FROM sqlitedb_developers WHERE id = ?"
        cursor.execute(select_query, (dev_id,))
        name = cursor.fetchone()
        print("Ім'я розробника", name)
        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі зSQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрито")


get_developer_name(2)
