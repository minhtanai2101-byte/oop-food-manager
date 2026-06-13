from config import FOOD_CATEGORIES


def validate_import_foods_df(df):
    required_columns = ["Tên món", "Giá", "Loại món", "Trạng thái"]

    for column in required_columns:
        if column not in df.columns:
            return f"File thiếu cột: {column}"

    for index, row in df.iterrows():
        row_number = index + 2

        name = str(row["Tên món"]).strip()
        price = row["Giá"]
        category = str(row["Loại món"]).strip()
        status = str(row["Trạng thái"]).strip()

        if name == "":
            return f"Dòng {row_number}: Tên món không được để trống"

        if price < 0:
            return f"Dòng {row_number}: Giá không được nhỏ hơn 0"

        if category not in FOOD_CATEGORIES:
            return f"Dòng {row_number}: Loại món không hợp lệ"

        if status not in ["Còn bán", "Hết bán"]:
            return f"Dòng {row_number}: Trạng thái phải là Còn bán hoặc Hết bán"

    return ""