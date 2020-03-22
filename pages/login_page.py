from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        # регистрируем нового пользователя
        email_form = self.browser.find_element(*LoginPageLocators.EMAIL)     # найти поле ввода емайл
        email_form.send_keys(email)                                          # отправляем емайл в поле емайл
        pass_1 = self.browser.find_element(*LoginPageLocators.PASS_1)        # найти поле ввода пароля
        pass_1.send_keys(password)
        pass_2 = self.browser.find_element(*LoginPageLocators.PASS_2)        # найти поле повторного ввода пароля
        pass_2.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        reg_button.click()
        assert self.is_element_present(*LoginPageLocators.USER_IS_REGISTERED)  # сообщение о том, что юзер зареган


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "It's not a login page"

    def should_be_login_form(self):
        # реализуйте проверку на наличие формы логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку на наличие формы регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"