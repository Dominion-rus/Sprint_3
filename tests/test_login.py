import time
from selenium.webdriver.common.by import By
from conftest import SITE_URL,CORRECT_LOGIN,CORRECT_PASS
from locators import LoginPage,MainPage,RegistrationPage
class TestLogin():
#Проверка текста на форме логина
    def test_text_on_login_form(self,driver):
        driver.get(SITE_URL + 'login')
        time.sleep(5)
        assert driver.find_element(By.XPATH,LoginPage.auth_text).text == "Вход"
        assert driver.find_element(By.XPATH,LoginPage.email_text).text == "Email"
        assert driver.find_element(By.XPATH,LoginPage.passw_text).text == "Пароль"



#вход по кнопке «Войти в аккаунт» на главной
    def test_login_from_start_page_with_button(self,driver):
        driver.get(SITE_URL)
        time.sleep(2)
        driver.find_element(By.XPATH,LoginPage.login_page_button).click()
        driver.find_element(By.XPATH,LoginPage.input_email).send_keys(CORRECT_LOGIN)
        driver.find_element(By.XPATH,LoginPage.input_passw).send_keys(CORRECT_PASS)
        driver.find_element(By.XPATH,LoginPage.login_button).click()
        time.sleep(2)
        assert driver.find_element(By.XPATH,MainPage.order_button).text == "Оформить заказ"

#вход через кнопку «Личный кабинет»
    def test_login_with_lk_button(self,driver):
        driver.get(SITE_URL)
        time.sleep(2)
        driver.find_element(By.XPATH, MainPage.lk_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, LoginPage.input_email).send_keys(CORRECT_LOGIN)
        driver.find_element(By.XPATH, LoginPage.input_passw).send_keys(CORRECT_PASS)
        driver.find_element(By.XPATH, LoginPage.login_button).click()
        time.sleep(2)
        assert driver.find_element(By.XPATH, MainPage.order_button).text == "Оформить заказ"

#вход через кнопку в форме регистрации
    def test_login_from_registrarion_form(self,driver):
        driver.get(SITE_URL + 'register')
        time.sleep(2)
        driver.find_element(By.XPATH,RegistrationPage.login_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, LoginPage.input_email).send_keys(CORRECT_LOGIN)
        driver.find_element(By.XPATH, LoginPage.input_passw).send_keys(CORRECT_PASS)
        driver.find_element(By.XPATH, LoginPage.login_button).click()
        time.sleep(2)
        assert driver.find_element(By.XPATH, MainPage.order_button).text == "Оформить заказ"

#вход через кнопку в форме восстановления пароля
    def test_login_from_recovery_passw_form(self, driver):
        driver.get(SITE_URL)
        time.sleep(2)
        driver.find_element(By.XPATH, LoginPage.login_page_button).click()
        driver.find_element(By.XPATH, LoginPage.recovery_passw_btn).click()
        driver.find_element(By.XPATH,RegistrationPage.login_button).click()
        time.sleep(2)
        driver.find_element(By.XPATH, LoginPage.input_email).send_keys(CORRECT_LOGIN)
        driver.find_element(By.XPATH, LoginPage.input_passw).send_keys(CORRECT_PASS)
        driver.find_element(By.XPATH, LoginPage.login_button).click()
        time.sleep(2)
        assert driver.find_element(By.XPATH, MainPage.order_button).text == "Оформить заказ"






