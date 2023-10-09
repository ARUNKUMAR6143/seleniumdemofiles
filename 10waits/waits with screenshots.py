
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime

def test_selectdemo():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
     # using implicity wait and explicit wait

    driver.implicitly_wait(5)  # implicit

    wait = WebDriverWait(driver, 10)  #expilicit wait with object

    driver.get("http://fratelloinnotech.com")
    print("\nTitle : ", driver.title)
    try:
        wait.until(
            EC.presence_of_element_located((By.LINK_TEXT,"Internships"))).click()
        hdng = driver.find_element(By.XPATH,"//*[@class='ol-about-us-right']//h2[@class='ol-title']")
        print(hdng.text)
        stream = Select(driver.find_element(By.ID, "stream"))
        for option in stream.options:
            print(option.text)
        stream.select_by_visible_text("Mca")
    except Exception as ex: #NoSuchElementException
       # print(ex)
        timestamp= datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") # date to print on screenshot

        path = "scrshots/screenshot_"+timestamp+".png" # file location with an object
        #driver.save_screenshot(path)
        driver.get_screenshot_as_file(path) # screenshoot


    time.sleep(10)
    driver.close()


