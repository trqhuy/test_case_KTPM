"""
TC09: Verification of UTC Email Google OAuth Link
"""
from pages.login_page import LoginPage


def test_09_google_utc_oauth_link(driver):
    """
    Test Case TC09:
    1. Open UTC Login Page
    2. Check 'Đăng nhập bằng e-mail UTC' button is displayed
    3. Verify href attribute contains google oauth URL structure
    """
    login_page = LoginPage(driver)
    login_page.open_login_page()

    href = login_page.get_google_login_href()
    assert href is not None
    assert "accounts.google.com" in href or "oauth2" in href
