import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_links():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")

    #links = driver.find_elements(By.XPATH,"//a")
                # OR                                "a" is the common  tag of all the links in web pag
    links = driver.find_element(By.TAG_NAME,"a")

    print(len(links))




