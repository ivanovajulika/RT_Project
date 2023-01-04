import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser...")
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,1080")
    options.headless = False
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser...")
    browser.quit()
