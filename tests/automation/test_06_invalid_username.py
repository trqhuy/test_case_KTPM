"""
TC06: Negative Test - Invalid Username
"""
from pages.login_page import LoginPage


def test_06_invalid_username_login(driver):
    """
    Test Case TC06:
    1. Open UTC Login Page
    2. Enter non-existent username and dummy password
    3. Click login button
    4. Verify authentication failure (remains on login form or displays error)
    """
    login_page = LoginPage(driver)
    login_page.open_login_page()

    login_page.login("non_existent_utc_user_99999", "SomePassword123!")

    # Verify authentication fails and login form remains visible
    assert login_page.is_username_field_displayed() is True
