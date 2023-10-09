from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains ,Keys
import time


def test_sliders():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    dtitle = driver.title
    assert dtitle == "Automation Testing Practice"

    min = driver.find_element(By.XPATH,"//*[@id='slider']/span")
    print(min.location) #{'x': 762, 'y': 1096}

    slid =  driver.find_element(By.ID,'slider')
    print(slid.location)  # {'x': 771, 'y': 1100}

    action = ActionChains(driver)
    action.drag_and_drop_by_offset(min, 900, 0).perform()

    print(slid.location)

    time.sleep(10)


