import time
from selenium.webdriver.common.by import By
from conftest import SITE_URL,CORRECT_LOGIN,CORRECT_PASS
from locators import LoginPage,MainPage,PersonalAccount

class TestLogout():
#выход по кнопке «Выйти» в личном кабинете
    def test_logout_from_pers_acc(self,driver):
        driver.get(SITE_URL)
        time.sleep(2)
        driver.find_element(By.XPATH, MainPage.lk_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, LoginPage.input_email).send_keys(CORRECT_LOGIN)
        driver.find_element(By.XPATH, LoginPage.input_passw).send_keys(CORRECT_PASS)
        driver.find_element(By.XPATH, LoginPage.login_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, MainPage.lk_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH,PersonalAccount.logout_button).click()
        time.sleep(2)
        assert driver.find_element(By.XPATH, LoginPage.auth_text).text == "Вход" and driver.current_url == SITE_URL + 'login'