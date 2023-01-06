from pages.login_page import LoginPage
import allure

link = "https://b2c.passport.rt.ru"


@allure.story("TC_001.01 | Меню выбора типа аутентификации - кнопка 'Телефон'")
def test_btn_phone(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # проверяет, что на странице присутствует кнопка Телефон
    page.should_be_btn_phone()
    # нажимает на кнопку Телефон и проверяет цвет текста кнопки и текст в плейсхолдере
    page.go_to_phone_btn()


@allure.story("TC_001.02 | Меню выбора типа аутентификации - кнопка 'Почта'")
def test_btn_mail(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # проверяет, что на странице присутствует кнопка Почта
    page.should_be_btn_mail()
    # нажимает на кнопку Почта и проверяет цвет текста кнопки и текст в плейсхолдере
    page.go_to_mail_btn()


@allure.story("TC_001.03 | Меню выбора типа аутентификации - кнопка 'Логин'")
def test_btn_login(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # проверяет, что на странице присутствует кнопка Логин
    page.should_be_btn_login()
    # нажимает на кнопку Логин и проверяет цвет текста кнопки и текст в плейсхолдере
    page.go_to_login_btn()


@allure.story("TC_001.04 | Меню выбора типа аутентификации - кнопка 'Лицевой счет'")
def test_btn_ls(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # проверяет, что на странице присутствует кнопка Логин
    page.should_be_btn_ls()
    # нажимает на кнопку Логин и проверяет цвет текста кнопки и текст в плейсхолдере
    page.go_to_ls_btn()


@allure.story(
    "TC_002.01 | Меню выбора типа аутентификации - По умолчанию выбрана кнопка переключения между вкладками 'Телефон'"
)
def test_btn_phone_default(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # проверяет, что кнопка по дефолту содержит текст 'Телефон'.
    page.should_be_btn_default()


@allure.story("TC_004.01 | Наличие кнопки авторизации через соц. сеть VK")
def test_user_can_go_to_vk(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # проверяет, что на странице присутствует ссылка на страницу соц.сети
    page.should_be_link_to_vk_page()
    # переходит на страницу соц.сети
    page.go_to_vk_page()


@allure.story("TC_004.02 | Наличие кнопки авторизации через соц. сеть OK")
def test_user_can_go_to_ok(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # проверяет, что на странице присутствует ссылка на страницу соц.сети
    page.should_be_link_to_ok_page()
    # переходит на страницу соц.сети
    page.go_to_ok_page()


@allure.story("TC_004.03 | Наличие кнопки авторизации через соц. сеть Mail")
def test_user_can_go_to_mail(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # проверяет, что на странице присутствует ссылка на страницу соц.сети
    page.should_be_link_to_mail_page()
    # переходит на страницу соц.сети
    page.go_to_mail_page()


@allure.story("TC_004.04 | Наличие кнопки авторизации через соц. сеть Google")
def test_user_can_go_to_google(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # проверяет, что на странице присутствует ссылка на страницу соц.сети
    page.should_be_link_to_google_page()
    # переходит на страницу соц.сети
    page.go_to_google_page()


@allure.story("TC_004.05 | Наличие кнопки авторизации через соц. сеть YA")
def test_user_can_go_to_ya(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)

    # проверяет, что на странице присутствует ссылка на страницу соц.сети
    page.should_be_link_to_ya_page()
    # переходит на страницу соц.сети
    page.go_to_ya_page()
