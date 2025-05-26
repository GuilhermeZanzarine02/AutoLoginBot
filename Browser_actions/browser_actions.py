import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService

class Web:
    def __init__(self):
        self.driver = self

    def open_web_site(self):
        service = EdgeService(executable_path=r"C:\Users\gleme\Downloads\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=service)
        url = "https://www.saucedemo.com/"
        driver.get(url)
        driver.maximize_window()
        time.sleep(2)
        self.driver = driver

    def fill_login_field(self, field_id, text):
        drive = self.driver
        campo = drive.find_element(By.ID, field_id)
        for letra in text:
            campo.send_keys(letra)
            time.sleep(round(random.uniform(0.1, 0.2), 3))

    def click_button(self, field_id):
        drive = self.driver
        button = drive.find_element(By.ID, field_id)
        time.sleep(1.5)
        button.click()
    
    def fill_login(self):
        self.fill_login_field('user-name', 'standard_user')
        self.fill_login_field('password', 'secret_sauce')
        self.click_button('login-button')

    def select_product(self):
        drive = self.driver

        products = {
            0 : drive.find_element(By.ID, "add-to-cart-sauce-labs-backpack"),
            1 : drive.find_element(By.ID, "add-to-cart-sauce-labs-bike-light"),
            2 : drive.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            3 : drive.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket"),
            4 : drive.find_element(By.ID, "add-to-cart-sauce-labs-onesie"),
            5 : drive.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
        }

        quantidade = random.randint(1, 3)

        sample = random.sample(list(products.keys()), quantidade)

        print(sample)

        for i in sample:
            products[i].click()
            time.sleep(2)

        cart_link = drive.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_link.click()

        time.sleep(4)
        checkout = drive.find_element(By.ID, "checkout")
        checkout.click()

    def fill_checkou_informations(self, id_field, text):
        drive = self.driver

        frist_name = drive.find_element(By.ID, id_field)
        for letra in text:
            frist_name.send_keys(letra)
            time.sleep(round(random.uniform(0.1, 0.2), 3))
    
    def fill_checkout(self):
        drive = self.driver

        self.fill_checkou_informations("first-name", "Guilherme")
        self.fill_checkou_informations("last-name", "Zanzarine")
        self.fill_checkou_informations("postal-code", "02306000")

        continue_button = drive.find_element(By.ID, "continue")
        time.sleep(1.5)
        continue_button.click()

        finish_button = drive.find_element(By.ID, "finish")
        time.sleep(1.5)
        finish_button.click()

        
        
            



      
            
            
        
   