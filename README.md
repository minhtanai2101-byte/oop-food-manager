# Food Manager App

Ứng dụng quản lý món ăn được xây dựng trong quá trình học Python thực tế.

App bắt đầu từ phiên bản CLI terminal, sau đó được nâng cấp dần qua OOP, JSON, SQLite, Streamlit, GitHub, Deploy và hiện tại đã chuyển sang sử dụng Supabase PostgreSQL online.

## Demo

Link app online:

```text
https://food-manager-tan.streamlit.app
```

## Công nghệ sử dụng

```text
Python
Streamlit
PostgreSQL
Supabase
psycopg2
Git / GitHub
Streamlit Community Cloud
```

## Chức năng chính

App hiện hỗ trợ:

```text
- Xem danh sách món ăn
- Thêm món mới
- Sửa tên món
- Sửa giá món
- Sửa loại món
- Sửa trạng thái còn bán / hết bán
- Xóa món có xác nhận
- Tìm kiếm món theo tên
- Lọc món theo loại
- Lọc món theo trạng thái
- Sắp xếp món theo tên / giá
- Thống kê nhanh danh sách món
```

## Database

Phiên bản hiện tại sử dụng:

```text
Supabase PostgreSQL
```

Thay vì lưu dữ liệu trong file SQLite local, app hiện kết nối tới PostgreSQL online thông qua Supabase.

Mô hình hiện tại:

```text
Streamlit App
        ↓
Supabase PostgreSQL
        ↓
foods table
```

Bảng `foods` gồm các cột chính:

```text
id
name
price
category
available
```

## Bảo mật thông tin database

Thông tin kết nối database không được đưa lên GitHub.

App sử dụng:

```text
.streamlit/secrets.toml
```

để lưu `DATABASE_URL` khi chạy local.

File này đã được thêm vào `.gitignore`:

```text
.streamlit/secrets.toml
```

Khi deploy trên Streamlit Community Cloud, `DATABASE_URL` được cấu hình trong phần Secrets của Streamlit Cloud.

## Tối ưu hiệu năng

Sau khi chuyển từ SQLite sang Supabase PostgreSQL, app được tối ưu thêm để giảm lag khi chạy online:

```text
- Cache danh sách món bằng st.cache_data
- Clear cache sau khi thêm / sửa / xóa dữ liệu
- Dùng st.form để giảm rerun khi nhập liệu
- Chỉ render một chức năng tại một thời điểm
- Không chạy create_table() và seed_sample_data() mỗi lần app load
```

## Cấu trúc file chính

```text
app.py
```

File chính chạy app Streamlit.

```text
database.py
```

Chứa các hàm làm việc với Supabase PostgreSQL như đọc, thêm, sửa, xóa dữ liệu.

```text
app_sections.py
```

Chứa các phần giao diện như thêm món, sửa giá, sửa tên, sửa loại, sửa trạng thái và xóa món.

```text
app_handlers.py
```

Chứa các hàm xử lý khi người dùng bấm nút thêm / sửa / xóa.

```text
app_filters.py
```

Chứa logic tìm kiếm, lọc và sắp xếp món ăn.

```text
app_stats.py
```

Hiển thị thống kê nhanh.

```text
app_table.py
```

Hiển thị bảng danh sách món ăn.

```text
app_validators.py
```

Kiểm tra dữ liệu nhập vào trước khi thêm hoặc sửa món.

```text
config.py
```

Chứa các cấu hình chung như danh sách loại món.

```text
food.py
```

Chứa class Food đại diện cho một món ăn.

## Cài đặt local

Cài thư viện:

```bash
pip install -r requirements.txt
```

Tạo file secrets local:

```text
.streamlit/secrets.toml
```

Thêm nội dung:

```toml
DATABASE_URL = "postgresql://..."
```

Chạy app:

```bash
streamlit run app.py
```

## Ghi chú quan trọng

Không commit file `secrets.toml` lên GitHub.

Nếu password database có ký tự đặc biệt như `@`, cần mã hóa trong connection string.

Ví dụ:

```text
@  →  %40
```

## Trạng thái hiện tại

```text
- App chạy được local
- App deploy được trên Streamlit Community Cloud
- Database đã chuyển từ SQLite sang Supabase PostgreSQL
- Các chức năng CRUD đã test thành công
- App đã được tối ưu bước đầu để giảm lag
```

## Mục tiêu học được từ project

Qua project này, đã thực hành được:

```text
- Python cơ bản
- OOP
- Làm việc với file JSON
- SQLite
- SQL cơ bản
- PostgreSQL
- Supabase
- Streamlit
- Git / GitHub
- Deploy app online
- Bảo mật thông tin kết nối bằng secrets
- Tối ưu app Streamlit bằng cache và form
```

## Tác giả
- Minh Tan AI