import random
import pytest
from selenium import webdriver

SITE_URL = "https://stellarburgers.nomoreparties.site/"
USER_NAME='TestUSer'
CORRECT_LOGIN= 'fatal1ty2013@yandex.ru'
CORRECT_PASS=  'Arzsow'
INCORRECT_PASS='Arzsow123'
SHORT_PASS='123'

#Генератор Email
def generate_login():
    return USER_NAME + str(random.randrange(100,999)) + '@yandex.ru'

#Генератор паролей
def generate_password():
    return USER_NAME + str(random.randrange(100,9999))


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(SITE_URL)

    yield driver

    driver.quit()



