import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r"D:\source\PythonTesting\drivers\chromedriver-win64\chromedriver.exe"

# chrome driver
chrome_service_object = Service(chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service_object)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
radiobuttons = driver.find_elements(By.XPATH, "//input[@type='radio']")

next(checkbox.click() for checkbox in checkboxes if checkbox.get_attribute('value') == "option2")

# Implicit selection of radio button
# next(radiobutton.click() for radiobutton in radiobuttons if radiobutton.get_attribute('value') == "radio2")

# Explicit selection of radio button
radioButtons =  driver.find_elements(By.CSS_SELECTOR, ".radioButton" )
radioButtons[1].click()


assert driver.find_element(By.ID, 'displayed-text').is_displayed()
driver.find_element(By.ID, 'hide-textbox').click()
assert not driver.find_element(By.ID, 'displayed-text').is_displayed()


# Java popups



# try:
#     # assert checkboxes[1].is_selected()
#     # assert radiobuttons[1].is_selected()
#     # assert not radioButtons[1].is_selected()
#     assert display_el
#     assert hide_txt_button
#     # assert not display_el
#     print("Test Passed")
# except AssertionError as e:
#     print("Test Failed")
#     print(e)

time.sleep(5)