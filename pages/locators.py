from selenium.webdriver.common.by import By
#from .base_page import BasePage


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

#class LoginPage(BasePage):
class LoginPageLocators(): 
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
#    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
#button name=login_submit form id=login_form
#button name=registration_submit form id=register_form

