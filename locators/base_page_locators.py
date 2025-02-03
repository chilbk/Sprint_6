from selenium.webdriver.common.by import By

class BasePageLocators:
    BASE_TOP_ORDER_BUTTON = (By.XPATH, './/*[contains(@class,"Header_Header")]//*[text()="Заказать"]')
    BASE_TOP_YANDEX_LOGO = (By.XPATH, './/*[@href="//yandex.ru"]')
    BASE_TOP_SCOOTER_LOGO = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')
    Y_D = (By.XPATH, '//div[@class="dzen-layout--header-micro-app__header-1m"]')
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')