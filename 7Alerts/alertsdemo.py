import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_alerts():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")
                #Authentication 7Alerts : we can send username and password with url
    #driver.get("https://username:password@testautomationpractice.blogspot.com/")


    driver.maximize_window()
    dtitle = driver.title
    assert dtitle == "Automation Testing Practice"

    driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button[1]").click()

    alert = driver.switch_to.alert # Alert
    print(alert.text)
    alert.accept()
    time.sleep(5)


    driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button[2]").click()
    conform_alert = driver.switch_to.alert  # conform Alert
    #conform_alert.accept()
    print(conform_alert.text)
    conform_alert.dismiss()
    time.sleep(5)


    driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button[3]").click()

    promt_alert = driver.switch_to.alert    # promt Alert
    #promt_alert.accept()
    print(promt_alert.text)
    promt_alert.send_keys("arun")
    #promt_alert.dismiss()
    time.sleep(5)




