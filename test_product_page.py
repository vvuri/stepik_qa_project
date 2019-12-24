from .pages.product_page import ProductPage
import pytest

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

