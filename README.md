# Project quản lý món ăn bằng Python OOP
## 1. Giới thiệu
- Đây là project quản lý danh sách món ăn bằng Python.
- Project sử dụng lập trình hướng đối tượng OOP, lưu dữ liệu bằng file JSON, và chạy bằng menu trong terminal.
## 2. Chức năng chính
- Xem danh sách món ăn
- Thêm món ăn mới
- Không cho phép món trùng tên
- Tìm món theo tên
- Xóa món theo tên
- Sửa giá món ăn
- Sửa trạng thái món còn bán hay hết bán
- Lọc món theo loại món
- Lọc món theo trạng thái món
- Sắp xếp món theo tên hoặc giá
- Lưu dữ liệu vào file JSON
- Đọc dữ liệu từ file JSON khi mở chương trình
## 3. Cấu trúc file
```text
project/
- main.py
- food.py
- food_manager.py
- food_actions.py
- input_helpers.py
- config.py
- oop_food.json
```
## 4. Ý nghĩa từng file
- `main.py`: file chạy chính, hiển thị menu và điều phối chương trình
- `food.py`: chứa class Food, đại diện cho một món ăn
- `food_manager.py`: chứa class FoodManager, quản lý danh sách món ăn
- `food_actions.py`: chứa các handle xử lý hành động trong menu
- `input_helpers.py`: chứa các hàm input hỗ trợ nhập liệu
- `config.py`: chứa cấu hình chung như tên file dữ liệu
- `oop_food.json`: file lưu dữ liệu món ăn.
## 5. Cách chạy chương trình
- Mở terminal tại thư mục project và chạy file:
```bash 
python main.py
```
- Sau đó chọn chức năng theo menu hiển thị trên màn hình
## 6. Dữ liệu
- Dữ liệu món ăn được lưu trong file: oop_food.json
- Khi chương trình chạy, dữ liệu được đọc từ file JSON
- Khi thêm, xóa, sửa giá hoặc trạng thái món, dữ liệu được lưu vào file JSON
## 7. Kiến thức đã sử dụng
- Class và object
- Method
- List object
- Function
- import giữa các file
- JSON
- Xử lý lỗi bằng try/except
- Kiểm tra chuẩn hóa dữ liệu đầu vào
- Tách code thành nhiều file