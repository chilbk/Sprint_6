import pytest
from resources import ORDER_URL
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators  # Добавил импорт локаторов
import time

#Здесь когда-то было много, но последней правкой я убил всё, что здесь было. Осталась лишь самая последняя попытка
#Остальное я написал в README.md
def test_enter_name(browser):
    browser.get(ORDER_URL)
    time.sleep(3)
    order_page = OrderPage(browser)
    order_page.enter_name("Ревью")
    input_field = browser.find_element(*OrderPageLocators.CUSTOMER_NAME)
    assert input_field.get_attribute("value") == "Ревью", "Имя не было введено корректно"
