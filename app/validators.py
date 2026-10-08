"""
Validation module for UTC e-Office login business logic (Unit Test targets).
"""
import re

def validate_username(username: str) -> dict:
    if username is None:
        return {"valid": False, "message": "Tên đăng nhập không được để trống"}
    username = username.strip()
    if not username:
        return {"valid": False, "message": "Tên đăng nhập không được để trống"}
    if len(username) < 3:
        return {"valid": False, "message": "Tên đăng nhập phải có ít nhất 3 ký tự"}
    if len(username) > 50:
        return {"valid": False, "message": "Tên đăng nhập không vượt quá 50 ký tự"}
    return {"valid": True, "message": "Hợp lệ"}


def validate_password(password: str) -> dict:
    if password is None or password == "":
        return {"valid": False, "message": "Mật khẩu không được để trống"}
    if len(password) < 4:
        return {"valid": False, "message": "Mật khẩu phải có ít nhất 4 ký tự"}
    return {"valid": True, "message": "Hợp lệ"}


def validate_utc_email(email: str) -> dict:
    if not email:
        return {"valid": False, "message": "Email không được để trống"}
    pattern = r"^[a-zA-Z0-9._%+-]+@utc\.edu\.vn$"
    if not re.match(pattern, email.strip()):
        return {"valid": False, "message": "Email phải có tên miền @utc.edu.vn"}
    return {"valid": True, "message": "Hợp lệ"}
