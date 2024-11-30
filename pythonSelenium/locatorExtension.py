import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()


chrome_driver_path = r"D:\source\PythonTesting\drivers\chromedriver-win64\chromedriver.exe"

service_object = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service_object, options=chrome_options)


driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
# XPATH Button
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# Find Button by Text
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()







time.sleep(10)