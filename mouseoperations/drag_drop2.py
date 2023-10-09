import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_f1():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    actions = ActionChains(driver)

    driver.get("https://www.redbus.in/")
    print("\nTitle : ", driver.title)

    source = driver.find_element(By.XPATH,"//*[@id='src']")
    source.send_keys("Kukatpally")
    time.sleep(3)
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(10)
    driver.close()

def test_f2():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("https://jqueryui.com/droppable/")
    print("\nTitle : ", driver.title)
    time.sleep(5)

    driver.switch_to.frame(0)  #iframe
    time.sleep(5)

    source = driver.find_element(By.XPATH,"//*[@id='draggable']")
    target = driver.find_element(By.XPATH,"//*[@id='droppable']")
    time.sleep(5)

    actions = ActionChains(driver)
    actions.drag_and_drop(source,target).perform()

    time.sleep(10)
    driver.close()

"""
driver.switch_to().alert()
driver.switch_to().frame()
driver.switch_to().window()
"""