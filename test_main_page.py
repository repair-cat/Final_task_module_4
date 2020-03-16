from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser): 
    page = MainPage(browser, link)      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                         # открываем главную страницу
    page.go_to_login_page()             # выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)    # реализация трех тестов из login_page.py
    login_page.should_be_login_page()

@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # открытие корзины из главной страницы и провека наличия/отсутсвия продукта
    page = MainPage(browser, link)
    page.open()                             # открывает главную страницу
    page.go_to_basket()                     # переходим в корзину
    basket = BasketPage(browser, browser.current_url)
    basket.basket_have_not_product()
    basket.basket_is_empty()
