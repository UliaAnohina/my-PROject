# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose interface language, e.g. 'en', 'ru', 'es'")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    # options.add_argument("--headless")  # можно добавить для фона, если нужно
    print(f"\nStarting Chrome with language='{user_language}'...")
    driver = webdriver.Chrome(options=options)
    yield driver
    print("\nQuitting browser...")
    driver.quit()