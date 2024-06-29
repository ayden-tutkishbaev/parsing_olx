import sqlite3


def create_categories_table():
    database = sqlite3.connect('goods_database.db')
    cursor = database.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories(
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_title TEXT UNIQUE
    )
    """)
    database.commit()
    database.close()


def create_goods_table():
    database = sqlite3.connect('goods_database.db')
    cursor = database.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS goods(
        good_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER REFERENCES categories(category_id),
        good_title TEXT UNIQUE,
        good_link TEXT,
        good_price TEXT,
        good_location TEXT
    )
    """)
    database.commit()
    database.close()


def save_category(category_title):
    database = sqlite3.connect('goods_database.db')
    cursor = database.cursor()
    cursor.execute("""
    INSERT INTO categories(category_title) VALUES (?) 
    ON CONFLICT DO NOTHING
    """, (category_title, ))
    database.commit()
    database.close()

def get_category_id(category_title):
    database = sqlite3.connect('goods_database.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT category_id FROM categories WHERE category_title = ?
    ''', (category_title, ))
    category_id = cursor.fetchone()[0]  # (1, ) -> 1
    return category_id


def save_good(category_id, good_title, good_link, good_price, good_location):
    database = sqlite3.connect('goods_database.db')
    cursor = database.cursor()
    cursor.execute("""
    INSERT INTO goods(category_id, good_title, good_link, good_price, good_location)
    VALUES (?,?,?,?,?) ON CONFLICT DO NOTHING
    """, (category_id, good_title, good_link, good_price, good_location))
    database.commit()
    database.close()