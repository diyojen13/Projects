from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class Test_sauce:
    def test_invalid_login(self):
        driver = webdriver.Chrome("chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        sleep(2)
        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        errorMassage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMassage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"Test Sonucu: {testResult}")

testClass = Test_sauce()
testClass.test_invalid_login()

