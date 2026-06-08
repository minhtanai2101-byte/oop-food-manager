import streamlit as st
from database import create_table, get_all_foods
from app_stats import show_food_stats
from app_table import show_food_table
from app_filters import show_sidebar, filter_and_sort_foods
from app_sections import (show_add_food_section,
                          show_delete_food_section,
                          show_update_available_section,
                          show_update_price_section)
st.set_page_config(
    page_title="Quản lý món ăn",
    page_icon="🥗",
    layout="wide"
)

def main(): 
    create_table()

    st.title("Quản lý món ăn")
    if "success_message" in st.session_state:
        st.success(st.session_state["success_message"])
        del st.session_state["success_message"]

    foods = get_all_foods()
    show_food_stats(foods)

    filter_category, filter_available, sort_option = show_sidebar()

    display_foods = filter_and_sort_foods(
        foods,
        filter_category,
        filter_available,
        sort_option)


    show_food_table(display_foods)

    st.write("---")
    show_add_food_section(foods)

    st.write("---")
    show_delete_food_section(foods)

    st.write("---")
    show_update_price_section(foods)

    st.write("---")
    show_update_available_section(foods)

if __name__ == "__main__":
    main()