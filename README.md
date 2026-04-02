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
- **Kiểm tra trạng thái:** `GET /health`
- **Phân tích cảm xúc:** `POST /predict`
  
**Ví dụ Request (Python):**
```python
import requests

url = "[http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict)"
payload = {"text": "App này rất tuyệt vời"}
response = requests.post(url, json=payload)
print(response.json())
##Response trả về (JSON):
JSON
{
  "input_text": "App này rất tuyệt vời",
  "prediction": "positive",
  "confidence_score": 0.985421
}
Video Demo Nghiệm thu
[Bấm vào đây để xem Video Demo]
