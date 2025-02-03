from selenium.webdriver.common.by import By
class OrderPageLocators:
    # Экран Order
    CUSTOMER_NAME = (By.CSS_SELECTOR, 'input.Input_Input__1iN_Z')
    CUSTOMER_LASTNAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    CUSTOMER_ADRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    CUSTOMER_METRO = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    CUSTOMER_PHONE = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, './/button[text()="Далее"]')
    # Экран Order. Про аренду
    RENTAL_HEADER = (By.XPATH, '//div[@class="Order_Header__BZXOb" and text()="Про аренду"]')
    RENTAL_DATE = (By.XPATH, '//input[@placeholder="* Когда привезти"]')
    RENTAL_PERIOD = (By.XPATH, '//*[@class="Dropdown-placeholder"]')
    RENTAL_DATE_IS_FILLED = (By.XPATH, '//*[@class="Dropdown-placeholder is-selected"]')
    RENTAL_SCOOTER_COLOR_BLACK = (By.ID, 'black')
    RENTAL_SCOOTER_COLOR_GRAY = (By.ID, 'grey')
    RENTAL_COMMENTS = (By.XPATH, './/*[@placeholder="Комментарий для курьера"]')
    RENTAL_ORDER_BUTTON = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]')
    RENTAL_BACK_BUTTON = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Назад"]')
    # Экран Order. Хотите оформить заказ?
    MODAL_WINDOW = (By.XPATH, '//div[@class="Order_Modal__YZ-d3"]')
    MODAL_YES_BUTTON = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Да"]')
    MODAL_NOT_BUTTON = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Нет"]')

    # Экран Order. Заказ оформлен
    REGISTERED_WINDOW = (By.XPATH, '//*[text()="Заказ оформлен"]')
    REGISTERED_STATUS_BUTTON = (By.XPATH, '//div[@class="Order_NextButton__1_rCA"]/button[text()="Посмотреть статус"]')