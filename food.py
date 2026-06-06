class Food:
    def __init__(self, id, name, price, category, available):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.available = available
    def show_info(self):
        print(f"ID: {self.id}")
        print(f"Tên: {self.name}")
        print(f"Giá: {self.price}")
        print(f"Loại món: {self.category}")
        if self.available == True:
            print("Trạng thái: Còn bán")
        else: 
            print("Trạng thái: Hết bán")
    def update_price(self, new_price):
        if new_price <= 0:
            return False
        self.price = new_price
        return True

    def update_available(self, new_available):
        if type(new_available) != bool:
            return False
        self.available = new_available
        return True
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "available": self.available
        }
    @staticmethod
    def from_dict(data):
        return Food(
            data["id"],
            data["name"],
            data["price"],
            data["category"],
            data["available"]
        ) 
