from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
    
    def should_be_login_link(self):
        # self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid") - без обратоки исключения, что плохо
        # assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented" - без фала locators
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    
    

