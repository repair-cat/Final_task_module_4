"""тест-кейсы для страниц товаров"""
from .pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.product_should_be_add_to_basket()      # находим элемент корзины и кликаем на него, вводим ответ на alert
    page.product_added_to_basket()              # сравнение имени товара и имени товара в сообщении
    page.product_price_is_equal_to_basket()     # сравнение цены товара и корзины               