# Збереження резервної копії бази даних із Python
"""
Модуль sqlite3 в Python надає функцію для збереження резервної копії бази даних SQLite. За допомогою методу
connection.backup() можна створити резервну копію бази SQLite.

connection.backup(target, *, pages=0, progress=None, name="main", sleep=0.250)

Ця функція створює повну резервну копію бази даних SQLite. Зміни записуються в аргумент target, який має
бути екземпляром іншого з'єднання.

За умовчанням, коли параметр pages дорівнює 0 або негативному числу, вся база даних копіюється в один крок. В протилежному
У разі метод виконує цикл, копіюючи задану кількість сторінок за раз.

Аргумент name визначає базу даних, резервну копію якої необхідно зробити. Аргумент sleep - кількість секунд між
послідовними спробами зберегти сторінки, що залишилися. Аргумент sleep можна задати як цілого числа, так
і у вигляді числа з плаваючою точкою.
"""

import sqlite3


def progress(status, remaining, total):
    print(f'Скопійовано {total-remaining} з {total}...')


try:
    sqlite_con = sqlite3.connect('sqlite_python.db')
    backup_con = sqlite3.connect('sqlite_backup.db')
    with backup_con:
        sqlite_con.backup(backup_con, pages=3, progress=progress)  # pages=3 -- copying 3 element at the time, progress -- func above
    print("Резервне копіювання виконано успішно")

except sqlite3.Error as error:
    print("Помилка при резервному копіюванні: ", error)

finally:
    if backup_con:
        backup_con.close()
        sqlite_con.close()

'''
Після підключення до SQLite обидві бази даних було відкрито за допомогою двох різних підключень.
Далі виконується метод connection.backup() за допомогою екземпляра першого підключення. Також задано кількість сторінок,
які слід скопіювати за одну ітерацію.
'''