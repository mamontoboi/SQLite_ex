"""
---------------Отримання зображення та файлу, збережених у вигляді BLOB-------------

Припустимо, дані, які зберігаються у вигляді BLOB у базі даних, потрібно отримати, записати у файл на диску та відкрити
у звичному вигляді.

Для цього потрібно зробити наступні кроки:
* Встановити SQLite-з'єднання з базою даних із Python;
* Створити об'єкт cursor з об'єкта з'єднання;
* Створити SELECT-запит для отримання BLOB-колонок із таблиці;
* Використовувати cursor.fetchall() для отримання всіх рядків та перебору по них;
* Створити функцію для конвертації BLOB-даних у потрібний формат та записати готові файли на диск;
* Закрити об'єкт cursor та з'єднання.
"""

import sqlite3
import os


def write_to_file(data, filename):
    # Перетворення двійкових даних у потрібний формат
    with open(filename, 'wb') as file:
        file.write(data)  # saves in byte-like format still. Bad for text
    print("Дані з blob збережені у: ", filename, "\n")


def read_blob_data(emp_id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Підключений до SQLite")

        sql_fetch_blob_query = """SELECT * FROM new_employee WHERE id = ?"""
        cursor.execute(sql_fetch_blob_query, (emp_id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name = row[1]
            photo = row[2]
            resume_file = row[3]

            print("Збереження зображення співробітника та резюме на диску\n")
            photo_path = os.path.join("db_data", name + ".jpg")
            resume_path = os.path.join("db_data", name + "_resume.txt")
            write_to_file(photo, photo_path)
            write_to_file(resume_file, resume_path)
        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрито")


read_blob_data(1)
read_blob_data(2)

'''
Зображення та файли справді збереглися на диску.

Отримання зображення та файлу, збережених у вигляді BLOB
Примітка: для копіювання бінарних даних на диск вони спочатку мають бути конвертовані у потрібний формат.
У цьому прикладі форматами були .jpg та .txt.
'''