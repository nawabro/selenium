# test_app.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()  # replace with the path to your WebDriver if needed

driver.get("http://127.0.0.1:5000/")

client_id = driver.find_element(By.NAME, "client_id")
client_id.send_keys("123")

email = driver.find_element(By.NAME, "email")
email.send_keys("test@yahoo.com")

email.submit()

time.sleep(20)  # wait for the response to load

assert "Form submitted successfully" in driver.page_source

driver.quit()