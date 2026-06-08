import streamlit as st
from ui_helpers import format_price, get_available_text

def build_food_table_data(foods):
    food_data = []

    for food in foods:
        available = get_available_text(food.available)
                
        food_data.append({
            "ID": food.id,
            "Tên món": food.name,
            "Giá bán": format_price(food.price),
            "Loại món": food.category,
            "Trạng thái": available 
        })
    return food_data

def show_food_table(display_foods):
    st.write("Danh sách món ăn:")
    st.write(f"Đang hiển thị: {len(display_foods)} món")

    if len(display_foods) == 0:
        st.info("Không có món phù hợp với bộ lọc hiện tại.")
    else:
        food_data = build_food_table_data(display_foods)
        st.table(food_data)