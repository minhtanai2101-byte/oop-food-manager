import streamlit as st
import pandas as pd
from imports import validate_import_foods_df
from database import get_foods_by_filters, import_foods_from_df, get_all_foods, get_foods_by_category, get_foods_by_category_and_available
from config import FOOD_CATEGORIES
from app_stats import show_food_stats
from app_table import show_food_table, convert_foods_to_csv, convert_foods_to_excel
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

    csv_data = convert_foods_to_csv(foods)

    st.download_button(
    label="Tải danh sách món CSV",
    data=csv_data,
    file_name="foods.csv",
    mime="text/csv")

    excel_data = convert_foods_to_excel(foods)

    st.download_button(
    label="Tải danh sách món Excel",
    data=excel_data,
    file_name="foods.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    uploaded_file = st.file_uploader(
    "Tải file CSV hoặc Excel lên",
    type=["csv","xlsx"])

    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)

        st.write("Dữ liệu đọc từ file:")
        st.dataframe(df)

        error = validate_import_foods_df(df)

        if error != "":
            st.error(error)
        else:
            st.success("File hợp lệ, có thể import")
        if st.button("Import vào database"):
            imported_count = import_foods_from_df(df)
            if imported_count > 0:
                st.success(
                    f"Đã import {imported_count} món mới"
                )
            else:
                st.info("Không có món mới để import")
                    
                
        
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