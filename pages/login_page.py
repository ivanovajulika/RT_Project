from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_btn_phone(self):
        assert self.element_is_present(*LoginPageLocators.BTN_PHONE)

    def go_to_phone_btn(self):
        self.btn_mask(*LoginPageLocators.BTN_PHONE, "Мобильный телефон")

    def should_be_btn_mail(self):
        assert self.element_is_present(*LoginPageLocators.BTN_MAIL)

    def go_to_mail_btn(self):
        self.btn_mask(*LoginPageLocators.BTN_MAIL, "Электронная почта")

    def should_be_btn_login(self):
        assert self.element_is_present(*LoginPageLocators.BTN_LOGIN)

    def go_to_login_btn(self):
        self.btn_mask(*LoginPageLocators.BTN_LOGIN, "Логин")

    def should_be_btn_ls(self):
        assert self.element_is_present(*LoginPageLocators.BTN_LS)

    def go_to_ls_btn(self):
        self.btn_mask(*LoginPageLocators.BTN_LS, "Лицевой счёт")

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
        text = self.browser.find_element(*LoginPageLocators.BTN_DEFAULT).text
        assert text == "Телефон", "Wrong text"

    # def register_user(self, email="email", password="password"):
    #     email_input = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
    #     email_input.send_keys(email)
    #     password_input = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
    #     password_input.send_keys(password)
    #     password_conf_input = self.browser.find_element(
    #         *LoginPageLocators.CONFIRM_PASSWORD
    #     )
    #     password_conf_input.send_keys(password)
    #     self.browser.find_element(*LoginPageLocators.REG_BTN).click()
