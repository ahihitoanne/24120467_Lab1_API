import requests

url = "http://127.0.0.1:8000/predict"
payload = {
    "text": "API này hoạt động cực kỳ tốt! Tôi rất vui mừng!."
}

print("Đang gửi request lên server...")
response = requests.post(url, json=payload)

if response.status_code == 200:
    print("Kết quả trả về thành công:")
    print(response.json())
else:
    print(f"Có lỗi xảy ra. Mã lỗi: {response.status_code}")
    print(response.text)