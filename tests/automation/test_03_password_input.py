"""
TC03: Verify Password Input Field Security & Type
"""
from pages.login_page import LoginPage


def test_03_password_input_security(driver):
    """
    Test Case TC03:
    1. Open UTC Login Page
    2. Check type attribute of userpwd input element is 'password'
    3. Enter password string and verify value matches
    """
    login_page = LoginPage(driver)
    login_page.open_login_page()

    input_type = login_page.get_attribute(login_page.PASSWORD_INPUT, "type")
    assert input_type == "password"

    test_pwd = "SecretPassword123"
    login_page.enter_password(test_pwd)

    entered_val = login_page.get_attribute(login_page.PASSWORD_INPUT, "value")
    assert entered_val == test_pwd
