from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

class test_work:
    def nologin(self):
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(1)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)
    
    def nopassword(self):
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(1)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("")
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)

    def kayitlikullanici(self):
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(1)
        usernameInput.send_keys("locked_out_user")
        sleep(1)
        passwordInput.send_keys("secret_sauce")
        sleep(1)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)

    def hataButon(self):
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(1)
        usernameInput.send_keys(" ")
        passwordInput.send_keys(" ")
        sleep(1)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(1)
        errorBtn = driver.find_element(By.CLASS_NAME, "error-button")
        errorBtn.click()
        sleep(2)

    def testSayfa(self):
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(1)
        usernameInput.send_keys("standard_user")
        sleep(1)
        passwordInput.send_keys("secret_sauce")
        sleep(1)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(3)
        
    def inventory(self):
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(1)
        usernameInput.send_keys("standard_user")
        sleep(1)
        passwordInput.send_keys("secret_sauce")
        sleep(1)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(1)
        lengthOfInventory = driver.find_elements(By.CLASS_NAME,"inventory_item_name")
        print(f"Bu sayfada {len(lengthOfInventory)} tane urun bulunmaktadir.")


testClass = test_work()
testClass.nologin()
testClass.nopassword()
testClass.kayitlikullanici()
testClass.hataButon()
testClass.testSayfa()
testClass.inventory()