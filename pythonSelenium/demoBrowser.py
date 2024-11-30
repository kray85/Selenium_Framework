import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# Initialize Chrome options
chrome_options = Options()
# chrome_options.add_argument("--start-maximized")

# Set the path to the ChromeDriver executable
chrome_driver_path = r"D:\source\PythonTesting\drivers\chromedriver.exe"

# gecko_driver_path = r"D:\source\PythonTesting\drivers\firefox\geckodriver.exe"
# edge_driver_path = r"D:\source\PythonTesting\drivers\edge\msedgedriver.exe"

# chrome driver
service_object = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service_object, options=chrome_options)

# gecko_service_object = Service(gecko_driver_path)
# driver = webdriver.Firefox(service=gecko_service_object)

# edge_service_object = Service(edge_driver_path)
# driver = webdriver.Edge(service=edge_service_object)


driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#")

driver.back()

time.sleep(5)
driver.close()