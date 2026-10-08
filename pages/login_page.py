from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import BASE_URL


class LoginPage(BasePage):
    # Locators strictly derived from actual website HTML
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "userpwd")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.submit_login")
    GOOGLE_UTC_BUTTON = (By.CSS_SELECTOR, "a.button")
    LOGIN_FORM = (By.TAG_NAME, "form")

    def open_login_page(self):
        self.open(BASE_URL)

    def enter_username(self, username: str):
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_google_login_href(self) -> str:
        return self.get_attribute(self.GOOGLE_UTC_BUTTON, "href")

    def is_username_field_displayed(self) -> bool:
        return self.is_displayed(self.USERNAME_INPUT)

    def is_password_field_displayed(self) -> bool:
        return self.is_displayed(self.PASSWORD_INPUT)

    def is_login_button_displayed(self) -> bool:
        return self.is_displayed(self.LOGIN_BUTTON)
