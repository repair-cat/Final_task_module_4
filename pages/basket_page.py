"""проверки для корзины"""

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_have_not_product(self):
        # проверка на отсутствие товара в корзине
        assert self.is_not_element_present(*BasketPageLocators.BASKET_HAVE_PRODUCT), "Basket have any products!"

    
    def basket_is_empty(self):
        # проверка на то, что корзина пуста
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "Basket is not empty!"
