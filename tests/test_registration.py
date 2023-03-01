import time
from selenium.webdriver.common.by import By
from locators import RegistrationPage
from conftest import generate_login,generate_password,SITE_URL,USER_NAME,SHORT_PASS

class TestRegistration:
    def test_text_on_form_registration(self,driver):
        driver.get(SITE_URL+'register')
        time.sleep(5)
        assert driver.find_element(By.XPATH,RegistrationPage.reg_text).text == "Регистрация"
        assert driver.find_element(By.XPATH,RegistrationPage.name_text).text =="Имя"
        assert driver.find_element(By.XPATH,RegistrationPage.email_text).text =="Email"
        assert driver.find_element(By.XPATH,RegistrationPage.passw_text).text == "Пароль"

    def test_correct_registration(self,driver):
        driver.get(SITE_URL + 'register')
        time.sleep(5)
        driver.find_element(By.XPATH,RegistrationPage.input_name).send_keys(USER_NAME)
        driver.find_element(By.XPATH,RegistrationPage.input_email).send_keys(generate_login())
        driver.find_element(By.XPATH,RegistrationPage.input_passw).send_keys(generate_password())
        driver.find_element(By.XPATH,RegistrationPage.button_reg).click()
        time.sleep(5)
        current_url = driver.current_url
        assert current_url == SITE_URL + 'login'

    def test_short_password_registration(self,driver):
        driver.get(SITE_URL + 'register')
        time.sleep(2)
        driver.find_element(By.XPATH, RegistrationPage.input_name).send_keys(USER_NAME)
        driver.find_element(By.XPATH, RegistrationPage.input_email).send_keys(generate_login())
        driver.find_element(By.XPATH, RegistrationPage.input_passw).send_keys(SHORT_PASS)
        driver.find_element(By.XPATH, RegistrationPage.button_reg).click()
        time.sleep(2)
        assert driver.find_element(By.XPATH,RegistrationPage.incorrect_passw_text).text=="Некорректный пароль"






