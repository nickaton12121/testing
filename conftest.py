from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--maximized')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3) # если элемент не найден, то драйвер будет ждать 3 секунды, прежде чем выбросить исключение NoSuchElementException
    yield driver
    driver.close()