from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def test_demoradio():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    dtitle = driver.title
    assert dtitle == "Automation Testing Practice"
    subtitle = driver.find_element(By.XPATH,"//*[@class='title']").text
    assert subtitle == "Automation Testing Practice"
    driver.find_element(By.ID,"name").send_keys("arun")
    driver.find_element(By.ID,"email").send_keys("aru@.com")
    driver.find_element(By.ID,"phone").send_keys("12345667")
    driver.find_element(By.ID,"textarea").send_keys("AMRUTHS")
             #radio button
    select = driver.find_element(By.XPATH,"//*[@id='male']")
    select.is_selected()
    select.click()


