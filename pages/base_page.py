from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure

class BasePage:
    timeout = 10
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переходим на сайт')
    def go_to_site(self, url):
        return self.driver.get(url)

    @allure.step('Нажатие кнопки Заказать вверху страницы')
    def click_top_order_button(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(BasePageLocators.BASE_TOP_ORDER_BUTTON))
        return element.click()

    @allure.step('Нажатие на логотип Яндекса и переключение на другое окно')
    def click_yandex_logo(self):
        # Получаем текущее окно
        original_window = self.driver.current_window_handle
        # Кликаем по логотипу Яндекса
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(BasePageLocators.BASE_TOP_YANDEX_LOGO))
        element.click()
        # Страница Дзен открывается в новом окне
        WebDriverWait(self.driver, 10).until(EC.new_window_is_opened)
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(BasePageLocators.Y_D))

    @allure.step('Нажатие на логотип Самоката')
    def click_scooter_logo(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(BasePageLocators.BASE_TOP_SCOOTER_LOGO))
        return element.click()

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Переключение на другую вкладку')
    def switch_to_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Закрытия уведомления об использовании cookie')
    def click_cookie_button(self):
        return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(
            BasePageLocators.COOKIE_BUTTON)).click()