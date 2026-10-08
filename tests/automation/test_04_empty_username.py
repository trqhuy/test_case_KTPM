"""
TC04: Validation Test - Empty Username Submission
"""
from pages.login_page import LoginPage


def test_04_empty_username_validation(driver):
    """
    Test Case TC04:
    1. Open UTC Login Page
    2. Leave username empty, enter password
    3. Click login button
    4. Verify page stays on Login page (does not redirect to dashboard)
    """
    login_page = LoginPage(driver)
    login_page.open_login_page()

    login_page.enter_username("")
    login_page.enter_password("some_password")
    login_page.click_login()

    # User remains on login form
    assert login_page.is_username_field_displayed() is True
