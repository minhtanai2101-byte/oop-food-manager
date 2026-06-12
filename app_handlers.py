import streamlit as st
from database import (update_food_price_in_db,
                    update_food_available_in_db,
                    delete_food,
                    update_food_name_in_db,
                    update_food_category_in_db, update_food_in_db)
from app_validators import validate_new_price, validate_new_food_name, validate_update_food_name

def handle_update_food_price(selected_food, new_price):
    error = validate_new_price(new_price)
    if error != "":
        st.error(error)
    else:
        update_food_price_in_db(selected_food.id, new_price)
        st.cache_data.clear()
        st.session_state["success_message"] = "Cập nhật giá thành công!"
        st.rerun()

def handle_delete_food(selected_food):
    delete_food(selected_food.id)
    st.cache_data.clear()
    st.session_state["success_message"] = "Xóa món thành công!"
    st.rerun()

def handle_update_food_available(selected_food, new_available):
    update_food_available_in_db(selected_food.id, new_available)
    st.cache_data.clear()
    st.session_state["success_message"] = "Cập nhật trạng thái thành công"
    st.rerun()

def handle_update_food_name(food_id, new_name, foods):
    error = validate_new_food_name(new_name, foods)
    if error != "":
        st.error(error)
    else:
        update_food_name_in_db(food_id, new_name.strip())
        st.cache_data.clear()
        st.session_state["success_message"] = "Sửa tên món thành công"
        st.rerun()

def handle_update_food_category(food_id, new_category):
    update_food_category_in_db(food_id, new_category)
    st.cache_data.clear()
    st.session_state["success_message"] = "Sửa loại món thành công"
    st.rerun()

def handle_update_food(food_id, new_name, new_price, new_category, new_available, foods):
    error = validate_update_food_name(food_id, new_name, foods)

    if error != "":
        st.error(error)
        return

    update_food_in_db(
        food_id,
        new_name.strip(),
        new_price,
        new_category,
        new_available
    )

    st.cache_data.clear()
    st.session_state["success_message"] = "Sửa món thành công"
    st.rerun()

