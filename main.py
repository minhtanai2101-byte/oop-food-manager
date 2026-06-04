from food_manager import FoodManager
from config import DATA_FILE
from food_actions import (
    handle_add_food,
    handle_find_food,
    handle_filter_by_category,
    handle_remove_food,
    handle_filter_by_available,
    handle_sort_foods,
    handle_update_food_available,
    handle_update_food_price,
    handle_filter_by_price_range,
    handle_show_statistic
) 

def print_menu(menu):
    print("----MENU QUẢN LÝ MÓN ĂN----")
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item}")

def main():
    manager = FoodManager()
    manager.load_from_json(DATA_FILE)

    menu = ["Xem danh sách món",
            "Thêm món",
            "Tìm món",
            "Xóa món",
            "Sửa giá món",
            "Sửa trạng thái món",
            "Lọc theo loại món",
            "Lọc theo trạng thái",
            "Sắp xếp món",
            "Lọc theo khoảng giá",
            "Thống kê món ăn",
            "Thoát"]

    while True:
        print_menu(menu)

        try:
            choice = int(input("Bạn muốn chọn mục mấy: "))
        except ValueError:
            print("Chỉ nhập số")
            continue
            
        if choice not in range(1,13):
            print("Chỉ nhập số từ 1 đến 12")
        
        elif choice == 1:
            print("Danh sách món ăn")
            manager.show_all_foods()
        
        elif choice == 2:
            handle_add_food(manager) 
        
        elif choice == 3:
            handle_find_food(manager)
        
        elif choice == 4:
            handle_remove_food(manager)

        elif choice == 5:
            handle_update_food_price(manager)

        elif choice == 6:
            handle_update_food_available(manager)

        elif choice == 7:
            handle_filter_by_category(manager)
        
        elif choice == 8:
            handle_filter_by_available(manager)
        
        elif choice == 9:
            handle_sort_foods(manager)

        elif choice == 10:
            handle_filter_by_price_range(manager)
        
        elif choice == 11:
            handle_show_statistic(manager) 
        else:
            break

if __name__ == "__main__":
    main()

