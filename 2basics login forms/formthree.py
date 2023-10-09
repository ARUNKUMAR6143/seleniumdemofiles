from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
driver.maximize_window()
test_verify = driver.find_element(By.XPATH,"//*[contains(text(),'Selenium - Automation ')]")
assert test_verify == "Selenium - Automation Practice Form"
driver.find_element(By.NAME,"firstname").send_keys("arun")
driver.find_element(By.NAME,"lastname").send_keys("kundeti")
driver.find_element(By.NAME,"sex").click()
driver.find_element(By.NAME,"exp").click()
driver.find_element(By.NAME,"profession").click()
time.sleep(5)