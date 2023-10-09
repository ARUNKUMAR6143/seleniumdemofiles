from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def test_checkboxes():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    dtitle = driver.title
    assert dtitle == "Automation Testing Practice"
    # check boxes
    # driver.find_element(By.XPATH,"//input[@type='checkbox']").click()   # one check box

    # to select all check boxes
    all_boxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")

    # for i in range(len(all_boxes)):
    # all_boxes[i].click()

    # select multiple checkboxes by choice

    for one_box in all_boxes:
        weekname = one_box.get_attribute("id")
        if weekname == "monday" or weekname == "sunday" or weekname == "tuesday":
            one_box.click()

    time.sleep(10)
