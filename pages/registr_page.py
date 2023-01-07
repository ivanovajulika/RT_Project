from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegistrPageLocators
from .data import Data


class RegistrPage(BasePage):
    def input_name(self, name):
        input = self.browser.find_element(*RegistrPageLocators.INPUT_FIRSTNAME)
        input.send_keys(name)
        self.browser.find_element(*RegistrPageLocators.BTN_REGISTR).click()
        assert not self.element_is_present(*RegistrPageLocators.ERR)
