import pytest
import allure
from selenium import webdriver
from resources import ORDER_URL
from pages.order_page import OrderPage

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()