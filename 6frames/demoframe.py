import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_frame():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    dtitle = driver.title
    assert dtitle == "Automation Testing Practice"

        #we can find the how many frames avaiable in web page by search ifames

    driver.switch_to.frame("frame-one796456169")# enter into frame with id attribute value of the frame
    #driver.switch_to.frame(0)  #enter into frame with index of the frame
    #driver.switch_to.frame(#name attribute value)
    #driver.switch_to.frame(#webelement)

    driver.find_element(By.XPATH,"//*[@id='RESULT_TextField-0']").send_keys("arun")
    driver.find_element(By.XPATH,"(//*[@id='q2']/table/tbody/tr[1]/td/label)[1]").click()
    driver.find_element(By.XPATH,"(//*[@id='q2']/table/tbody/tr[2]/td/label)[1]").click()

    driver.switch_to.default_content() # exit out of the frame

    time.sleep(5)
