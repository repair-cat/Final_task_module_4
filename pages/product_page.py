"""методы для добавления товаров в корзину"""
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def product_should_be_add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket.click()
        self.solve_quiz_and_get_code()      # ввод ответа во всплывающее окно 

    
    def product_added_to_basket(self):
        # проверка добавления товара в корзину
        product_to_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_to_basket == product_name, "Product had not added to the basket"


    def product_price_is_equal_to_basket(self):
        # проверка совпадения цены товара и цены в корзине
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.MINI_BASKET).text
        assert product_price == basket_price, 'The Price in the basket is not equal the product price'
        