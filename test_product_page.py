from .pages.product_page import ProductPage

def  test_guest_can_add_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.check_name_product("Coders at Work")
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

