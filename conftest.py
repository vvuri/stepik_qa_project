import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: es, fr, en, ...")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
   
    try:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        # options.add_argument('headless')              # headless mode
        # options.add_argument('window-size=1920x935')  # headles mode size
        browser = webdriver.Chrome(options=options)
    except:
        raise pytest.UsageError("language do not correct")
    finally:
        print(", language:" + language + "\n")

    yield browser
    print("\nquit browser..")
    browser.quit()