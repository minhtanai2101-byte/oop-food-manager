def input_positive_int(message):
    try:
        number = int(input(message))
    except ValueError:
        print("Chỉ nhập số")
        return None
    if number <= 0:
        print("Giá phải lớn hơn 0")
        return None
    return number

def input_available(message):
    answer = input(message).strip()
    if answer.lower() == "còn bán":
        return True
    elif answer.lower() == "hết bán":
        return False
    else:
        print("Chỉ nhập còn bán hoặc hết bán")
        return None

def input_required_text(message, error_message):
    text = input(message).strip()
    if text == "":
        print(error_message)
        return None
    return text