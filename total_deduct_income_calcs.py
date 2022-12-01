# Завдання 4
# Створіть агрегатні функції для підрахунку загальної кількості  витрат i прибуткiв за місяць.
# Забезпечте відповідний інтерфейс користувача.

import sqlite3


def total_income():
    return f"""SELECT * FROM profits_and_deductions
            WHERE amount > 0 AND strftime('%m', time) = ?"""


def total_deductions():
    return f"""SELECT * FROM profits_and_deductions
            WHERE amount < 0 AND strftime('%m', time) = ?"""


def summary(sign):
    try:
        sqlite_connect = sqlite3.connect('monefy.db')
        cursor = sqlite_connect.cursor()

        month = input("Write number of the month you'd like to check your statistics for: \n")

        if sign == '+':
            cursor.execute(total_income(), (month,))
        else:
            cursor.execute(total_deductions(), (month,))

        results = cursor.fetchall()
        total = 0
        for i in results:
            total += i[2]

        if sign == "+":
            print(f"The total monthly income equals to {total} dineros.")
        else:
            print(f"The total monthly spending was {abs(total)} dineros.")

        sqlite_connect.close()

    except sqlite3.Error as e:
        print(f"The following exception was encountered: {e}\n")
    finally:
        if sqlite_connect:
            sqlite_connect.close()

