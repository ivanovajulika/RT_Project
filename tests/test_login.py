from pages.login_page import LoginPage



@allure.story(
    "TC_005.01 | Форма 'Авторизации' - Пользователь может авторизоваться по валидной эл.почте и валидному паролю."
)
def test_user_can_autorize_valid_email(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # авторизация пользователя
    page.autorized_user_with_valid_email()
    # проверяет что пользователь авторизован
    page.should_be_autorized_user()


@allure.story(
    "TC_005.02 | Форма 'Авторизации' - Система выводит сообщение об ошибке при вводе не валидного пароля."
)
def test_error_invalid_password(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # проверяет что Кнопка "Забыл пароль" серого цвета
    page.should_be_color_grey()
    # авторизация пользователя с невалидным Паролем
    page.autorized_user_with_invalid_password()
    # проверяет что Система выводит сообщение об ошибке и кнопка "Забыл пароль" оранжевого цвета
    page.should_be_error()


@allure.story(
    "TC_005.03 | Форма 'Авторизации' - Система выводит сообщение о пустом поле при вводе пустого Email."
)
def test_error_empty_email(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # авторизация пользователя с пустым Email
    page.autorized_user_with_empty_email()
    # проверяет что Система выводит сообщение об ошибке
    page.should_be_error_empty_email()


@allure.story(
    "TC_005.04 | Форма 'Авторизации' - Пользователь может авторизоваться по валидному логину и валидному паролю."
)
def test_user_can_autorize_valid_login(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # авторизация пользователя
    page.autorized_user_with_valid_login()
    # проверяет что пользователь авторизован
    page.should_be_autorized_user()
