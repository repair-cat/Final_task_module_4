from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"
login_link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'


def test_guest_can_go_to_login_page(browser): 
    page = MainPage(browser, link)      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                         # открываем страницу
    page.go_to_login_page()             # выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)    # реализация трех тестов из login_page.py
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

