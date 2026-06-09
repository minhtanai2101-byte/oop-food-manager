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
    INSERT INTO foods (name, price, category, available)
    VALUES (?, ? ,? ,?)
    """, (
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

def update_food_name_in_db(food_id, new_name):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute("""
    UPDATE foods
    SET name = ?
    WHERE id = ?
    """, (new_name, food_id))
    connection.commit()
    connection.close()

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

def update_food_category_in_db(food_id, new_category):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute("""
    UPDATE foods
    SET category = ?
    WHERE id = ?
    """, (new_category, food_id))
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

def seed_sample_data():
    foods = get_all_foods()
    if len(foods) == 0:
        food1 = Food(None,"Phở bò", 40000, "Món nước", True)
        food2 = Food(None,"Cơm gà", 35000, "Món cơm", True)
        food3 = Food(None,"Trà đào",25000, "Đồ uống", True)
        insert_food(food1)
        insert_food(food2)
        insert_food(food3)