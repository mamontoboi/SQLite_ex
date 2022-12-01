"""
Робота із зображеннями та файлами в SQLite

Як бінарні дані можуть виступати файли з будь-яким розширенням, зображення, відео або інші медіа;
BLOB-дані можна зчитувати з таблиці SQLite.
Перед виконанням операцій над BLOB-даними переконайтеся, що ви знаєте назву таблиці SQLite. Для зберігання цієї
інформації потрібно створити нову, або змінити існуючу, додавши колонку відповідного типу.

У цьому прикладі використовуватиметься таблиця new_employee. Її можна створити за допомогою наступного скрипту:

CREATE TABLE new_employee (id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL, resume BLOB NOT NULL);
Ця таблиця містить дві BLOB-колонки:

Колонка фото для зберігання зображення співробітника.
Колонка resume для зберігання файлу резюме.
Але варто також розібратися з тим, що таке BLOB.

BLOB (large binary object - "великий бінарний об'єкт") - це тип даних, який використовується для зберігання "важких"
файлів, таких як зображення, відео, музика, документи тощо. Перед збереженням у базі даних ці файли потрібні
конвертувати в бінарні дані, тобто масив байтів.

Додавання зображень та файлів у таблицю.
Вставимо зображення та резюме співробітника в таблицю new_employee. Для цього потрібно виконати такі кроки:
* Встановити SQLite-з'єднання з базою даних із Python;
* Створити об'єкт cursor із об'єкта з'єднання;
* Створити INSERT-запит. На цьому етапі потрібно знати назви таблиці та колонки, в яку виконуватиметься вставка;
* Створити функцію для перетворення цифрових даних (наприклад, зображень або файлів) в бінарні;
* Виконати запит INSERT за допомогою cursor.execute();
* Після успішного завершення операції закомітити збереження до бази даних;
* Закрити об'єкт cursor та з'єднання;
* Перехопити будь-які SQL-виключення.
"""
import sqlite3


def convert_to_binary_data(filename):
    # Перетворення даних на двійковий формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


def insert_blob(emp_id, name, photo, resume_file):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Підключений до SQLite")

        sqlite_insert_blob_query = """INSERT INTO new_employee
                                  (id, name, photo, resume) VALUES (?, ?, ?, ?)"""

        emp_photo = convert_to_binary_data(photo)
        resume = convert_to_binary_data(resume_file)
        # Перетворення даних у формат кортежу
        data_tuple = (emp_id, name, emp_photo, resume)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqlite_connection.commit()
        print("Зображення та файл успішно вставлені як BLOB у таблицю")
        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрито")


# Creation of new database in file 'sqlite_python.db'
try:
    # Поєднуємося з БД
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    # Готуємо запит на створення таблиці
    sqlite_create_table_query = '''CREATE TABLE new_employee (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL, 
    photo BLOB NOT NULL, 
    resume BLOB NOT NULL);'''

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


insert_blob(1, "Smith", "smith.jpg", "smith_resume.docx")
insert_blob(2, "David", "david.jpg", "david_resume.docx")

'''
У прикладі були вставлені id співробітника, ім'я, фото та файл з резюме. Для останніх двох було передано розташування
файлів, так що програма змогла рахувати їх і конвертувати в бінарні дані
Як можна явно побачити, зображення та файл конвертувалися у бінарний формат у процесі читання даних у режимі rb. І
тільки після цього дані були вставлені в стовпчик BLOB. Також було використано запит із параметрами для вставки
динамічних даних у таблиці.
'''