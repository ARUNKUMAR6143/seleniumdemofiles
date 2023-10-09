import time

from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_mouse():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    driver.maximize_window()
    a = driver.title
    print(a)
          # Right click
    admin = driver.find_element(By.LINK_TEXT,"Admin")
    action = ActionChains(driver)
    action.context_click(admin)    # right click by context_click method