from selenium.common.exceptions import NoSuchElementException

# from .locators import BasePageLocators
from .locators import LoginPageLocators


class BasePage:
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    def tab_changes_automatically(self, method, locator, data):
        self.browser.find_element(method, locator).click()
        input = self.browser.find_element(*LoginPageLocators.INPUT_USERNAME)
        input.send_keys(data)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD).click()

    def changes_color(self, method, locator, c):
        color = self.browser.find_element(method, locator).value_of_css_property(
            "color"
        )
        assert color == c, "Wrong color"

    def changes_text(self, method, locator, word):
        text = self.browser.find_element(method, locator).text
        assert text == word, "Wrong text in placeholder"

    # def should_be_autorized_user(self):
    #     assert self.element_is_present(*BasePageLocators.USER_ICON)
