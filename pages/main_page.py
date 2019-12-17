from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_login_url(self):
        url = self.browser.current_url
        assert url.find("login") != -1, "Not in login page here"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present (*LoginPageLocators.LOGIN_FORM) , "No login form on this page"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present (*LoginPageLocators.REGISTER_FORM) , "No register form on this page"
