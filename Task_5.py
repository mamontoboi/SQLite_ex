# Create an Exchange Rates To USD db using API Monobank (api.monobank.ua).
# Do requests via request lib, parse results, write it into db. (3 examples required)
# Example:
# Table - Exchange Rate To USD:
#
# id (INT PRIMARY KEY) - 1, 2, 3, ...
# currency_name (TEXT) - UAH
# currency_value (REAL) - 39.5
# current_date (DATETIME) - 10/22/2022 7:00 PM


import sqlite3
import requests
import json

# USD 840
# EUR 978
# UAH 980


def menu():
    while True:
        choice = input("""
        What do you want to do with database:
        1 to create database
        2 record exchange rate from USD into UAH
        3 record exchange rate from EUR into UAH
        4 to delete database
        5 for EXIT\n""")

        match choice:
            case '1':
                db_creation()
            case '2':
                db_insert("USD")
            case '3':
                db_insert("EUR")
            case '4':
                db_deletion()
            case '5':
                break
            case _:
                continue


def db_insert(name):
    response = requests.get("https://api.monobank.ua/bank/currency")
    response_date = response.headers["Date"]
    print(response_date)

    match name:
        case "USD":
            currency_name = 840
        case "EUR":
            currency_name = 978

    text_json = json.loads(response.text)
    print(text_json)

    for i in text_json:
        if i['currencyCodeA'] == currency_name and i['currencyCodeB'] == 980:
            currency_value = round(float(i["rateBuy"]), 3)

    try:
        sqlite_connect = sqlite3.connect('Task_5.db')
        cursor = sqlite_connect.cursor()

        data_tuple = (name, currency_value, response_date)
        print("The database was successfully connected.")

        sqlite_query = """INSERT INTO "Exchange rate to UAH"
        ("currency name", "currency value", datetime) VALUES (?, ?, ?);"""

        cursor.execute(sqlite_query, data_tuple)
        print(f"The entry of exchange rate from {name} into UAH was made.")

        sqlite_connect.commit()

    except sqlite3.Error as e:
        print(f"The following problem was encountered: {e}.\n")
    finally:
        if sqlite_connect:
            sqlite_connect.close()
        print("The database was closed.\n")


def db_creation():
    try:
        sqlite_connection = sqlite3.connect('Task_5.db')
        cursor = sqlite_connection.cursor()

        sql_query = """CREATE TABLE "Exchange rate to UAH" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        "currency name" TEXT NOT NULL,
        "currency value" REAL NOT NULL,
        datetime timestamp);"""

        cursor.execute(sql_query)
        print("The database was successfully created.\n")

        sqlite_connection.commit()

    except sqlite3.Error as e:
        print(f"The following problem was encountered: {e}.\n")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
        print("The database was closed.\n")


def db_deletion():
    try:
        sqlite_connection = sqlite3.connect('Task_5.db')
        cursor = sqlite_connection.cursor()

        sql_query = """DROP TABLE "Exchange rate to UAH";"""

        cursor.execute(sql_query)
        print("The database was successfully deleted.\n")

        sqlite_connection.commit()

    except sqlite3.Error as e:
        print(f"The following problem was encountered: {e}.\n")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
        print("The database was closed.\n")


if __name__ == '__main__':
    menu()
