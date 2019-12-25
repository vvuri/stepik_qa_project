from .base_page import BasePage

class BasketPage(BasePage): 
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)
    
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "The basket do not empty"

    def should_be_success_message_empty_basket(self):
        pass

