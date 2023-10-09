import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import waits

def test_implicit():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()

    # once we write the implicity wait it can be applicable for every line.

    driver.implicitly_wait(10)  # 10 is milli seconds
    dtitle = driver.title
    assert dtitle == "Automation Testing Practice"
    subtitle = driver.find_element(By.XPATH, "//*[@class='title']").text
    assert subtitle == "Automation Testing Practice"
    driver.find_element(By.ID, "name").send_keys("arun")
    driver.find_element(By.ID, "email").send_keys("aru@.com")
    driver.find_element(By.ID, "phone").send_keys("12345667")
    driver.find_element(By.ID, "textarea").send_keys("AMRUTHS")
    select = driver.find_element(By.XPATH, "//*[@id='male']")
    select.is_selected()
    select.click()