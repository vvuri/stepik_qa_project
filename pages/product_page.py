from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def check_name_product(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_BOOK)
        name_product_in_basket = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_BOOK_IN_BASKET)
        assert name_product.text == name_product_in_basket.text

    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()
