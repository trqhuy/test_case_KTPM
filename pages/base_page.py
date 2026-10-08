from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.config import TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    def open(self, url: str):
        self.driver.get(url)

    def find(self, locator: tuple):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator: tuple):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: tuple):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator: tuple, text: str):
        element = self.find_visible(locator)
        element.clear()
        if text:
            element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        return self.find_visible(locator).text

    def get_attribute(self, locator: tuple, attribute_name: str) -> str:
        return self.find(locator).get_attribute(attribute_name)

    def is_displayed(self, locator: tuple) -> bool:
        try:
            return self.find_visible(locator).is_displayed()
        except TimeoutException:
            return False

    def get_title(self) -> str:
        return self.driver.title

    def get_current_url(self) -> str:
        return self.driver.current_url
