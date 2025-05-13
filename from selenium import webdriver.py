from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service('/path/to/chromedriver.exe')  # Update with the correct path to your chromedriver
driver = webdriver.Chrome(service=service)

driver.find("://www.google.com")

time.sleep(10) 

driver.quit()
# This code opens Google Chrome and navigates to Google.com, then waits for 10 seconds before closing the browser.

