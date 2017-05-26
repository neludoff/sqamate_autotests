import pytest
from selenium import webdriver
from random import randint


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)  # what is 5? why 5?
    request.addfinalizer(wd.quit)
    return wd


host = 'https://sqamate.com'
login = 'test_' + str(randint(0, 1000)) + '@sqamate.com'  # don't use 'log' not for logs
password = 'secret'


def signup(driver):
    driver.get(host + '/signup/')

    driver = login(driver)
    if driver.find_elements_by_class_name('alert'):  # python understands [], {}, None, False, 0 as false
        print 'Created ' + login  # don't need print('...') just print ...


def login(driver):
    driver.get(host + '/login/')

    driver.find_element_by_name("login").send_keys(login)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_class_name('button').click()

    return driver  # added return driver because same code was in signup, so i reused login
