"""
TC05: Validation Test - Empty Password Submission
"""
from pages.login_page import LoginPage


def test_05_empty_password_validation(driver):
    """
    Test Case TC05:
    1. Open UTC Login Page
    2. Enter username, leave password empty
    3. Click login button
    4. Verify page stays on Login page
    """
    login_page = LoginPage(driver)
    login_page.open_login_page()

    login_page.enter_username("valid_user")
    login_page.enter_password("")
    login_page.click_login()

    assert login_page.is_password_field_displayed() is True
