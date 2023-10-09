import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_img():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")



    images = driver.find_elements(By.XPATH,"//img")
               #OR
    #images = driver.find_elements(By.TAG_NAME,"img")

    print(len(images))
    for img in images:
        print(img.text)

    time.sleep(5)
    count = 0
    for img in images:
        value = img.get_attribute("src")
        res = requests.head(value)
        if res.status_code == 200:
            print(value,"valid")
            count+= 1
    else:
        print(value,"invald")
    print("valid images",count)