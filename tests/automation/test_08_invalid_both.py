"""
TC08: Negative Test - Invalid Username and Password
"""
from pages.login_page import LoginPage


def test_08_invalid_username_and_password(driver):
    """
    Test Case TC08:
    1. Open UTC Login Page
    2. Enter random invalid username and random invalid password
    3. Click login button
    4. Verify authentication failure
    """
    login_page = LoginPage(driver)
    login_page.open_login_page()

    login_page.login("invalid_user_abc", "invalid_pass_xyz")

    assert login_page.is_username_field_displayed() is True
