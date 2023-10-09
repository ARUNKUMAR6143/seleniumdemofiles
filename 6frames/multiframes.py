import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_frames2():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("https://ui.vision/demo/webtest/frames/")
    print("\nTitle : ", driver.title)
    time.sleep(3)
    driver.switch_to.frame(0) # enter into first frame

    driver.find_element(By.XPATH,"//*[@id='id1']/div/input").send_keys("arun")

    driver.switch_to.default_content() # exit from the frame first frame
    time.sleep(3)

    driver.switch_to.frame(1) # enter in to second frame
    driver.find_element(By.XPATH, "//*[@id='id2']/div/input").send_keys("123")
    time.sleep(3)

    driver.switch_to.default_content()  # exit from the frame second frame
