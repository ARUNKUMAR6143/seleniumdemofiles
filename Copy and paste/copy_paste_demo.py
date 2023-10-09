from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains ,Keys
import time

def test_copypaste():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://textcompare.com/")
    driver.maximize_window()
    time.sleep(5)
                #  ctrl+A    select all
                #  ctrl+c    copy all
                #  Tab       move to paste position
                # ctrl+v    paste

    input1 = driver.find_element(By.XPATH,"//*[@name='frm_compare_1']")
    input1.send_keys("welcome arun")
    input2 = driver.find_element(By.XPATH,"//*[@name='frm_compare_2']")


    act = ActionChains(driver)  # first create the action object

                   #  ctrl+A    select all
    act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

                      #  ctrl+c    copy all
    act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

                  #  Tab       move to paste position
    act.send_keys(Keys.TAB).perform()
    input2.clear()

                       # ctrl+v    paste
    act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    time.sleep(5)

