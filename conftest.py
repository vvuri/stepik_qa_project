import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: es, fr, en, ...")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    browser_name = request.config.getoption("browser_name")
    if browser_name == "firefox":
        print("\nstart firefox browser for test")
        browser = webdriver.Firefox()
    else:
        print("\nstart chrome browser for test")
        browser = webdriver.Chrome()
    
    try:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    except:
        raise pytest.UsageError("language do not correct")
    finally:
        print(", language:" + language + "\n")

    yield browser
    print("\nquit browser..")
    browser.quit()