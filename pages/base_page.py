'''базовая страница, от которой будут унаследованы все остальные классы. 
В ней мы опишем вспомогательные методы для работы с драйвером.'''

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)


    def is_element_present(self, how, what):        # метод для проверки наличия элемента
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True


    def is_not_element_present(self, how, what, timeout=4):     # метод для проверки отсутсвия элемента
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False


    def is_disappeared(self, how, what, timeout=4):             # метод для проверки исчезновения элемента
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


    def go_to_login_page(self):
        # кликабельна ли ссылка логина
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()


    def should_be_login_link(self):
        # есть ли ссылка на логин на странице
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"


    def solve_quiz_and_get_code(self):          # для получения проверочного кода на странице товара в вылетающем окне
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
