import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r"D:\source\PythonTesting\drivers\chromedriver-win64\chromedriver.exe"

# chrome driver
chrome_service_object = Service(chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service_object)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")


driver.find_element(By.ID, 'autosuggest').send_keys("ind")
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

next(country.click() for country in countries if country.text == "India")

try:
#
    assert driver.find_element(By.ID, 'autosuggest').get_attribute('value') == "India"
    print("Test Passed")
except AssertionError as e:
    print(e)
    print("Test Failed")

# print(driver.find_element(By.ID, 'autosuggest').text)

time.sleep(5)