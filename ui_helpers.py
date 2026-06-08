def get_available_text(available):
    if available == True:
        return "Còn bán"
    else:
        return "Hết bán"

def format_price(price):
    return f"{price:,.0f} VNĐ"