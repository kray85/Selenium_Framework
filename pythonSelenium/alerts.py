import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r"D:\source\PythonTesting\drivers\chromedriver.exe"

# chrome driver
chrome_service_object = Service(chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service_object)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name = 'Batman'

driver.find_element(By.ID, 'name').send_keys(name)
driver.find_element(By.ID, 'alertbtn').click()
driver.find_element(By.ID, 'confirmbtn').click()

alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()
alert.dismiss()


time.sleep(5)