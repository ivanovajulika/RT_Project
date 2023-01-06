from selenium.webdriver.common.by import By


class LoginPageLocators:
    BTN_PHONE = (By.ID, "t-btn-tab-phone")
    BTN_MAIL = (By.ID, "t-btn-tab-mail")
    BTN_LOGIN = (By.ID, "t-btn-tab-login")
    BTN_LS = (By.ID, "t-btn-tab-ls")
    BTN_DEFAULT = (By.CLASS_NAME, "rt-tab--active")
    LINK_FORGOT_PASSWORD = (By.ID, "forgot_password")
    INPUT_USERNAME = (By.ID, "username")
    INPUT_PASSWORD = (By.ID, "password")
    BTN_ENTER = (By.ID, "kc-login")
    PLACEHOLDER_LOGIN = (By.XPATH, "(//*[@class='rt-input__placeholder'])[1]")
    PLACEHOLDER_PASSWORD = (By.XPATH, "(//*[@class='rt-input__placeholder'])[2]")

    LINK_VK = (By.ID, "oidc_vk")
    LINK_OK = (By.ID, "oidc_ok")
    LINK_MAIL = (By.ID, "oidc_mail")
    LINK_GOOGLE = (By.ID, "oidc_google")
    LINK_YA = (By.ID, "oidc_ya")


# class BasePageLocators:
#     USER_ICON = (By.CSS_SELECTOR, ".icon-user")
