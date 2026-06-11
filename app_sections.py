import streamlit as st
from config import FOOD_CATEGORIES
from app_validators import validate_new_food
from ui_helpers import get_available_text
from app_handlers import (handle_delete_food,
                          handle_update_food_available,
                          handle_update_food_price,
                          handle_update_food_name,
                          handle_update_food_category)
from database import insert_food
from food import Food

def show_add_food_section(foods):
    with st.expander("Thêm món mới"):
        with st.form("add_food_form"):
            name = st.text_input("Tên món")
            price = st.number_input("Giá món", min_value=0, step=1000)
            category = st.selectbox("Loại món", FOOD_CATEGORIES)
            available = st.checkbox("Còn bán", value=True)

            submitted = st.form_submit_button("Thêm món")
            if submitted:
                error = validate_new_food(name, price, foods)

                if error != "":
                    st.error(error)
                else:
                    new_food = Food(None, name.strip(), price, category, available)
                    insert_food(new_food)
                    st.cache_data.clear()
                    st.session_state["success_message"] = "Thêm món thành công!"

                    st.rerun()

def show_delete_food_section(foods):
    with st.expander("Xóa món"):
        if len(foods) == 0:
            st.warning("Chưa có món nào để xóa")
        else:
            with st.form("delelte_food_form"):
                selected_food = st.selectbox(
                    "Chọn món cần xóa",
                    foods,
                    format_func=lambda food: food.name,
                    key="select_food_for_delete"
                )
                st.warning("Thao tác này sẽ xóa món khỏi database.")
                confirm_delete = st.checkbox("Tôi chắc chắn muốn xóa món này", key="confirm_delete")
                submitted = st.form_submit_button("Xóa món")
                if submitted:
                    if confirm_delete == False:
                        st.error("Bạn cần xác nhận trước khi xóa")
                    else:
                        handle_delete_food(selected_food)

def show_update_price_section(foods):
    with st.expander("Sửa giá món"):
        if len(foods) == 0:
            st.warning("Chưa có món nào để sửa giá")
        else:
            with st.form("update_price_form"):
                selected_food_for_price = st.selectbox(
                "Chọn món cần sửa giá",
                foods,
                format_func=lambda food: food.name,
                key="select_food_for_price"
                )

                new_price = st.number_input("Giá mới", min_value=0, step=1000)
                submitted = st.form_submit_button("Sửa giá món") 
                if submitted:
                    handle_update_food_price(selected_food_for_price, new_price)

def show_update_available_section(foods):
    with st.expander("Sửa trạng thái món"):
        if len(foods) == 0:
            st.warning("Chưa có món nào để sửa trạng thái")
        else:
            with st.form("Update_available_form"):
                selected_food_for_available = st.selectbox("Chọn món cần sửa trạng thái",
                    foods, format_func=lambda food: food.name,
                    key="select_food_for_available")
                current_status = get_available_text(selected_food_for_available.available)
                st.write("Trạng thái hiện tại:", current_status)
                new_available = st.checkbox("Còn bán",
                    value=selected_food_for_available.available,
                    key="checkbox_available")
                submitted = st.form_submit_button("Cập nhật trạng thái")
                if submitted:
                    handle_update_food_available(selected_food_for_available, new_available)

def show_update_name_section(foods):
    with st.expander("Sửa tên món"):
        if len(foods) == 0:
            st.warning("Chưa có món nào để sửa tên")
        else:
            with st.form("update_name_form"):
                selected_food_for_name = st.selectbox("Chọn món cần sửa tên",
                    foods, format_func=lambda food: food.name,
                    key="select_food_for_name")
                new_name = st.text_input("Tên mới")
                submitted = st.form_submit_button("Cập nhật tên mới")
                if submitted:
                    handle_update_food_name(selected_food_for_name.id, new_name, foods)

def show_update_category_section(foods):
    with st.expander("Sửa loại món"):
        if len(foods) == 0:
            st.warning("Chưa có món nào để sửa loại món")
        else:
            with st.form("update_category_form"):
                selected_food_for_category = st.selectbox("Chọn món cần sửa loại món",
                    foods, format_func=lambda food: food.name,
                    key="select_food_for_category")
                new_category = st.selectbox("Loại mới",FOOD_CATEGORIES, key="select_new_category")
                submitted = st.form_submit_button("Cập nhật loại món mới")
                if submitted:
                    handle_update_food_category(selected_food_for_category.id, new_category)