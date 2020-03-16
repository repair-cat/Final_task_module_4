"""методы для добавления товаров в корзину"""
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def product_should_be_add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket.click()
        self.solve_quiz_and_get_code()      # ввод ответа во всплывающее окно 

    
    def product_name_like_in_basket(self):
        # проверка добавления товара в корзину
        product_to_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_to_basket == product_name, "Product had not added to the basket"


    def product_price_is_equal_to_basket(self):
        # проверка совпадения цены товара и цены в корзине
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.MINI_BASKET).text
        assert product_price == basket_price, 'The Price in the basket is not equal the product price'

    
    def should_not_be_success_message(self):
        # не появилось ли сообщение о добавлении товара в корзину
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADD_MESSAGE), "Success message is presented, but should not be"


    def should_disappear_success_message(self):
        # исчезло ли сообщение о добавлении товара в корзину
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADD_MESSAGE), "Success message is not disappear"
        