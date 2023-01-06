from pages.login_page import LoginPage
import allure

link = "https://b2c.passport.rt.ru"


@allure.story(
    "TC_005.01 | Пользователь может авторизоваться по валидной эл.почте и валидному паролю."
)
def test_user_can_autorize(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # авторизация пользователя
    page.autorized_user_with_valid_data()
    # проверяет что пользователь авторизован
    page.should_be_autorized_user()


@allure.story(
    "TC_005.02 | Система выводит сообщение об ошибке при вводе не валидного пароля."
)
def test_error_invalid_password(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # проверяет что Кнопка "Забыл пароль" серого цвета
    page.should_be_color_grey()
    # авторизация пользователя с невалидным паролем
    page.autorized_user_with_invalid_password()
    # проверяет что Система выводит сообщение об ошибке
    page.should_be_error()


@allure.story("TC_005.03 | Система выводит капчу при вводе не валидного пароля 3 раза.")
def test_should_be_captcha(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # авторизация пользователя с невалидным паролем
    page.autorized_user_with_invalid_password()
    page.autorized_user_with_invalid_password()
    page.autorized_user_with_invalid_password()
    # проверяет что Система выводит капчу
    page.should_be_captcha()
