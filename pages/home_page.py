from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
import allure

class HomePage(BasePage):
    @allure.step('Прокрутить до элемента и кликнуть')
    def scroll_to_and_click(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        return element.text
    @allure.step('Прокрутить до кнопки заказа внизу страницы и нажать')
    def scroll_and_click_order_button_bottom(self):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(HomePageLocators.BOTTOM_ORDER_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePageLocators.BOTTOM_ORDER_BUTTON)).click()
