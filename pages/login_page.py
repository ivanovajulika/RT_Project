from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
from .data import Data


class LoginPage(BasePage):
    def should_be_btn_phone(self):
        assert self.element_is_present(*LoginPageLocators.BTN_PHONE)

    def go_to_phone_btn(self):
        self.browser.find_element(*LoginPageLocators.BTN_PHONE).click()
        self.changes_color(*LoginPageLocators.BTN_PHONE, "rgba(255, 79, 18, 1)")
        self.changes_text(*LoginPageLocators.PLACEHOLDER_LOGIN, "Мобильный телефон")
        self.changes_text(*LoginPageLocators.PLACEHOLDER_PASSWORD, "Пароль")

    def should_be_btn_mail(self):
        assert self.element_is_present(*LoginPageLocators.BTN_MAIL)

    def go_to_mail_btn(self):
        self.browser.find_element(*LoginPageLocators.BTN_MAIL).click()
        self.changes_color(*LoginPageLocators.BTN_MAIL, "rgba(255, 79, 18, 1)")
        self.changes_text(*LoginPageLocators.PLACEHOLDER_LOGIN, "Электронная почта")
        self.changes_text(*LoginPageLocators.PLACEHOLDER_PASSWORD, "Пароль")

    def should_be_btn_login(self):
        assert self.element_is_present(*LoginPageLocators.BTN_LOGIN)

    def go_to_login_btn(self):
        self.browser.find_element(*LoginPageLocators.BTN_LOGIN).click()
        self.changes_color(*LoginPageLocators.BTN_LOGIN, "rgba(255, 79, 18, 1)")
        self.changes_text(*LoginPageLocators.PLACEHOLDER_LOGIN, "Логин")
        self.changes_text(*LoginPageLocators.PLACEHOLDER_PASSWORD, "Пароль")

    def should_be_btn_ls(self):
        assert self.element_is_present(*LoginPageLocators.BTN_LS)

    def go_to_ls_btn(self):
        self.browser.find_element(*LoginPageLocators.BTN_LS).click()
        self.changes_color(*LoginPageLocators.BTN_LS, "rgba(255, 79, 18, 1)")
        self.changes_text(*LoginPageLocators.PLACEHOLDER_LOGIN, "Лицевой счёт")
        self.changes_text(*LoginPageLocators.PLACEHOLDER_PASSWORD, "Пароль")

    def should_be_link_to_vk_page(self):
        assert self.element_is_present(*LoginPageLocators.LINK_VK)

    def go_to_vk_page(self):
        self.browser.find_element(*LoginPageLocators.LINK_VK).click()
        assert "auth.vk.com" in self.browser.current_url, "wrong url"

    def should_be_link_to_ok_page(self):
        assert self.element_is_present(*LoginPageLocators.LINK_OK)

    def go_to_ok_page(self):
        self.browser.find_element(*LoginPageLocators.LINK_OK).click()
        assert "connect.ok.ru" in self.browser.current_url, "wrong url"

    def should_be_link_to_mail_page(self):
        assert self.element_is_present(*LoginPageLocators.LINK_MAIL)

    def go_to_mail_page(self):
        self.browser.find_element(*LoginPageLocators.LINK_MAIL).click()
        assert "connect.mail.ru" in self.browser.current_url, "wrong url"

    def should_be_link_to_google_page(self):
        assert self.element_is_present(*LoginPageLocators.LINK_GOOGLE)

    def go_to_google_page(self):
        self.browser.find_element(*LoginPageLocators.LINK_GOOGLE).click()
        assert "accounts.google.com" in self.browser.current_url, "wrong url"

    def should_be_link_to_ya_page(self):
        assert self.element_is_present(*LoginPageLocators.LINK_YA)

    def go_to_ya_page(self):
        self.browser.find_element(*LoginPageLocators.LINK_YA).click()
        assert "yandex.ru/auth" in self.browser.current_url, "wrong url"

    def should_be_btn_default(self):
        self.changes_text(*LoginPageLocators.BTN_DEFAULT, "Телефон")

    def should_be_tab_changes_mail_in_phone(self):
        self.tab_changes_automatically(*LoginPageLocators.BTN_PHONE, Data.email)
        self.changes_color(*LoginPageLocators.BTN_MAIL, "rgba(255, 79, 18, 1)")
        self.changes_color(*LoginPageLocators.BTN_PHONE, "rgba(16, 24, 40, 1)")
        self.changes_text(*LoginPageLocators.PLACEHOLDER_ACTIVE, "Электронная почта")

    def should_be_tab_changes_login_in_phone(self):
        self.tab_changes_automatically(*LoginPageLocators.BTN_PHONE, Data.login)
        self.changes_color(*LoginPageLocators.BTN_LOGIN, "rgba(255, 79, 18, 1)")
        self.changes_color(*LoginPageLocators.BTN_PHONE, "rgba(16, 24, 40, 1)")
        self.changes_text(*LoginPageLocators.PLACEHOLDER_ACTIVE, "Логин")

    def should_be_tab_changes_phone_in_mail(self):
        self.tab_changes_automatically(*LoginPageLocators.BTN_MAIL, Data.phone)
        self.changes_color(*LoginPageLocators.BTN_PHONE, "rgba(255, 79, 18, 1)")
        self.changes_color(*LoginPageLocators.BTN_MAIL, "rgba(16, 24, 40, 1)")
        self.changes_text(*LoginPageLocators.PLACEHOLDER_ACTIVE, "Мобильный телефон")

    def should_be_tab_changes_login_in_mail(self):
        self.tab_changes_automatically(*LoginPageLocators.BTN_MAIL, Data.login)
        self.changes_color(*LoginPageLocators.BTN_LOGIN, "rgba(255, 79, 18, 1)")
        self.changes_color(*LoginPageLocators.BTN_MAIL, "rgba(16, 24, 40, 1)")
        self.changes_text(*LoginPageLocators.PLACEHOLDER_ACTIVE, "Логин")

    def should_be_tab_changes_ls_in_mail(self):
        self.tab_changes_automatically(*LoginPageLocators.BTN_MAIL, Data.ls)
        self.changes_color(*LoginPageLocators.BTN_LS, "rgba(255, 79, 18, 1)")
        self.changes_color(*LoginPageLocators.BTN_MAIL, "rgba(16, 24, 40, 1)")
        self.changes_text(*LoginPageLocators.PLACEHOLDER_ACTIVE, "Лицевой счёт")

    def should_be_tab_changes_mail_in_ls(self):
        self.tab_changes_automatically(*LoginPageLocators.BTN_LS, Data.email)
        self.changes_color(*LoginPageLocators.BTN_MAIL, "rgba(255, 79, 18, 1)")
        self.changes_color(*LoginPageLocators.BTN_LS, "rgba(16, 24, 40, 1)")
        self.changes_text(*LoginPageLocators.PLACEHOLDER_ACTIVE, "Электронная почта")

    def should_be_tab_changes_login_in_ls(self):
        self.tab_changes_automatically(*LoginPageLocators.BTN_LS, Data.login)
        self.changes_color(*LoginPageLocators.BTN_LOGIN, "rgba(255, 79, 18, 1)")
        self.changes_color(*LoginPageLocators.BTN_LS, "rgba(16, 24, 40, 1)")
        self.changes_text(*LoginPageLocators.PLACEHOLDER_ACTIVE, "Логин")

    def autorized_user_with_valid_data(self):
        self.browser.find_element(*LoginPageLocators.BTN_MAIL).click()
        email_input = self.browser.find_element(*LoginPageLocators.INPUT_USERNAME)
        email_input.send_keys(Data.email)
        password_input = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD)
        password_input.send_keys(Data.password)
        self.browser.find_element(*LoginPageLocators.BTN_ENTER).click()

    def autorized_user_with_invalid_password(self):
        self.browser.implicitly_wait(10)
        self.browser.find_element(*LoginPageLocators.BTN_MAIL).click()
        email_input = self.browser.find_element(*LoginPageLocators.INPUT_USERNAME)
        email_input.send_keys(Data.email)
        password_input = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD)
        password_input.send_keys(Data.invalid_password)
        self.browser.find_element(*LoginPageLocators.BTN_ENTER).click()

    def should_be_autorized_user(self):
        assert self.element_is_present(*BasePageLocators.BTN_LK)
        assert self.element_is_present(*BasePageLocators.BTN_LOGOUT)

    def should_be_color_grey(self):
        self.changes_color(
            *LoginPageLocators.LINK_FORGOT_PASSWORD, "rgba(16, 24, 40, 0.5)"
        )

    def should_be_error(self):
        self.changes_color(
            *LoginPageLocators.LINK_FORGOT_PASSWORD, "rgba(255, 79, 18, 1)"
        )
        assert self.element_is_present(*LoginPageLocators.LINK_ERROR)
        self.changes_text(*LoginPageLocators.LINK_ERROR, "Неверный логин или пароль")

    def should_be_captcha(self):
        assert self.element_is_present(*LoginPageLocators.CAPTCHA)
