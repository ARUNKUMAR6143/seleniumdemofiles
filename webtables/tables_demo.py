from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
import time

def test_verify_tbl1():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()
    fb_title  = driver.title
    assert fb_title == "DEMOQA"
    print("\nTitle ",driver.title)
    time.sleep(5)

    table = driver.find_element(By.XPATH,"//*[@class='rt-table']")   #table body
    tbody = table.find_element(By.XPATH,"//*[@class='rt-tbody']")    # table body no header
    tr_groups = tbody.find_elements(By.XPATH,"//*[@class='rt-tr-group']")  # coloums
    print(len(tr_groups))
    for tr_group in tr_groups:
        li = tr_group.text.split("\n")
        print(li)


def test_verify_tbl2():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://demo.guru99.com/test/web-table-element.php")
    driver.maximize_window()
    fb_title  = driver.title
    assert fb_title == "Web Table Elements"
    print("\nTitle ",driver.title)
    time.sleep(5)

    table = driver.find_element(By.XPATH,"//*[@class='dataTable']")
    tbody = table.find_element(By.TAG_NAME,"tbody")
    trs = tbody.find_elements(By.TAG_NAME,"tr")
    print(len(trs))
    for tr in trs:
        tds = tr.find_elements(By.TAG_NAME,"td")
        li=[]
        print(len(tds))
        for td in tds:
            li.append(td.text)
        print(li)