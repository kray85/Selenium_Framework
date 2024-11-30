import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_driver_path = r"D:\source\PythonTesting\drivers\chromedriver-win64\chromedriver.exe"

# chrome driver
chrome_service_object = Service(chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service_object)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSSSelector, Classname, name, linkText
# try:
driver.find_element(By.NAME,'email').send_keys("johndoe@example.com")
driver.find_element(By.ID, 'exampleInputPassword1').send_keys("password")
driver.find_element(By.ID, 'exampleCheck1').click()

 # XPath //tagname[@attribute] - Xpath  -> //input[@type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(message)

# CSSSElector tagname[attribute=value] - CSSSelector  -> input[type='submit']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("John Doe")
assert "Success!" in message
driver.find_element(By.CSS_SELECTOR, '#inlineRadio1').click()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(" India")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

# static dropdown
dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
# dropdown.select_by_index(0)
dropdown.select_by_visible_text("Female")
# dropdown.select_by_value()


# except Exception as e:
#     print(e)



time.sleep(5)
