from food import Food
from config import DATA_FILE
from input_helpers import (
    input_required_text,
    input_available,
    input_positive_int
)

def handle_add_food(manager):
    name = input_required_text("Nhập tên món: ", "Tên món không được để trống")
    if name is None:
        return
    price = input_positive_int("Nhập giá: ")
    if price is None:
        return
    category = input_required_text("Nhập loại món: ","Loại món không được để trống")
    if category is None:
        return
    available = input_available("Món còn bán hay hết bán: ")
    if available is None:
        return
    new_food = Food(name, price, category, available)
    if manager.add_food(new_food):
        manager.save_to_json(DATA_FILE)
        print("Đã thêm món và lưu dữ liệu")
    else:
        print("Món bạn nhập đã có trong danh sách từ trước")

def handle_find_food(manager):
    food_name = input("Nhập tên món muốn tìm: ").strip()
    result = manager.find_food(food_name)
    if result is None:
        print("Không tìm thấy món này")
    else:
        print("Món bạn cần tìm:")
        result.show_info()

def handle_remove_food(manager):
    food_name = input("Nhập tên món muốn xóa: ").strip()
    if manager.remove_food(food_name):
        manager.save_to_json(DATA_FILE)
        print("Đã xóa món và lưu dữ liệu")
    else:
        print("Không tìm thấy món muốn xóa")

def handle_update_food_price(manager):
    food_name = input("Nhập tên món muốn sửa giá: ").strip()
    new_price = input_positive_int("Nhập giá: ")
    if new_price is None:
        return
    if manager.update_food_price(food_name, new_price):
        manager.save_to_json(DATA_FILE)
        print("Đã sửa giá món và lưu vào dữ liệu")
    else:
        print("Không tìm thấy món muốn sửa giá")

def handle_update_food_available(manager):
    food_name = input("Nhập tên món muốn sửa trạng thái: ").strip()
    new_available = input_available("Nhập trạng thái còn bán hay hết bán: ").strip()
    if new_available is None:
        return
   
    if manager.update_food_available(food_name, new_available):
        manager.save_to_json(DATA_FILE)
        print("Đã sửa trạng thái món và lưu vào dữ liệu")
    else:
        print("Không tìm thấy món muốn sửa trạng thái")

def handle_filter_by_category(manager):
    category = input("Nhập loại món muốn lọc: ").strip()
    result = manager.filter_by_category(category)
    if len(result) == 0:
        print("Không có loại món phù hợp")
    else:
        print(f"Danh sách {category}:")
        for food in result:
            food.show_info()
            print("-" *20)

def handle_filter_by_available(manager):
    answer = input("Nhập trạng thái muốn lọc còn bán hay hết bán: ")
    if answer.lower() == "còn bán":
        available = True
    elif answer.lower() == "hết bán":
        available = False
    else:
        print("Chỉ nhập còn bán hoặc hết bán")
        return
    result = manager.filter_by_available(available)
    if len(result) == 0:
        print("Không có món nào phù hợp")
    else:
        for food in result:
            food.show_info()
            print("-" *20)

def handle_sort_foods(manager):
    sort_by = input("Tiêu chí sắp xếp tên hay giá: ").strip()
    answer = input("Sắp xếp tăng hay giảm: ").strip()
    if answer.lower() == "tăng":
        reverse = False
    elif answer.lower() == "giảm":
        reverse = True
    else:
        print("Chỉ nhập tăng hoặc giảm")
        return
    if manager.sort_foods(sort_by, reverse):
        print("Đã sắp xếp thành công")
        manager.show_all_foods()
    else:
        print("Chỉ nhập tên hoặc giá")
