from pages.login_page import LoginPage

link = "https://b2c.passport.rt.ru"


def test_btn_phone(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # открывает страницу
    page.open_page()
    # проверяет, что на странице присутствует кнопка Телефон
    page.should_be_btn_phone()
    # нажимает на кнопку Телефон и проверяет цвет текста кнопки и текст в плейсхолдере
    page.go_to_phone_btn()


def test_btn_mail(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # открывает страницу
    page.open_page()
    # проверяет, что на странице присутствует кнопка Почта
    page.should_be_btn_mail()
    # нажимает на кнопку Почта и проверяет цвет текста кнопки и текст в плейсхолдере
    page.go_to_mail_btn()


def test_btn_login(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # открывает страницу
    page.open_page()
    # проверяет, что на странице присутствует кнопка Логин
    page.should_be_btn_login()
    # нажимает на кнопку Логин и проверяет цвет текста кнопки и текст в плейсхолдере
    page.go_to_login_btn()


def test_btn_ls(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # открывает страницу
    page.open_page()
    # проверяет, что на странице присутствует кнопка Логин
    page.should_be_btn_ls()
    # нажимает на кнопку Логин и проверяет цвет текста кнопки и текст в плейсхолдере
    page.go_to_ls_btn()


# Тест проверяет, что пользователь может перейти на страницу авторизации соц.сети VK
def test_user_can_go_to_vk(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # открывает страницу
    page.open_page()
    # проверяет, что на странице присутствует ссылка на страницу соц.сети
    page.should_be_link_to_vk_page()
    # переходит на страницу соц.сети
    page.go_to_vk_page()


# Тест проверяет, что пользователь может перейти на страницу авторизации соц.сети OK
def test_user_can_go_to_ok(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # открывает страницу
    page.open_page()
    # проверяет, что на странице присутствует ссылка на страницу соц.сети
    page.should_be_link_to_ok_page()
    # переходит на страницу соц.сети
    page.go_to_ok_page()


# Тест проверяет, что пользователь может перейти на страницу авторизации соц.сети MAIL
def test_user_can_go_to_mail(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # открывает страницу
    page.open_page()
    # проверяет, что на странице присутствует ссылка на страницу соц.сети
    page.should_be_link_to_mail_page()
    # переходит на страницу соц.сети
    page.go_to_mail_page()


# Тест проверяет, что пользователь может перейти на страницу авторизации соц.сети GOOGLE
def test_user_can_go_to_google(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # открывает страницу
    page.open_page()
    # проверяет, что на странице присутствует ссылка на страницу соц.сети
    page.should_be_link_to_google_page()
    # переходит на страницу соц.сети
    page.go_to_google_page()


# Тест проверяет, что пользователь может перейти на страницу авторизации соц.сети YA
def test_user_can_go_to_ya(browser):
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # открывает страницу
    page.open_page()
    # проверяет, что на странице присутствует ссылка на страницу соц.сети
    page.should_be_link_to_ya_page()
    # переходит на страницу соц.сети
    page.go_to_ya_page()
