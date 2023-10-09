from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import datetime

def test_screen():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//*[@id='firstName']").send_keys("arun")
    driver.find_element(By.XPATH,"//*[@type='text']").send_keys("kumar")
    driver.find_element(By.ID,"userEmail").send_keys("rmnejne")

    timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")  # date to print on screenshot

    path = "scrshots/screenshot_" + timestamp + ".png"  # file location with an object
    # driver.save_screenshot(path)
    driver.get_screenshot_as_file(path)  # screenshoot


