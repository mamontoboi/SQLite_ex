# Виконання SQL запитів за допомогою функції executescript
"""
Скрипти SQLite чудово справляються зі стандартними завданнями. Це набір SQL-команд, збережених у файлі (у форматі .sql).
Один файл містить одну або більше SQL-операцій, які потім виконуються з командного рядка.

Далі кілька поширених сценаріїв використання SQL-скриптів

Створення резервних копій відразу кількох баз даних за один раз.
Порівняння кількості рядків двох різних баз із однією схемою.
Створення всіх таблиць в одному скрипті, що дозволить створити потрібну схему на сервері
Виконати скрипт із командного рядка SQLite можна за допомогою команди .read:

sqlite> .read sqlitescript.sql

CREATE TABLE fruits (
 id INTEGER PRIMARY KEY,
 name TEXT NOT NULL,
 price REAL NOT NULL
);

CREATE TABLE drinks (
 id INTEGER PRIMARY KEY,
 name TEXT NOT NULL,
 price REAL NOT NULL
);
"""

# Теж саме на Python:
import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("База даних підключена до SQLite")

    with open('sqlite_examples.sql', 'r') as sqlite_file:
        sql_script = sqlite_file.read()  # reading of the script 'sqlite_examples.sql'

    cursor.executescript(sql_script)  # execution of the script
    print("Скрипт SQLite успішно виконано")
    cursor.close()

except sqlite3.Error as error:
    print("Помилка при підключенні до sqlite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("З'єднання з SQLite закрито")
