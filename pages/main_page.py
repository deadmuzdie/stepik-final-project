from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
    #    self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        url = self.browser.current_url
#        if (url.find("login") != -1):
        assert url.find("login") != -1, "Not in login page here"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present (*LoginPageLocators.LOGIN_FORM) , "No login form on this page"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present (*LoginPageLocators.REGISTER_FORM) , "No register form on this page"
#def should_be_login_link(self):
#    assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"