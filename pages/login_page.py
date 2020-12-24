from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        login = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        login.send_keys(email)
        pass_word = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        pass_word.send_keys(password)
        pass_rep = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REP)
        pass_rep.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        submit_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not found"
        assert '/login/' in self.url, "There is no 'login' substring in the url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not found"
