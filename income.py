# Завдання 3
# Змініть таблицю так, щоби можна було додати не лише витрати, а й прибутки.

import sqlite3
import datetime


def income(purpose, amount):
    try:
        sqlite_connection = sqlite3.connect('monefy.db')
        cursor = sqlite_connection.cursor()

        sqlite_query = """INSERT INTO profits_and_deductions 
        (purpose, amount, time) VALUES (?, ?, ?);"""

        time_now = datetime.datetime.now()
        data = (purpose, amount, time_now.strftime('%Y-%m-%d %H:%M'))
        cursor.execute(sqlite_query, data)
        print(f"Entry was successfully added. The income of {amount} dineros received as {purpose} was recorded.\n")

        sqlite_connection.commit()

    except sqlite3.Error as e:
        print(f"The following exception has occurred: {e}.\n")

    finally:
        if sqlite_connection:
            sqlite_connection.close()

