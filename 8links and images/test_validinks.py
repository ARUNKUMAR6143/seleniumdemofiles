
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_valid():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")
    links = driver.find_elements(By.TAG_NAME,'a')

    print(len(links))

    for link in links:
        print(link.text)

    count = 0
    for link in links:
        url = link.get_attribute("href")  # href is the attribute common of all the links
        res = requests.head(url)            # import requests
        if res.status_code <= 200:        # checking the status codes
            print(url,"valid")
            count+=1
        else:
            print(url,"broken link")

    print("valid links",count)