import time
from selenium.webdriver.common.by import By
from conftest import SITE_URL,CORRECT_LOGIN,CORRECT_PASS
from locators import LoginPage,MainPage,PersonalAccount


class TestPersonalAcc():

#переход по клику на «Личный кабинет»
    def test_transition_to_personal_account(self,driver):
        driver.get(SITE_URL)
        time.sleep(2)
        driver.find_element(By.XPATH, MainPage.lk_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, LoginPage.input_email).send_keys(CORRECT_LOGIN)
        driver.find_element(By.XPATH, LoginPage.input_passw).send_keys(CORRECT_PASS)
        driver.find_element(By.XPATH, LoginPage.login_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, MainPage.lk_button).click()
        time.sleep(5)
        assert driver.find_element(By.XPATH,PersonalAccount.info_text).text == "В этом разделе вы можете изменить свои персональные данные"