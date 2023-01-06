import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

link = "https://b2c.passport.rt.ru"


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,1080")
    options.headless = False
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    # открывает страницу
    browser.get(link)
    browser.implicitly_wait(10)

    yield browser
    browser.quit()
