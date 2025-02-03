from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure
import time


class OrderPage(BasePage):

    @allure.step('Ввести имя клиента')
    def enter_name(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.CUSTOMER_NAME))
        element.click()  # Явный клик по полю перед вводом
        time.sleep(1)  # Даем странице время обработать клик
        element.clear()  # Очистка перед вводом
        time.sleep(0.5)  # Небольшая пауза перед вводом (опционально)
        element.send_keys(name)

        # Клик вне поля, если нужно активировать валидацию
        self.driver.find_element(OrderPageLocators.CUSTOMER_NAME).click()
        time.sleep(0.5)  # Опциональная пауза после ввода

        # Проверяем, что текст действительно ввелся
        assert element.get_attribute(
            "value") == name, f"Ожидалось '{name}', но введено '{element.get_attribute('value')}'"

    @allure.step('Ввести фамилию клиента')
    def enter_last_name(self, last_name):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(OrderPageLocators.CUSTOMER_LASTNAME))
        return element.send_keys(last_name)

    @allure.step('Ввести адрес клиента')
    def enter_address(self, address):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(OrderPageLocators.CUSTOMER_ADRESS))
        return element.send_keys(address)

    @allure.step('Ввести телефон клиента')
    def enter_phone(self, phone):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(OrderPageLocators.CUSTOMER_PHONE))
        return element.send_keys(phone)

    @allure.step('Ввести метро')
    def select_metro_station(self, metro):
        metro_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(OrderPageLocators.CUSTOMER_METRO))
        metro_input.send_keys(metro)

        metro_option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//li[contains(@class, "select-search__option") and text()="{metro}"]')))
        return metro_option.click()

    @allure.step('Нажать кнопку Далее')
    def click_next_button(self):
        next_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON))
        return next_button.click()

    @allure.step('Ввести дату аренды')
    def enter_rental_date(self, rental_date):
        rental_date_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(OrderPageLocators.RENTAL_DATE))
        return rental_date_input.send_keys(rental_date)

    @allure.step('Выбрать срок аренды')
    def select_rental_period(self, period):
        dropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD))
        dropdown.click()

        period_option = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//div[contains(@class, "Dropdown-option") and text()="{period}"]')))
        return period_option.click()

    @allure.step('Выбор цвета самоката')
    def choice_scooters_color_checkbox(self, black_checkbox=False, grey_checkbox=False):
        if black_checkbox == True:
            WebDriverWait(self.driver, OrderPage.timeout).until(EC.element_to_be_clickable(
                OrderPageLocators.ORDER_INPUT_CHECKBOX_BLACK)).click()
        elif grey_checkbox == True:
            WebDriverWait(self.driver, OrderPage.timeout).until(EC.element_to_be_clickable(
                OrderPageLocators.ORDER_INPUT_CHECKBOX_GREY)).click()
        return self

    @allure.step("Выбрать цвет самоката")
    def select_scooter_color(self, color):
        if color == 'black':
            self.click_element(OrderPageLocators.RENTAL_SCOOTER_COLOR_BLACK)
            return color
        elif color == 'grey':
            self.click_element(OrderPageLocators.RENTAL_SCOOTER_COLOR_GRAY)
            return color

    @allure.step('Ввести имя клиента')
    def enter_name(self, comment):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(OrderPageLocators.RENTAL_COMMENTS))
        return element.send_keys(comment)

    @allure.step('Нажатие кнопки Назад')
    def click_rental_back_button(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.RENTAL_BACK_BUTTON))
        return element.click()

    @allure.step('Нажатие кнопки Заказать и ожидание открытия Модального Окна')
    def click_rental_order_button_and_modal_window(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.RENTAL_ORDER_BUTTON))
        element.click()
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(OrderPageLocators.MODAL_WINDOW))

    @allure.step('Нажатие кнопки Нет')
    def click_modal_window_nope(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.MODAL_NOT_BUTTON))
        return element.click()

    @allure.step('Нажатие кнопки Да и ожидание открытия окна Заказ Оформлен')
    def click_modal_window_yep(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.MODAL_YES_BUTTON))
        element.click()
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(OrderPageLocators.REGISTERED_WINDOW))

    @allure.step('Нажатие клавиши Посмотреть статус')
    def click_modal_window_nope(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.REGISTERED_STATUS_BUTTON))
        return element.click()





