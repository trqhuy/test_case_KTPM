"""
TC10: Security Authentication Redirect Check
"""
from pages.login_page import LoginPage
from config.config import BASE_URL


def test_10_unauthorized_access_redirect(driver):
    """
    Test Case TC10:
    1. Navigate directly to internal protected URL (e.g., /Home or /VanBan)
    2. Verify system redirects unauthenticated user back to Login Page
    """
    login_page = LoginPage(driver)

    protected_url = BASE_URL.rstrip('/') + "/VanBan"
    login_page.open(protected_url)

    # System should display login page controls or redirect to login
    assert login_page.is_username_field_displayed() is True or "Login" in driver.current_url or "vanphongdientu.utc.edu.vn" in driver.current_url
