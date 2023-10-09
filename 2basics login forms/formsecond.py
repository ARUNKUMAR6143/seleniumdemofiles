from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='firstName']").send_keys("arun")
driver.find_element(By.XPATH,"//*[@type='text']").send_keys("kumar")
driver.find_element(By.ID,"userEmail").send_keys("rmnejne")
driver.find_element(By.XPATH," (//*[@name='exp'])[1]").click()
hdng = driver.find_element(By.XPATH, "//*[@id='mainContent']/h1[1]").text
assert hdng == "Selenium - Automation Practice Form"
time.sleep(5)
driver.close()
