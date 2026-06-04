import json
from food import Food

class FoodManager:
    def __init__(self):
        self.foods = []
    
    def add_food(self, food):
        result = self.find_food(food.name)
        if result == None:
            self.foods.append(food)
            return True
        else:
            return False
                  
    def show_all_foods(self):
        for i, food in enumerate(self.foods, start=1):
            print(f"{i}.")
            food.show_info()
            print("-"  * 20)
    
    def find_food(self, food_name):
        food_name = food_name.strip().lower()
        for food in self.foods:
            if food.name.strip().lower() == food_name:
                return food
        return None
    
    def remove_food(self, food_name):
        result = self.find_food(food_name)
        if result is None:
            return False
        else:
            self.foods.remove(result)
            return True

    def filter_by_category(self, category):
        result = []
        for food in self.foods:
            if food.category.lower() == category.lower():
                result.append(food)
        return result
    
    def filter_by_available(self, available):
        result = []
        for food in self.foods:
            if food.available == available:
                result.append(food)
        return result
    
    def sort_foods(self, sort_by, reverse=False):
        if sort_by.lower() == "tên":
            self.foods.sort(key=lambda food: food.name, reverse=reverse)
            return True
        elif sort_by.lower() == "giá":
            self.foods.sort(key=lambda food: food.price, reverse=reverse)
            return True
        else:
            return False
    
    def update_food_price(self, food_name, new_price):
        result = self.find_food(food_name)
        if result is None:
            return False
        else:
            result.update_price(new_price)
            return True
    
    def update_food_available(self, food_name, new_available):
        result = self.find_food(food_name)
        if result is None:
            return False
        else:
            result.update_available(new_available)
            return True
    
    def to_dicts(self):
        result = []
        for food in self.foods:
            food_dict = food.to_dict()
            result.append(food_dict)
        return result
    
    def save_to_json(self, file_name):
        food_dicts = self.to_dicts()
        
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(food_dicts, file, ensure_ascii=False, indent=4)

    def load_from_json(self, file_name):
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                food_dicts = json.load(file)
            
            self.foods = []

            for food_dict in food_dicts:
                food = Food.from_dict(food_dict)
                self.foods.append(food)
            return True
        except FileNotFoundError:
            print("Chưa có file dữ liệu")
            self.foods = []
            return False
        except json.JSONDecodeError:
            print("File dữ liệu bị lỗi")
            self.foods = []
            return False
        
    def filter_by_price_range(self, min_price, max_price):
        result = []
        for food in self.foods:
            if min_price <= food.price <= max_price:
                result.append(food)
        return result

