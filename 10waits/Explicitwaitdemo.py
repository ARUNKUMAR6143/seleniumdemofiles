import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_explicit():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
              #Explicit wait work on the condition when we require

    my_wait = WebDriverWait(driver,10) #we create exelicit wait once time with an object

    dtitle = driver.title
    assert dtitle == "Automation Testing Practice"
    subtitle = driver.find_element(By.XPATH, "//*[@class='title']").text
    assert subtitle == "Automation Testing Practice"
    driver.find_element(By.ID, "name").send_keys("arun")
    driver.find_element(By.ID, "phone").send_keys("12345667")
    driver.find_element(By.ID, "textarea").send_keys("AMRUTHS")

    # when synchronous problem on webelement to find it by using the explicit wait

    syn_problem = my_wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='male']"))) # not using find elements
    syn_problem.click()
    # it will search element by condition not time