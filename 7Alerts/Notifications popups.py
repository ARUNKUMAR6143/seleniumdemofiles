from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_notif():
    # notifications popups can handle with browser setting
    ops = webdriver.ChromeOptions()
    ops.add_argument("--disable-notifications")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


    driver.get("https://whatmylocation.com/")


    driver.maximize_window()
