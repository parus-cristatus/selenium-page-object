from .base_page import BasePage
from .locators import LoginPageLocators
import random
import string


# Temporary helper function to generate random email strings
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


class LoginPage(BasePage):
    def register_new_user(self, password='e)6E2u1zoy'):
        email = f"{generate_random_string(5)}@yandex.com"
        email_element = self.browser.find_element(*LoginPageLocators.REG_FORM_EMAIL_FIELD)
        email_element.send_keys(email)
        password_element = self.browser.find_element(*LoginPageLocators.REG_FORM_PASSWORD_FIELD_PRIMARY)
        password_element.send_keys(password)
        password_repeat = self.browser.find_element(*LoginPageLocators.REG_FORM_PASSWORD_FIELD_REPEAT)
        password_repeat.send_keys(password)
        submit_btn = self.browser.find_element(*LoginPageLocators.REG_BTN)
        submit_btn.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'No "login" in page URL'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'No login form is found'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), 'No registration form is found'
