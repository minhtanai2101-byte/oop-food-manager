import streamlit as st
from config import FOOD_CATEGORIES
from app_validators import validate_new_food
from ui_helpers import get_available_text
from app_handlers import (handle_delete_food,
                          handle_update_food_available,
                          handle_update_food_price)
from database import insert_food
from food import Food

def show_add_food_section(foods):
    with st.expander("Thêm món mới"):
        name = st.text_input("Tên món")
        price = st.number_input("Giá món", min_value=0, step=1000)
        category = st.selectbox("Loại món", FOOD_CATEGORIES)
        available = st.checkbox("Còn bán", value=True)

        if st.button("Thêm món"):
            error = validate_new_food(name, price, foods)

            if error != "":
                st.error(error)
            else:
                new_food = Food(None, name.strip(), price, category, available)
                insert_food(new_food)

                st.session_state["success_message"] = "Thêm món thành công!"

                st.rerun()

def show_delete_food_section(foods):
    with st.expander("Xóa món"):
        if len(foods) == 0:
            st.warning("Chưa có món nào để xóa")
        else:
            selected_food = st.selectbox(
                "Chọn món cần xóa",
                foods,
                format_func=lambda food: food.name,
                key="select_food_for_delete"
            )

            if st.button("Xóa món"):
                handle_delete_food(selected_food)

def show_update_price_section(foods):
    with st.expander("Sửa giá món"):
        if len(foods) == 0:
            st.warning("Chưa có món nào để sửa giá")
        else:
            selected_food_for_price = st.selectbox(
                "Chọn món cần sửa giá",
                foods,
                format_func=lambda food: food.name,
                key="select_food_for_price"
            )

            new_price = st.number_input("Giá mới", min_value=0, step=1000)

            if st.button("Cập nhật giá"):
                handle_update_food_price(selected_food_for_price, new_price)

def show_update_available_section(foods):
    with st.expander("Sửa trạng thái món"):
        if len(foods) == 0:
            st.warning("Chưa có món nào để sửa trạng thái")
        else:
            selected_food_for_available = st.selectbox("Chọn món cần sửa trạng thái",
                foods, format_func=lambda food: food.name,
                key="select_food_for_available")
            current_status = get_available_text(selected_food_for_available.available)
            st.write("Trạng thái hiện tại:", current_status)
            new_available = st.checkbox("Còn bán",
                value=selected_food_for_available.available,
                key="checkbox_available")
            
            if st.button("Cập nhật trạng thái"):
                handle_update_food_available(selected_food_for_available, new_available)