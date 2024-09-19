import sqlite3
import pprint


def initiate_db():
    with sqlite3.connect("initiate.db") as connection:
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            price INTEGER NOT NULL,
            image_path TEXT NOT NULL
        )''')

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS Users(
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    balance INTEGER NOT NULL
                )''')


def fill_products():
    with sqlite3.connect("initiate.db") as connection:
        cursor = connection.cursor()
        for i in range(1, 11):
            cursor.execute("INSERT INTO Products (title, description, price, image_path) VALUES (?, ?, ?, ?)",
                           (f"Название: Продукт{i}", f"Описание: {i * 100} г", i * 100, f"images/{i}.jpg"))


def get_all_products():
    with sqlite3.connect("initiate.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Products")
        data = cursor.fetchall()
    return data


def is_included(username: str):
    with sqlite3.connect("initiate.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
        user = cursor.fetchone()
    return bool(user)


def add_user(username: str, email: str, age: int):
    with sqlite3.connect("initiate.db") as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)", (username, email, age))
        print(username, email, age)


if __name__ == "__main__":
    initiate_db()
    data = get_all_products()
    if not data:
        fill_products()
    pprint.pprint(data)