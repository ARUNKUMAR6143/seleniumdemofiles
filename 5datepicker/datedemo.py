import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_date():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    dtitle = driver.title
    assert dtitle == "Automation Testing Practice"
    driver.find_element(By.XPATH,"//*[@id='datepicker']").click()
    year = "2026"
    month = "January"
    date = "10"
    # we first select month and year
    while True:
        mon = driver.find_element(By.XPATH,"//*[@class='ui-datepicker-title']/span").text
        yea =  driver.find_element(By.XPATH,"//*[@class='ui-datepicker-title']/span[2]").text
        if mon == month and yea == year:
            break  # when month and year match the loop will break
        else:
            # when month and year not matching then go to next
            driver.find_element(By.XPATH,"//a[@title='Next']/span").click() # forword click the arrow for next
    time.sleep(10)
            #driver.find_element(By.XPATH,"//a[@class='ui-datepicker-prev ui-corner-all']/span").click()# back word
                     # now select the date from all dates

    all_dates = driver.find_elements(By.XPATH,"//*[@class ='ui-datepicker-calendar']/tbody/tr/td/a")
    print(all_dates)
    for one_date in all_dates:
        if one_date.text == date:
            one_date.click()
            break

    time.sleep(10)







