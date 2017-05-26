import pytest
from selenium import webdriver
from random import randint

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd

pwd = 'secret'

def test_1_signup(driver):
    driver.get("https://sqamate.com/signup/")

    while True:
        global log
        log = 'test_' + str(randint(0, 1000)) + '@sqamate.com'
        driver.find_element_by_name("login").send_keys(log)
        driver.find_element_by_name("password").send_keys(pwd)
        driver.find_element_by_class_name('button').click()

        # если не находим алерт, то выходим из функции. Если находим алерт (т.е. уже имеется такой имэйл), то генерим
        #  имэйл заново.
        if len(driver.find_elements_by_class_name('alert')) == 0:
            print('\nСоздана учетная запись пользователя ' + log)
            return

def test_2_login(driver):
    driver.get("https://sqamate.com/login/")

    driver.find_element_by_name("login").send_keys(log)
    driver.find_element_by_name("password").send_keys(pwd)
    driver.find_element_by_class_name('button').click()