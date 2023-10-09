import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os


def test_screen():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
                            # screenshot by giving path of directory and file name

    #driver.save_screenshot("C:\\Users\lenovo\PycharmProjects\seleniumpractice\9screenshots\\homepage.png")
    #driver.quit()

                   # method os.getcwd is current working directory next give file name
   # driver.save_screenshot(os.getcwd()+"\\nxtscrnshot.png")            # method1
    #driver.get_screenshot_as_file(os.getcwd()+"\\nxtscrnshot.png")     #method2
 
                # date and time when on screenshot capture

    timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    path = os.getcwd()+"\\nxtscrnshot" + timestamp + ".png"
    driver.get_screenshot_as_file(path)  # same as second method
    time.sleep(5)
    driver.close()


