from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators
from .locators import LoginPageLocators


class BasePage:
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open_page(self):
        self.browser.get(self.link)

    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    def btn_mask(self, method, locator, word):
        self.browser.find_element(method, locator).click()
        color = self.browser.find_element(method, locator).value_of_css_property(
            "color"
        )
        assert color == "rgba(255, 79, 18, 1)", "Wrong color"
        text = self.browser.find_element(*LoginPageLocators.PLACEHOLDER_LOGIN).text
        assert text == word, "Wrong text in placeholder"
        text = self.browser.find_element(*LoginPageLocators.PLACEHOLDER_PASSWORD).text
        assert text == "Пароль", "Wrong text in placeholder"

    # def should_be_autorized_user(self):
    #     assert self.element_is_present(*BasePageLocators.USER_ICON)
