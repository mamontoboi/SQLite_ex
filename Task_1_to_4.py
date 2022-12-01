# Завдання 1
# Зробіть таблицю для підрахунку особистих витрат із такими полями: id, призначення, сума, час.
#
# Завдання 2
# Створіть консольний інтерфейс (CLI) на Python для додавання нових записів до бази даних.
#
# Завдання 3
# Змініть таблицю так, щоби можна було додати не лише витрати, а й прибутки.
#
# Завдання 4
# Створіть агрегатні функції для підрахунку загальної кількості  витрат i прибуткiв за місяць.
# Забезпечте відповідний інтерфейс користувача.

import sqlite3
from income import income
from deductions import deductions
from total_deduct_income_calcs import summary


def create_new_db():
    try:
        sqlite_connection = sqlite3.connect('monefy.db')
        cursor = sqlite_connection.cursor()

        sqlite_query = """CREATE TABLE profits_and_deductions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        purpose TEXT NOT NULL,
        amount FLOAT NOT NULL,
        time timestamp);"""

        cursor.execute(sqlite_query)

        sqlite_connection.commit()
        print("The database was successfully created.\n")

    except sqlite3.Error as e:
        print("The database cannot be created.")
        print(f"The following problem has occurred: {e}")

    finally:
        if sqlite_connection:
            sqlite_connection.close()


if __name__ == '__main__':
    while True:
        quest = input("""
        What do you to do:
        1 - Create a new expenses database
        2 - Record an income
        3 - Make a deduction
        4 - Total income per month
        5 - Total deductions per month
        6 - Exit the programme\n
        """)
        match quest:
            case '1':
                create_new_db()
            case '2':
                amount = float(input("Sum: "))
                purpose = input("Purpose: ")
                income(purpose=purpose, amount=amount)
            case '3':
                amount = float(input("Sum: "))
                purpose = input("Purpose: ")
                deductions(purpose=purpose, amount=amount)
            case '4':
                summary('+')
            case '5':
                summary('-')
            case '6':
                print("Thank you for choosing our software!")
                break
            case _:
                print("You must choose from the menu above.")
                continue



