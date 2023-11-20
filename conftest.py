import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='Choose browser: chrome or firefox')
    parser.addoption(
        '--language',
        action='store',
        default='en-gb',
        help=f'Choose language: en or ru'
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser')
    user_language = request.config.getoption('language')
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print("\nquit browser..")
    browser.quit()


