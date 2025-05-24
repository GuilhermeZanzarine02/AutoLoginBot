import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
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

    def fill_login_Username(self):
        drive = self.driver
        campo = drive.find_element(By.ID, 'user-name')
        username = "standard_user"
        for letra in username:
            campo.send_keys(letra)
            time.sleep(round(random.uniform(0.1, 0.2), 3))
        
    def fill_login_password(self):
        drive = self.driver
        campo = drive.find_element(By.ID, 'password')
        password = "secret_sauce"
        for letra in password:
            campo.send_keys(letra)
            time.sleep(round(random.uniform(0.1, 0.2), 3))