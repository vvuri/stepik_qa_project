from .pages.product_page import ProductPage
import pytest
"""
@pytest.fixture(scope="function", params=[
("http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear", "The shellcoder's handbook"),
("http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019", "Coders at Work")
])
def param_test(request):
    return request.param

def test_guest_can_add_product_to_basket(browser, param_test):
    (link, name) = param_test
    page = ProductPage(browser, link)
    page.open()
    page.check_name_product(name)
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
"""


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.check_name_product("Coders at Work")
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
