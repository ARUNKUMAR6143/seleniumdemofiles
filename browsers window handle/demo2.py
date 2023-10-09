from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_windowdemo():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("https://www.flipkart.com/")
    print("parent Title : ", driver.title)
    time.sleep(10)
    driver.find_element(By.XPATH, "//*[@class='_2KpZ6l _2doB4z']").click()
    driver.find_element(By.NAME, "q").send_keys("mobiles")
    driver.find_element(By.XPATH, "//*[@width='20']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@class='_2KpZ6l _2doB4z'").click()
    time.sleep(5)


    pw = driver.current_window_handle   # parent      # single window
    print("parent ",pw)
    cw_list = driver.window_handles             # multiple tabs / windows
    for cw in cw_list:  # all windows
        print("child ",cw) # printing one by one window
        if cw !=pw:
            driver.switch_to.window(cw)
            print("child title", driver.title)
            driver.find_element(By.XPATH,"//*[text()='NOTIFY ME' or text()='Add to cart']").click()
            time.sleep(10)
            driver.close()
    driver.switch_to.window(pw)
    time.sleep(5)
    driver.quit()
