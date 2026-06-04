class Food:
    def __init__(self, name, price, category, available):
        self.name = name
        self.price = price
        self.category = category
        self.available = available
    def show_info(self):
        print(f"Tên: {self.name}")
        print(f"Giá: {self.price}")
        print(f"Loại món: {self.category}")
        if self.available == True:
            print("Trạng thái: Còn bán")
        else: 
            print("Trạng thái: Hết bán")
    def update_price(self, new_price):
        self.price = new_price
    def update_available(self, new_available):
        self.available = new_available
    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "available": self.available
        }
    @staticmethod
    def from_dict(data):
        return Food(
            data["name"],
            data["price"],
            data["category"],
            data["available"]
        ) 
