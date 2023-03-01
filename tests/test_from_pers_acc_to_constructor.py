import time
from selenium.webdriver.common.by import By
from conftest import SITE_URL,CORRECT_LOGIN,CORRECT_PASS
from locators import LoginPage,MainPage,PersonalAccount

class TestGoToConstructor():
#переход по клику на «Конструктор»
    def test_go_to_constructor_from_pers_acc(self,driver):
        driver.get(SITE_URL)
        time.sleep(2)
        driver.find_element(By.XPATH, MainPage.lk_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, LoginPage.input_email).send_keys(CORRECT_LOGIN)
        driver.find_element(By.XPATH, LoginPage.input_passw).send_keys(CORRECT_PASS)
        driver.find_element(By.XPATH, LoginPage.login_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, MainPage.lk_button).click()
        driver.find_element(By.XPATH,PersonalAccount.constructor_button).click()
        assert driver.find_element(By.XPATH, MainPage.order_button).text == "Оформить заказ"
#переход по клику на логотип Stellar Burgers
    def test_click_logo_from_pers_acc(self,driver):
        driver.get(SITE_URL)
        time.sleep(2)
        driver.find_element(By.XPATH, MainPage.lk_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, LoginPage.input_email).send_keys(CORRECT_LOGIN)
        driver.find_element(By.XPATH, LoginPage.input_passw).send_keys(CORRECT_PASS)
        driver.find_element(By.XPATH, LoginPage.login_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, MainPage.lk_button).click()
        driver.find_element(By.XPATH,MainPage.logo_svg).click()
        time.sleep(2)
        assert driver.find_element(By.XPATH, MainPage.order_button).text == "Оформить заказ"