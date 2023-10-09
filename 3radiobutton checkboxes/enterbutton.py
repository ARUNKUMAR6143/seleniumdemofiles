from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def test_enter():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    dtitle = driver.title
    assert dtitle == "Automation Testing Practice"

    enter = driver.find_element(By.XPATH,"//*[@id='Wikipedia1_wikipedia-search-input']")
    enter.send_keys("arun")
    enter.submit()   # enter button
    time.sleep()
