# Tra Cứu Phương Tiện Vi Phạm Giao Thông

Một ứng dụng Python tự động truy cập website CSGT.vn để tra cứu thông tin vi phạm giao thông bằng cách sử dụng Selenium, EasyOCR và lập lịch chạy tự động.

## Tính năng
- Đọc biển số và loại phương tiện từ file `.env`.
- Tự động tra cứu lịch chạy 6h sáng và 12h trưa hằng ngày.
- Phát hiện sai CAPTCHA và tự động thử lại.

---

## Yêu cầu hệ thống

- Python 3.x
- Google Chrome
- ChromeDriver phù hợp với phiên bản Chrome đang dùng

---

## Các thư viện cần cài đặt

Chạy lệnh sau để cài đặt các thư viện:

```bash
pip install -r requirements.txt
```

**Nếu muốn cài riêng lẻ:**

```bash
pip install easyocr selenium schedule python-dotenv torch torchvision torchaudio
```

---

## Cài đặt ChromeDriver

1. Kiểm tra phiên bản Chrome (`chrome://settings/help`).
2. Tải ChromeDriver phù hợp: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
3. Giải nén và:
   - Đặt file `chromedriver.exe` vào cùng thư mục với script Python, **hoặc**
   - Thêm đường dẫn `chromedriver` vào biến môi trường `PATH`.

---


## Cấu hình biến môi trường

Tạo một file tên `.env` trong cùng thư mục project, ví dụ:

```env
bien_so="12A34567"
option="Ô Tô"
```

- `bien_so`: biển số xe cần tra cứu.
- `option`: 
    - 1 = Ô tô
    - 2 = Xe máy
    - 3 = Xe đạp điện

---

## Cách sử dụng

1. Clone project về máy:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Cài đặt thư viện:

```bash
pip install -r requirements.txt
```

3. Tạo file `.env` như hướng dẫn bên trên.

4. Chạy script:

```bash
python auto_phatnguoi.py
```

5. Chương trình sẽ tự động:
    - Mở trình duyệt Chrome.
    - Tải CAPTCHA và giải mã bằng EasyOCR.
    - Điền thông tin và gửi tra cứu.
    - Nếu CAPTCHA sai sẽ tự thử lại.
    - Chạy tự động mỗi ngày vào các giờ đã định.

---

## Cấu trúc thư mục

```
├── auto_phatnguoi.py
├── README.md
├── .env
├── captcha.png (tạm thời, tự động sinh)
└── requirements.txt
```

---

## Ghi chú

- Website csgt.vn có thể thay đổi giao diện, cần cập nhật XPath nếu lỗi.
- EasyOCR không luôn nhận CAPTCHA chính xác 100%.
---
