# Hệ thống API Phân tích cảm xúc đa ngôn ngữ (Sentiment Analysis)

Đây là bài thực hành số 1 - môn Tư duy tính toán. Hệ thống cung cấp Web API sử dụng FastAPI để phân tích cảm xúc của văn bản (hỗ trợ cả tiếng Anh và tiếng Việt) thông qua mô hình học máy.

## Thông tin sinh viên
- **Họ và tên:** Phạm Đức Toàn
- **MSSV:** 24120467

## Thông tin mô hình
- **Tên mô hình:** `lxyuan/distilbert-base-multilingual-cased-sentiments-student`
- **Liên kết Hugging Face:** [lxyuan/distilbert-base-multilingual-cased-sentiments-student](https://huggingface.co/lxyuan/distilbert-base-multilingual-cased-sentiments-student)
- **Mô tả chức năng:** Mô hình này là một phiên bản DistilBERT hỗ trợ đa ngôn ngữ, nhận đầu vào là một câu văn và dự đoán cảm xúc của câu đó (tích cực, tiêu cực, hoặc trung tính).

## Hướng dẫn cài đặt và chạy chương trình
1. Clone repository này về máy.
2. Tạo môi trường ảo và kích hoạt: `python -m venv .venv`
3. Cài đặt các thư viện cần thiết: `pip install -r requirements.txt`
4. Khởi động server API: `python -m uvicorn main:app --reload`

## Hướng dẫn gọi API (Request/Response)
Hệ thống cung cấp 2 endpoints chính để tương tác. Dữ liệu giao tiếp được định dạng hoàn toàn bằng **JSON**.
### 1. Kiểm tra trạng thái hệ thống
- **Endpoint:** `GET /health`
- **Mô tả:** Dùng để ping kiểm tra xem server API có đang hoạt động và mô hình AI đã được nạp thành công vào bộ nhớ hay chưa.
- **Response trả về (200 OK):**
```json
{
  "status": "ok",
  "message": "Mô hình đã sẵn sàng hoạt động."
}
```
### 2. Phân tích cảm xúc văn bản (Endpoint Chính)
- **Endpoint:** `POST /predict`
- **Mô tả:** Nhận dữ liệu văn bản (tiếng Việt hoặc tiếng Anh) từ người dùng, đưa qua mô hình Multilingual DistilBERT và trả về kết quả dự đoán cảm xúc.

**Cấu trúc Request Body:**
| Tham số | Kiểu dữ liệu | Bắt buộc | Mô tả |
| :--- | :--- | :---: | :--- |
| `text` | `string` | Có | Câu văn hoặc đoạn văn bản cần phân tích cảm xúc. |

**Ví dụ Request (Sử dụng Python `requests`):**
```python
import requests

url = "[http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict)"
headers = {"Content-Type": "application/json"}
payload = {
    "text": "App này thiết kế rất đẹp và trải nghiệm mượt mà!"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

**✅ Ví dụ Response thành công (HTTP Status 200 OK):**
```json
{
  "input_text": "App này thiết kế rất đẹp và trải nghiệm mượt mà!",
  "prediction": "positive",
  "confidence_score": 0.985421
}
```

**❌ Ví dụ Response báo lỗi (HTTP Status 400 Bad Request):**
*(Trường hợp người dùng gửi văn bản rỗng)*
```json
{
  "detail": "Văn bản đầu vào không được để trống."
}
```
Dưới đây là video demo chi tiết 
https://github.com/user-attachments/assets/e1dcd2af-76d9-41d0-afd0-f63ec3d2f352



