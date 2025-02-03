from selenium.webdriver.common.by import By

class HomePageLocators:
    # Кнопка Заказать внизу страницы
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_UltraBig__UU3Lp')]")
    # Блок Вопросы о важном
    IMPORTANT_THING_1 = (By.ID, 'accordion__heading-0')
    IMPORTANT_THING_2 = (By.ID, 'accordion__heading-1')
    IMPORTANT_THING_3 = (By.ID, 'accordion__heading-2')
    IMPORTANT_THING_4 = (By.ID, 'accordion__heading-3')
    IMPORTANT_THING_5 = (By.ID, 'accordion__heading-4')
    IMPORTANT_THING_6 = (By.ID, 'accordion__heading-5')
    IMPORTANT_THING_7 = (By.ID, 'accordion__heading-6')
    IMPORTANT_THING_8 = (By.ID, 'accordion__heading-7')
    # Раскрывает Вопросы о важном
    IMPORTANT_ANSWER_1 = (By.XPATH, '//*[@aria-labelledby="accordion__heading-0"]')
    IMPORTANT_ANSWER_2 = (By.XPATH, '//*[@aria-labelledby="accordion__heading-1"]')
    IMPORTANT_ANSWER_3 = (By.XPATH, '//*[@aria-labelledby="accordion__heading-2"]')
    IMPORTANT_ANSWER_4 = (By.XPATH, '//*[@aria-labelledby="accordion__heading-3"]')
    IMPORTANT_ANSWER_5 = (By.XPATH, '//*[@aria-labelledby="accordion__heading-4"]')
    IMPORTANT_ANSWER_6 = (By.XPATH, '//*[@aria-labelledby="accordion__heading-5"]')
    IMPORTANT_ANSWER_7 = (By.XPATH, '//*[@aria-labelledby="accordion__heading-6"]')
    IMPORTANT_ANSWER_8 = (By.XPATH, '//*[@aria-labelledby="accordion__heading-7"]')
