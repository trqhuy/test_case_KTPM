# UTC e-Office Test Suite (Unit Test & Selenium Automation)

Dự án kiểm thử tự động (Unit Test & Selenium E2E Automation Test) cho website **Văn phòng điện tử UTC** (`https://vanphongdientu.utc.edu.vn/`) sử dụng **Python**, **pytest**, và **Selenium WebDriver** với mô hình **Page Object Model (POM)**.

## Cấu trúc Dự án

```
d:\HOC_Tap\KTPM/
├── app/                  # Logic ứng dụng / Validators (Unit Test)
├── config/               # Cấu hình dự án (BASE_URL, Timeouts)
├── pages/                # Page Object Model (BasePage, LoginPage)
├── tests/
│   ├── unit/             # Các bài Unit Test độc lập
│   └── automation/       # Các bài Selenium Automation Test UI/E2E
├── utils/                # Helper utilities (Screenshot...)
├── pytest.ini            # Cấu hình pytest
└── requirements.txt      # Danh sách thư viện cần cài đặt
```

## Hướng dẫn Chạy

### 1. Cài đặt môi trường
```bash
pip install -r requirements.txt
```

### 2. Chạy Unit Test
```bash
pytest tests/unit/ -v
```

### 3. Chạy Selenium Automation Test
```bash
pytest tests/automation/ -v --html=report.html --self-contained-html
```
