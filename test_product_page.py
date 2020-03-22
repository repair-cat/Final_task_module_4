"""тест-кейсы для страниц товаров"""
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'


@pytest.mark.user_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = 'Galagramma2'
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()      
        page.register_new_user(email, password)


    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.product_should_be_add_to_basket()      # находим элемент корзины и кликаем на него, вводим ответ на alert
        page.product_name_like_in_basket()          # сравнение имени товара и имени товара в сообщении
        page.product_price_is_equal_to_basket()     # сравнение цены товара и корзины               


    def test_guest_cant_see_success_message(self, browser):
        # тест на проверку отсутсвия сообщения о добавлении в корзину сразу после открытия страницы с товаром
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


def test_user_cant_see_success_message_after_adding_product_to_basket(browser):
    # тест на проверку отсутсвия сообщения о добавлении в корзину после нажатия на кнопку "Добавить в корзину"
    page = ProductPage(browser, link)
    page.open()
    page.product_should_be_add_to_basket()
    page.should_not_be_success_message()         
        

def test_message_disappeared_after_adding_product_to_basket(browser): 
    # тест на проверку об исчезновении сообщения о добавлении товара в корзину после нажатия на кнопку "Добавить в корзину"
    page = ProductPage(browser, link)
    page.open()
    page.product_should_be_add_to_basket()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    # ссылку на логин видно со страницы продукта
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    # пользователь может зайти в логин со страницы продукта
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # пользователь может зайти в корзину со страницы продукта
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()                                 # открываем старницу товара
    page.go_to_basket()                         # переходим в корзину
    basket = BasketPage(browser, browser.current_url)
    basket.basket_have_not_product()            # проверка на отсутствие продуктов в корзине
    basket.basket_is_empty()                    # проверка о наличии заголовка "Ваша корзина пуста"               
