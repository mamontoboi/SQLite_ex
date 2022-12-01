# Створення таблиці – це DDL-запит, який виконується з Python
# Створимо базу sqlitedb_developers у базі даних sqlite_python.db

import sqlite3

try:
    # Поєднуємося з БД
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    # Готуємо запит на створення таблиці
    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS sqlitedb_developers (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                email text NOT NULL UNIQUE,
                                joining_date datetime,
                                salary REAL NOT NULL);'''

    cursor = sqlite_connection.cursor()
    print("База даних підключена до SQLite")
    # Виконуємо запит за допомогою cursor.execute(query)
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблиця SQLite створена")
    # Закриваємо з'єднання з базою та об'єктом cursor
    cursor.close()

except sqlite3.Error as error:
    print("Помилка при підключенні до sqlite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("З'єднання з SQLite закрито")

'''
Перед переходом до виконання CRUD-операцій у SQLite з Python спочатку потрібно розібратися з типами даних SQLite та
відповідними їм типами даних у Python, які допомагають зберігати та зчитувати дані з таблиці.
У движка SQLite є кілька класів для зберігання значень. Кожне значення, що зберігається в базі даних, має один з
наступних типів чи класів.

NULL – значення NULL
INTEGER – числові значення. Цілі числа зберігаються в 1, 2, 3, 4, 6 та 8 байтах залежно від величини
REAL - числа з плаваючою точкою, наприклад, 3.14, число Пі
TEXT – текстові значення. Можуть зберігатися у кодуванні UTF-8, UTF-16BE або UTF-16LE
BLOB – бінарні дані. Для зберігання зображень та файлів
Наступні типи даних з Python без проблем конвертуються в SQLite. Для конвертації достатньо лише запам'ятати цю таблицю.

Тип Python - Тип SQLite
None - NULL
int - INTEGER
float - REAL
str	- TEXT
bytes - BLOB
'''

