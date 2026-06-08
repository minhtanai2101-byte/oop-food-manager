# Project quản lý món ăn bằng Python OOP
## 1. Giới thiệu
- Đây là project học Python theo từng giai đoạn phát triển phần mềm quản lý món ăn.
- Giai đoạn đầu project chạy hoàn toàn bằng CLI.
- Hiện tại project đã có giao diện streamlit.
- Bản CLI vẫn được giữ lại để tham khảo trong qua trình học tập, phát triển
- Trước đây project lưu dữ liệu bằng file Json, giờ đã chuyển qua database với SQLite
## 2. Công nghệ sử dụng
- Python
- OOP
- SQLite
- Streamlit
- Git/Github
## 3. Các phiên bản trong Project
### 1. CLI version
File chạy chính:
```bash
py main.py
```
Đây là phiên bản terminal ban đầu dùng để luyện:
- Menu CLI
- input/print
- xử lý thêm, sửa, xóa món
- kết nối JSON trước, sau đó là với SQLite
### 2. Streamlit web version
#### File chạy chính:
```bash
py -m streamlit run app.py
```
Chức năng hiện có:
- Xem danh sách món ăn
- Thêm món mới
- Chặn tên món rỗng
- Chặn giá không hợp lệ
- Chặn món trùng tên
- Xóa món
- Sửa giá món
- Sửa trạng thái còn bán / hết bán
- Lọc theo loại món
- Lọc theo trạng thái
- Sắp xếp theo tên hoặc giá
- Reset bộ lọc
- Thống kê nhanh
- Lưu dữ liệu bằng SQLite
#### Cấu trúc file chính:
```
app.py
→ File chạy chính của Streamlit web app

main.py
→ File chạy phiên bản CLI terminal

food.py
→ Chứa class Food

database.py
→ Chứa các hàm làm việc với SQLite

config.py
→ Chứa cấu hình chung như DATABASE_FILE, FOOD_CATEGORIES

ui_helpers.py
→ Chứa các hàm hỗ trợ hiển thị như định dạng giá, trạng thái

app_stats.py
→ Chứa phần thống kê nhanh

app_table.py
→ Chứa phần hiển thị bảng món ăn

app_filters.py
→ Chứa sidebar, bộ lọc và sắp xếp

app_validators.py
→ Chứa các hàm kiểm tra dữ liệu nhập

app_handlers.py
→ Chứa các hàm xử lý hành động xóa, sửa giá, sửa trạng thái

app_sections.py
→ Chứa các khối giao diện thêm, xóa, sửa món
```
## 4. Cách chạy chương trình
### Đối với version CLI
- Mở terminal tại thư mục project và chạy file:
```bash 
python main.py
```
- Sau đó chọn chức năng theo menu hiển thị trên màn hình
### Đối với version streamlit web
- Cài đặt thư viện cần thiết bằng lệnh:
```bash
py -m pip install -r requirements.txt
```
- Mở terminal tại thư mục project chạy:
```bash
py -m streamlit run app.py
```
- Sau đó sẽ hiển thị giao diện trên web để chọn các chức năng trực quan hơn
## 5. Dữ liệu
- Dữ liệu món ăn được lưu trong SQLite database: food_manager.db
- File này không đưa lên GitHub vì đã được thêm vào .gitignore
## 6. Kiến thức đã sử dụng
- Class và object
- Method
- List object
- Function
- import giữa các file
- JSON đã từng sử dụng ở giai đoạn trước
- Xử lý lỗi bằng try/except
- Kiểm tra chuẩn hóa dữ liệu đầu vào
- Tách code thành nhiều file
- SQLite
- SQL cơ bản: CREATE TABLE, INSERT INTO, SELECT, UPDATE, DELETE
- Kết nối Python với SQLite bằng sqlite3
- Cài đặt Streamlit
- Tách ra nhiều module ở version streamlit ứng với các khu vực hiển thị trên web và chức năng chính của các module
- Tách module database.py
## Tác giả
- Minh Tan AI