from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains ,Keys
import time


def test_scrolling():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    dtitle = driver.title
    assert dtitle == "Automation Testing Practice"

        # scroll down by pixel
    #driver.execute_script("window.scrollBy(0,3000)","")              # javascript syntax
    #value = driver.execute_script("return window.pageYOffset;")
    #print("number:", value)  # 1720.6666259765625

          # scroll down till end
    #driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")     # javascript syntax
    #value = driver.execute_script("return window.pageYOffset;")           # finding pixel value
    #print("number:",value)
    #time.sleep(5)

            # scroll down again upwords

    #driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")  # javascript syntax
    #value = driver.execute_script("return window.pageYOffset;")            # finding pixel value
    #print("number:", value)
    #time.sleep(5)

            # scroll down page element is visible
    txt = driver.find_element(By.XPATH,"//*[@id='HTML1']/h2")
    driver.execute_script("arguments[0].scrollIntoView();",txt)       # javascript syntax
    value = driver.execute_script("return window.pageYOffset;")      # finding pixel value
    print(value)      #1417.3333740234375
    time.sleep(5)
