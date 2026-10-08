"""
Unit tests for username, password, and UTC email validation functions.
No browser/Selenium required for these unit tests.
"""
import pytest
from app.validators import validate_username, validate_password, validate_utc_email


class TestUsernameValidation:
    """Unit tests for validate_username function."""

    def test_valid_username(self):
        result = validate_username("nguyenhuy")
        assert result["valid"] is True
        assert result["message"] == "Hợp lệ"

    def test_empty_username(self):
        result = validate_username("")
        assert result["valid"] is False
        assert result["message"] == "Tên đăng nhập không được để trống"

    def test_none_username(self):
        result = validate_username(None)
        assert result["valid"] is False
        assert result["message"] == "Tên đăng nhập không được để trống"

    def test_too_short_username(self):
        result = validate_username("ab")
        assert result["valid"] is False
        assert result["message"] == "Tên đăng nhập phải có ít nhất 3 ký tự"

    def test_too_long_username(self):
        result = validate_username("a" * 51)
        assert result["valid"] is False
        assert result["message"] == "Tên đăng nhập không vượt quá 50 ký tự"


class TestPasswordValidation:
    """Unit tests for validate_password function."""

    def test_valid_password(self):
        result = validate_password("Secret123")
        assert result["valid"] is True
        assert result["message"] == "Hợp lệ"

    def test_empty_password(self):
        result = validate_password("")
        assert result["valid"] is False
        assert result["message"] == "Mật khẩu không được để trống"

    def test_none_password(self):
        result = validate_password(None)
        assert result["valid"] is False
        assert result["message"] == "Mật khẩu không được để trống"

    def test_too_short_password(self):
        result = validate_password("123")
        assert result["valid"] is False
        assert result["message"] == "Mật khẩu phải có ít nhất 4 ký tự"


class TestUTCEmailValidation:
    """Unit tests for validate_utc_email function."""

    def test_valid_utc_email(self):
        result = validate_utc_email("huy.nt@utc.edu.vn")
        assert result["valid"] is True
        assert result["message"] == "Hợp lệ"

    def test_invalid_domain_email(self):
        result = validate_utc_email("huy.nt@gmail.com")
        assert result["valid"] is False
        assert result["message"] == "Email phải có tên miền @utc.edu.vn"

    def test_empty_email(self):
        result = validate_utc_email("")
        assert result["valid"] is False
        assert result["message"] == "Email không được để trống"
