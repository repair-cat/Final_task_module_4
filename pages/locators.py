"""для выноса селекторов во внешнюю переменную"""

from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')                 # кнопка "Добавить в корзину"
    MINI_BASKET = (By.XPATH, '//strong[contains(text(), "£")]')             # "Стоимость корзины составляет"
    PRODUCT_PRICE = (By.XPATH, '//p[@class="price_color"]')                 # Цена товара
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')                    # имя продукта
    PRODUCT_ADD_MESSAGE = (By.XPATH, '//div[@id="messages"]//strong[1]')    # имя товара в соообщении и добавлении его в корзину