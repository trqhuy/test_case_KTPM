"""
TC07: Negative Test - Incorrect Password
"""
from pages.login_page import LoginPage


def test_07_incorrect_password_login(driver):
    """
    Test Case TC07:
    1. Open UTC Login Page
    2. Enter valid username pattern with wrong password
    3. Click login button
    4. Verify authentication failure
    """
    login_page = LoginPage(driver)
    login_page.open_login_page()

    login_page.login("admin_utc", "WrongPassword_999")

    assert login_page.is_password_field_displayed() is True
