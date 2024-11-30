import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

chrome_driver_path = r"D:\source\PythonTesting\drivers\chromedriver.exe"

# chrome driver
chrome_service_object = Service(chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service_object)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element(By.CSS_SELECTOR, 'input.search-keyword').send_keys('ber')

time.sleep(2)

# Some validation
results = driver.find_elements(By.XPATH, '//div[@class="products"]/div')

for value in actualList:
    print(value)

count = len(results)
assert count == 3

for result in results:
    actualList.append(result.find_element(By.XPATH, 'h4').text)
    result.find_element(By.XPATH, "div/button").click()

assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR, 'img[alt="Cart"]').click()
driver.find_element(By.XPATH,'//button[text()="PROCEED TO CHECKOUT"]').click()


#  Some validation
prices = driver.find_elements(By.CSS_SELECTOR, 'tr td:nth-child(5) p')
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)
totalAmount =  int(driver.find_element(By.CSS_SELECTOR, '.totAmt').text)

assert sum == totalAmount


driver.find_element(By.CSS_SELECTOR, '.promoCode').send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'promoInfo')))
print(driver.find_element(By.CLASS_NAME, 'promoInfo').text)


discountedAmount = float(driver.find_element(By.CSS_SELECTOR, '.discountAmt').text)

assert totalAmount > discountedAmount


time.sleep(2)