import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
def test_sel_demo():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com")
    time.sleep(5)
    all_links = driver.find_elements(By.TAG_NAME,"a")
    print("size = ", len(all_links))
    try:
        with open("facebook_in_links.txt", "a", encoding = "Utf-8") as f: # creating a file and store the data
            for link in all_links:
                actlink = link.get_attribute("href")
                resp = requests.get(actlink)
                if resp.status_code == 200:
                    f.write(link.text+"\t"+actlink+"\n")
    except:
        print("error")



