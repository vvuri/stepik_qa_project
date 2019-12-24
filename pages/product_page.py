from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def check_name_product(self, name):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_BOOK)
        assert name_product.text == name

    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()
