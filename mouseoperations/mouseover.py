import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_mouse():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    driver.maximize_window()
    a = driver.title
    print(a)
    admin  =  driver.find_element(By.LINK_TEXT,"Admin").click()
    user  =   driver.find_element(By.XPATH,"//*[@class='oxd-topbar-body-nav-tab --parent']").click()
    users  =  driver.find_element(By.XPATH,"//*[@class='oxd-dropdown-menu']/li").click()

    action = ActionChains(driver)
    action.move_to_element(admin).move_to_element(user).move_to_element(users).perform()


    time.sleep(5)
