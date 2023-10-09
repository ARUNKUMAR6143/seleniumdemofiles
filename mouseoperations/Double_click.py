from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains ,Keys
import time


def test_double():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    dtitle = driver.title
    assert dtitle == "Automation Testing Practice"


    value = driver.find_element(By.ID,"field1") # we send the value and next double click
    value.clear()          # in field some value is there first we clear the value
    value.send_keys("arun")  # next send the value

    button = driver.find_element(By.XPATH,"//*[@ondblclick='myFunction1()']") # double click button
    action = ActionChains(driver)
    action.double_click(button).perform()  # method
    time.sleep(5)


