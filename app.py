import streamlit as st
from database import get_foods_by_filters, get_all_foods, get_foods_by_category, get_foods_by_category_and_available
from config import FOOD_CATEGORIES
from app_stats import show_food_stats
from app_table import show_food_table
from app_filters import show_sidebar, filter_and_sort_foods
from app_sections import (show_add_food_section,
                          show_delete_food_section,
                          show_update_available_section,
                          show_update_price_section,
                          show_update_name_section,
                          show_update_category_section, show_update_food_section)
st.set_page_config(
    page_title="Quản lý món ăn",
    page_icon="🥗",
    layout="wide"
)

def main(): 
    #create_table()
    #seed_sample_data()

    st.title("Quản lý món ăn")
    if "success_message" in st.session_state:
        st.success(st.session_state["success_message"])
        del st.session_state["success_message"]

    #foods = get_all_foods()
    filter_category, filter_available, sort_option, search_keyword = show_sidebar()
    foods = get_foods_by_filters(
    filter_category,
    filter_available,
    search_keyword,
    sort_option)
    
    
    show_food_stats(foods)

    #filter_category, filter_available, sort_option, search_keyword = show_sidebar()

    #display_foods = filter_and_sort_foods(
    #    foods,
     #   filter_category,
      #  filter_available,
       # sort_option,
        #search_keyword)
    show_food_table(foods)

    st.write("---")
    action = st.selectbox(
        "Chọn chức năng",
        [
            "Thêm món",
            "Xóa món",
            "Sửa món"
        ]
    )
    if action == "Thêm món":
        show_add_food_section(foods)

    elif action == "Xóa món":
        show_delete_food_section(foods)

    elif action == "Sửa giá món":
        show_update_price_section(foods)

    elif action == "Sửa tên món":
        show_update_name_section(foods)

    elif action == "Sửa loại món":
        show_update_category_section(foods)

    elif action == "Sửa trạng thái món":
        show_update_available_section(foods)
    
    elif action == "Sửa món":
        show_update_food_section(foods)

if __name__ == "__main__":
    main()