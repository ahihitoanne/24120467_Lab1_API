from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Tải mô hình từ Hugging Face vào bộ nhớ khi khởi động server
try:
    classifier = pipeline("sentiment-analysis", model="lxyuan/distilbert-base-multilingual-cased-sentiments-student")
except Exception as e:
    classifier = None
    print(f"Lỗi khi tải mô hình: {e}")

# Định nghĩa cấu trúc dữ liệu người dùng gửi lên
class TextRequest(BaseModel):
    text: str

# 1. GET /: Giới thiệu hệ thống
@app.get("/")
def read_root():
    return {
        "name": "Hugging Face Sentiment Analysis API",
        "description": "API phân tích cảm xúc văn bản tiếng Anh. Bài thực hành số 1 - Tư duy tính toán."
    }

# 2. GET /health: Kiểm tra trạng thái hệ thống
@app.get("/health")
def health_check():
    if classifier is not None:
        return {"status": "ok", "message": "Mô hình đã sẵn sàng hoạt động."}
    return {"status": "error", "message": "Mô hình chưa được tải."}

# 3. POST /predict: Nhận dữ liệu và trả kết quả AI
@app.post("/predict")
def predict(request: TextRequest):
    # Kiểm tra tính hợp lệ của dữ liệu đầu vào
    if not request.text or len(request.text.strip()) == 0:
        raise HTTPException(status_code=400, detail="Văn bản đầu vào không được để trống.")
    
    if classifier is None:
        raise HTTPException(status_code=503, detail="Hệ thống suy luận hiện không khả dụng.")

    try:
        # Chạy mô hình Hugging Face
        result = classifier(request.text)
        # Trả về JSON
        return {
            "input_text": request.text,
            "prediction": result[0]["label"],
            "confidence_score": result[0]["score"]
        }
    except Exception as e:
        # Xử lý lỗi trong quá trình suy luận
        raise HTTPException(status_code=500, detail=f"Lỗi suy luận từ mô hình: {str(e)}")