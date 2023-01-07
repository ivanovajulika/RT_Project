from pages.login_page import LoginPage
from pages.registr_page import RegistrPage
import allure
import pytest


def generate_string(n):
    return "д" * n


link = "https://b2c.passport.rt.ru"


@allure.story(
    "TC_007.01 | Форма 'Авторизации' - Ввод валидных данных в поле для ввода имени."
)
@pytest.mark.parametrize(
    "name",
    [
        generate_string(2),
        generate_string(3),
        generate_string(15),
        generate_string(29),
        generate_string(30),
        "Анна-Мария",
        " Анна",
        "Мария ",
        "МАРИЯ",
    ],
    ids=[
        "2 symbols",
        "3 symbols",
        "15 symbols",
        "29 symbols",
        "30 symbols",
        "with -",
        "begin space",
        "end space",
        "uper",
    ],
)
def test_input_name_pozitive(browser, name):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # переходит на страницу регистрации
    page.go_registration()
    # создает экземпляр страницы регистрации
    page = RegistrPage(browser, link)
    # вводит имя в поле Имя и проверяет наличие сообщения об ошибке
    page.input_name(name)


@allure.story(
    "TC_007.02 | Форма 'Авторизации' - Ввод не валидных данных в поле для ввода имени."
)
@pytest.mark.parametrize(
    "name",
    [
        "",
        "д",
        generate_string(31),
        generate_string(255),
        generate_string(1000),
        "Anna",
        "Анна-Мария-Антуанетта",
        "!№;%:?*()",
        "12345",
        "Карл5",
        "Анна Мария",
    ],
    ids=[
        "empty",
        "1 symbols",
        "31 symbols",
        "255 symbols",
        "1000 symbols",
        "Latin symbols",
        "with 2 -",
        "special_chars",
        "digit",
        "symbols with digit",
        "with space",
    ],
)
@pytest.mark.xfail
def test_input_name_negative(browser, name):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # переходит на страницу регистрации
    page.go_registration()
    # создает экземпляр страницы регистрации
    page = RegistrPage(browser, link)
    # вводит имя в поле Имя и проверяет наличие сообщения об ошибке
    page.input_name(name)
