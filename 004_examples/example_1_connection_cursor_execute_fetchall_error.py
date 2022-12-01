# Створення файлу бази даних sqlite_python.db та виведення подробиць про версію SQLite

# Підключаємо модуль sqlite3
import sqlite3

try:
    # За допомогою методу connect() виконується підключення до бази даних. Цей метод повертає об'єкт SQLite
    # Метод connect() приймає різні аргументи. У цьому прикладі передається назва бази даних
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    # Об'єкт connection не є безпечним. Модуль sqlite3 не дозволяє ділитися з'єднанням між потоками.
    # Якщо спробувати це зробити, можна отримати виняток
    # За допомогою об'єкта з'єднання створюється об'єкт cursor, який дозволяє виконувати SQLite запити з Python.
    # Для одного з'єднання можна створити необмежену кількість cursor. Він також не є безпечним.
    # Модуль не дозволяє ділитися об'єктами cursor між потоками. Якщо це зробити, буде помилка.
    cursor = sqlite_connection.cursor()
    print("База даних створена та успішно підключена до SQLite")

    sqlite_select_query = "select sqlite_version();"
    # Створення запиту на отримання версії бази даних
    # За допомогою методу execute об'єкта cursor можна виконати запит до бази даних із Python. Він приймає
    # SQLite-запит як параметр і повертає resultSet - тобто, рядки бази даних
    cursor.execute(sqlite_select_query)
    # Отримання результату запиту з resultSet можна за допомогою методу fetchAll()
    record = cursor.fetchall()  # fetchall returns list. fetchone returns one value
    print("Версія бази даних SQLite: ", record)  # Версія бази даних SQLite:  [('3.38.4',)]
    # Хорошою практикою вважається закривати об'єкти connection і cursor після завершення роботи, щоб уникнути
    # проблем із базою даних:
    cursor.close()

# За допомогою класу sqlite3.Error можна обробити будь-яку помилку та виняток, які можуть з'явитися під час роботи
# з SQLite з Python. Це дозволить зробити програму більш стійкою до відмови. Клас sqlite3.Error дозволить зрозуміти
# суть помилки. Він повертає повідомлення та код помилки.
except sqlite3.Error as error:
    print("Помилка при підключенні до sqlite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("З'єднання з SQLite закрито")
