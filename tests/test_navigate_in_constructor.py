import time
from selenium.webdriver.common.by import By
from conftest import SITE_URL
from locators import MainPage


class TestNavigate():

#переходы к разделу Начинки
    def test_navigate_to_topping(self,driver):
        driver.get(SITE_URL)
        time.sleep(2)
        driver.find_element(By.XPATH,MainPage.topping_span).click()
        time.sleep(2)
        assert driver.find_element(By.XPATH,MainPage.topping_header).text=="Начинки"

#переходы к разделу Булки
    def test_navigate_to_bun(self,driver):
        driver.get(SITE_URL)
        time.sleep(5)
        assert driver.find_element(By.XPATH,MainPage.bun_header).text=="Булки"

#переходы к разделу Соусы
    def test_navigate_to_sauce(self,driver):
        driver.get(SITE_URL)
        time.sleep(2)
        driver.find_element(By.XPATH,MainPage.sauce_span).click()
        time.sleep(2)
        assert driver.find_element(By.XPATH,MainPage.sauce_header).text=="Соусы"