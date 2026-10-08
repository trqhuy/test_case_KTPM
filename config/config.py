import os

BASE_URL = os.getenv("UTC_BASE_URL", "https://vanphongdientu.utc.edu.vn/")
TIMEOUT = int(os.getenv("UTC_TIMEOUT", "10"))
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
