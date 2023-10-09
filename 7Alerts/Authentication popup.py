import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_authen():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

                #Authentication Alerts : we can send username and password with url

    driver.get("https://username:password@testautomationpractice.blogspot.com/")
                       #USER NAME:PASSWORD@