import pytest
import allure
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from resources import ORDER_URL, REDIRECT_URL, RECOURSE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_click_top_order_button(browser):
    base_page = BasePage(browser)
    base_page.go_to_site(RECOURSE_URL)
    base_page.click_top_order_button()
    assert browser.current_url == ORDER_URL, 'Некорректный URL'

def test_click_yandex_logo(browser):
    base_page = BasePage(browser)
    base_page.go_to_site(RECOURSE_URL)
    base_page.click_yandex_logo()
    base_page.switch_to_window()
    base_page.find_element(BasePageLocators.Y_D)
    assert browser.current_url == REDIRECT_URL, 'Некорректный URL'

def test_click_scooter_logo(browser):
    base_page = BasePage(browser)
    base_page.go_to_site(RECOURSE_URL)
    base_page.click_scooter_logo()
    assert browser.current_url == RECOURSE_URL, 'Некорректный URL'