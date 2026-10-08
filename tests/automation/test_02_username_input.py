"""
TC02: Verify Username Input Field Interactivity
"""
from pages.login_page import LoginPage


def test_02_username_input_interactivity(driver):
    """
    Test Case TC02:
    1. Open UTC Login Page
    2. Type username string into input field
    3. Verify value attribute matches entered username
    """
    login_page = LoginPage(driver)
    login_page.open_login_page()

    test_user = "test_user_utc"
    login_page.enter_username(test_user)

    entered_val = login_page.get_attribute(login_page.USERNAME_INPUT, "value")
    assert entered_val == test_user
