
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_date():
    driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.flipkart.com")
    print(" title", driver.title)
