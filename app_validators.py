
def validate_new_food(name, price, foods):
    if name.strip() == "":
        return "Tên món không được để trống"
    if price <= 0:
        return "Giá phải lớn hơn 0"
    for food in foods:
        if food.name.strip().lower() == name.strip().lower():
            return "Tên món đã tồn tại"
    return ""

def validate_new_price(new_price):
    if new_price <= 0:
        return "Giá phải lớn hơn 0"
    return ""