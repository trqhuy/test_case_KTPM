import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.config import HEADLESS


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    if HEADLESS:
        chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(2)
    yield driver
    driver.quit()
