import streamlit as st
from config import FOOD_CATEGORIES

def filter_and_sort_foods(foods,
                        filter_category, 
                        filter_available, 
                        sort_option, 
                        search_keyword):
    display_foods = foods

    if filter_category != "Tất cả":
        display_foods = [
            food for food in display_foods
            if food.category == filter_category
        ]

    if filter_available == "Còn bán":
        display_foods = [
            food for food in display_foods
            if food.available == True
        ]
    elif filter_available == "Hết bán":
        display_foods = [
            food for food in display_foods
            if food.available == False
        ]
    
    if search_keyword:
        display_foods = [food 
                 for food in display_foods
                 if search_keyword.lower() in food.name.lower()]
    
    if sort_option == "Tên A-Z":
        display_foods = sorted(display_foods, key=lambda food: food.name)
    elif sort_option == "Giá tăng dần":
        display_foods = sorted(display_foods, key=lambda food: food.price)
    elif sort_option == "Giá giảm dần":
        display_foods = sorted(display_foods, key=lambda food: food.price, reverse=True)
    if search_keyword:
        display_foods = [food 
                 for food in display_foods
                 if search_keyword.lower() in food.name.lower()]
    
    return display_foods

def show_sidebar():
    st.sidebar.title("🍜 Quản lý món ăn")
    st.sidebar.header("Bộ lọc và sắp xếp")

    if st.sidebar.button("Reset bộ lọc"):
        st.session_state["filter_category"] = "Tất cả"
        st.session_state["filter_available"] = "Tất cả"
        st.session_state["sort_option"] = "Không sắp xếp"

    filter_category = st.sidebar.selectbox(
        "Lọc theo loại món",
        ["Tất cả"] + FOOD_CATEGORIES,
        key="filter_category"
    )

    filter_available = st.sidebar.selectbox(
        "Lọc theo trạng thái",
        ["Tất cả", "Còn bán", "Hết bán"],
        key="filter_available"
    )

    sort_option = st.sidebar.selectbox(
        "Sắp xếp",
        ["Không sắp xếp", "Tên A-Z", "Giá tăng dần", "Giá giảm dần"],
        key="sort_option"
    )

    search_keyword = st.sidebar.text_input("Tìm kiếm món")
    

    st.sidebar.markdown("---")
    st.sidebar.subheader("Hướng dẫn nhanh")
    st.sidebar.write("Dùng bộ lọc để tìm món cần xem.")
    st.sidebar.write("Dùng các khối bên dưới bảng để thêm, xóa hoặc sửa món.")

    return filter_category, filter_available, sort_option, search_keyword