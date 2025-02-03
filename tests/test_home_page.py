import pytest
import allure
from pages.home_page import HomePage
from locators.home_page_locators import HomePageLocators
from resources import RECOURSE_URL, ORDER_URL

@pytest.mark.parametrize('question_locator, answer_locator', [
    (HomePageLocators.IMPORTANT_THING_1, HomePageLocators.IMPORTANT_ANSWER_1),
    (HomePageLocators.IMPORTANT_THING_2, HomePageLocators.IMPORTANT_ANSWER_2),
    (HomePageLocators.IMPORTANT_THING_3, HomePageLocators.IMPORTANT_ANSWER_3),
    (HomePageLocators.IMPORTANT_THING_4, HomePageLocators.IMPORTANT_ANSWER_4),
    (HomePageLocators.IMPORTANT_THING_5, HomePageLocators.IMPORTANT_ANSWER_5),
    (HomePageLocators.IMPORTANT_THING_6, HomePageLocators.IMPORTANT_ANSWER_6),
    (HomePageLocators.IMPORTANT_THING_7, HomePageLocators.IMPORTANT_ANSWER_7),
    (HomePageLocators.IMPORTANT_THING_8, HomePageLocators.IMPORTANT_ANSWER_8),
])
@allure.title('Проверка раскрытия вопросов в разделе "Вопросы о важном"')
def test_scroll_to_and_click(browser, question_locator, answer_locator):
    with allure.step('Открываем главную страницу'):
        browser.get(RECOURSE_URL)
    home_page = HomePage(browser)
    with allure.step(f'Прокручиваем до вопроса {question_locator} и кликаем'):
        home_page.scroll_to_and_click(question_locator)
    with allure.step('Проверяем, что ответ раскрывается и стал видимым'):
        answer_element = browser.find_element(*answer_locator)
    assert answer_element.is_displayed(), 'Ответ не отобразился после клика на вопрос'


def test_scroll_and_click_order_button_bottom(browser):
    with allure.step('Открываем главную страницу'):
        browser.get(RECOURSE_URL)
    home_page = HomePage(browser)
    with allure.step('Прокручиваем страницу до кнопку Заказать и кликаем'):
        home_page.scroll_and_click_order_button_bottom()
    with allure.step('Проверяем, что URL страницы изменился'):
        assert browser.current_url == ORDER_URL, "Некорректный URL после нажатия кнопки заказа"
