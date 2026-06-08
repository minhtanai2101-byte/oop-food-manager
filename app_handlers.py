import streamlit as st
from database import update_food_price_in_db, update_food_available_in_db, delete_food
from app_validators import validate_new_price

def handle_update_food_price(selected_food, new_price):
    error = validate_new_price(new_price)
    if error != "":
        st.error(error)
    else:
        update_food_price_in_db(selected_food.id, new_price)
        st.session_state["success_message"] = "Cập nhật giá thành công!"
        st.rerun()

def handle_delete_food(selected_food):
    delete_food(selected_food.id)
    st.session_state["success_message"] = "Xóa món thành công!"
    st.rerun()

def handle_update_food_available(selected_food, new_available):
    update_food_available_in_db(selected_food.id, new_available)
    st.session_state["success_message"] = "Cập nhật trạng thái thành công"
    st.rerun()