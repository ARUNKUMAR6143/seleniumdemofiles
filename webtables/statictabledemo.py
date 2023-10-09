from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def test_static():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    dtitle = driver.title
    assert dtitle == "Automation Testing Practice"

    # no of rows in table
    no_rows = driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr") #
    print(len(no_rows))

    for ro_row in no_rows:
        li = ro_row.text.split("\n")
        print(li)
                # no of coloums in table   finding first header clonum all down are same

    no_coloums = driver.find_elements(By.XPATH, "//table[@name='BookTable']//th")
    print(len(no_coloums))
                        # specific rows and coloum data

    data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[6]/td[1]").text
    print(data)








