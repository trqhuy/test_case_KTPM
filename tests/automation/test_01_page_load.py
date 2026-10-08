"""
TC01: Verify UTC e-Office Login Page Loads Successfully
"""
from pages.login_page import LoginPage
from config.config import BASE_URL


def test_01_login_page_load(driver):
    """
    Test Case TC01:
    1. Open URL https://vanphongdientu.utc.edu.vn/
    2. Verify URL starts with BASE_URL
    3. Verify Username input, Password input, and Submit button are displayed
    """
    login_page = LoginPage(driver)
    login_page.open_login_page()

    assert driver.current_url.startswith(BASE_URL)
    assert login_page.is_username_field_displayed() is True
    assert login_page.is_password_field_displayed() is True
    assert login_page.is_login_button_displayed() is True
