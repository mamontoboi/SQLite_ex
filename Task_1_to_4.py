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


def found_all(num):
    try:
        sqlite_connection = sqlite3.connect('monefy.db')
        cursor = sqlite_connection.cursor()

        sql_query = """SELECT * FROM profits_and_deductions WHERE amount >= :num;"""
        data = {'num': num}
        cursor.execute(sql_query, data)
        print(cursor.fetchall())

    except sqlite3.Error as e:
        print(f"The following exception has occurred: {e}")

    finally:
        if sqlite_connection:
            sqlite_connection.close()


def total_exps(month):
    try:
        sqlite_connection = sqlite3.connect('monefy.db')
        cursor = sqlite_connection.cursor()

        sql_query = """SELECT SUM(amount) FROM profits_and_deductions 
                        WHERE amount < 0 
                        AND strftime('%m', time)=:month;"""
        data = {'month': month}
        cursor.execute(sql_query, data)
        x = cursor.fetchone()
        print(f"The total amount of monthly expenses is {abs(x[0])} dineros.")

    except sqlite3.Error as e:
        print(f"The following exception has occurred: {e}")

    finally:
        if sqlite_connection:
            sqlite_connection.close()


def delete_entry(id):
    try:
        sqlite_connection = sqlite3.connect('monefy.db')
        cursor = sqlite_connection.cursor()

        sql_query = """DELETE FROM profits_and_deductions WHERE id=:id;"""
        data = {'id': id}
        cursor.execute(sql_query, data)
        sqlite_connection.commit()
        print(f"The entry No. {id} was successfully deleted.")

    except sqlite3.Error as e:
        print(f"The following exception has occurred: {e}")

    finally:
        if sqlite_connection:
            sqlite_connection.close()


def delete_table():
    try:
        sqlite_connection = sqlite3.connect('monefy.db')
        cursor = sqlite_connection.cursor()

        sql_query = """DROP TABLE profits_and_deductions;"""
        cursor.execute(sql_query)
        sqlite_connection.commit()
        print(f"The table was successfully deleted.")

    except sqlite3.Error as e:
        print(f"The following exception has occurred: {e}")

    finally:
        if sqlite_connection:
            sqlite_connection.close()


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
        6 - Delete entry
        7 - Found entries more than value
        8 - Delete table
        9 - Exit the programme\n
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
                total_exps(input('Write the number of the month:\n'))
            case '6':
                delete_entry(input('Write an id number of the entry you want to delete:\n'))
            case '7':
                found_all(input('Write the value all entries above what you want to see:\n'))
            case '8':
                delete_table()
            case '9':
                print("Thank you for choosing our software!")
                break
            case _:
                print("You must choose from the menu above.")
                continue



