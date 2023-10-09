from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains ,Keys
import time

def test_drag():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    dtitle = driver.title
    assert dtitle == "Automation Testing Practice"

    # creating actionchains object
    action = ActionChains(driver)
    source = driver.find_element(By.ID,"draggable")
    traget = driver.find_element(By.XPATH,"//*[@class='ui-widget-header ui-droppable']")

    action.drag_and_drop(source,traget).perform()
    time.sleep(10)