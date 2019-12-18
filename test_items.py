import time
link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_btn_add_to_basket_is_visible(browser):
    browser.get(link)
    btn_basket = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert(btn_basket.is_displayed())


    time.sleep(30)