"""для выноса селекторов во внешнюю переменную"""

from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    PASS_1 = (By.CSS_SELECTOR, '#id_registration-password1')
    PASS_2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')
    USER_IS_REGISTERED = (By.CSS_SELECTOR, '.wicon')    


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')                 # кнопка "Добавить в корзину"
    MINI_BASKET = (By.XPATH, '//strong[contains(text(), "£")]')             # "Стоимость корзины составляет"
    PRODUCT_PRICE = (By.XPATH, '//p[@class="price_color"]')                 # Цена товара
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')                    # имя продукта
    PRODUCT_ADD_MESSAGE = (By.XPATH, '//div[@id="messages"]//strong[1]')    # имя товара в соообщении о добавлении его в корзину


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")                             # пользователь залогинен


class BasketPageLocators():
    LOOK_BASKET = (By.XPATH, '//span[@class="btn-group"]')                  # ссылка "Посмотреть корзину"
    BASKET_HAVE_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6.h3')                             # есть товары в корзине
    BASKET_IS_EMPTY = (By.XPATH, '//p[contains(text(), "Your basket is empty")]')       # заголовок - Ваша корзина пуста
