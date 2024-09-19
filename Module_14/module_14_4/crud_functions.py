import sqlite3
import pprint

with sqlite3.connect("initiate.db") as connection:
    cursor = connection.cursor()


    def initiate_db():
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            price INTEGER NOT NULL,
            image_path TEXT NOT NULL
        )''')


    def fill_db():
        for i in range(1, 11):
            cursor.execute("INSERT INTO Products (title, description, price, image_path) VALUES (?, ?, ?, ?)",
                           (f"Название: Продукт{i}", f"Описание: {i * 100} г", i * 100, f"images/{i}.jpg"))


    def get_all_products():
        cursor.execute("SELECT * FROM Products")
        data = cursor.fetchall()
        return data


    if __name__ == "__main__":
        initiate_db()
        data = get_all_products()
        if not data:
            fill_db()
        pprint.pprint(data)