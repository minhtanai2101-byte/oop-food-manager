import sqlite3
from food import Food
from config import DATABASE_FILE
def create_table():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS foods (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        category TEXT,
        available INTEGER)
                """)
    connection.commit()
    connection.close()

def insert_food(food):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO foods (id, name, price, category, available)
    VALUES (?, ? ,? ,? ,?)
    """, (
        food.id,
        food.name,
        food.price,
        food.category,
        int(food.available)
    ))
    connection.commit()
    connection.close()

def get_all_foods():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM foods")
    rows = cursor.fetchall()

    connection.close()

    foods = []

    for row in rows:
        food_id, name, price, category, available = row
        food = Food(food_id, name, price, category, bool(available))
        foods.append(food)
    return foods

def update_food_price_in_db(food_id, new_price):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE foods
    SET price = ?
    WHERE id = ?
    """, (new_price, food_id))

    connection.commit()
    connection.close()

def update_food_available_in_db(food_id, new_available):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE foods
    set available = ?
    WHERE id = ?
    """, (int(new_available), food_id))

    connection.commit()
    connection.close()

def delete_food(food_id):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor. execute("""
    DELETE FROM foods
    WHERE id = ?
    """, (food_id,))

    connection.commit()
    connection.close()