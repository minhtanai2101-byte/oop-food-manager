import streamlit as st

def get_food_stats(foods):
    total_foods = len(foods)
    available_count = 0
    unavailable_count = 0
    total_price = 0
    for food in foods:
        if food.available == True:
            available_count += 1
        else:
            unavailable_count += 1
        total_price += food.price
    if total_foods > 0:
        average_price = total_price / total_foods
    else:
        average_price = 0
    return total_foods, available_count, unavailable_count, average_price

def show_food_stats(foods):
    total_foods, available_count, unavailable_count, average_price = get_food_stats(foods)

    st.subheader("Thống kê nhanh")

    stats_col, empty_col = st.columns([2, 1])

    with stats_col:
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Tổng số món", total_foods)
        col2.metric("Món còn bán", available_count)
        col3.metric("Món hết bán", unavailable_count)
        col4.metric("Giá trung bình (VNĐ)", f"{average_price:,.0f}")