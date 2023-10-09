import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_innerframe():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://demoqa.com/nestedframes")
    driver.maximize_window()
    outer = driver.find_element(By.ID,"frame1") # entering in to frame by element method
    driver.switch_to.frame(outer)   # outer

    inner = driver.find_element(By.XPATH,"//*[@srcdoc='<p>Child Iframe</p>']") # entering into inner
    driver.switch_to.frame(inner)   # inner

    innerframe_text = driver.find_element(By.XPATH,"/html/body/p") # inner frame text
    print(innerframe_text.text)

    # now we are in the inner frame

    driver.switch_to.parent_frame()  # inner frame to outer frame

    driver.switch_to.default_content()  # outer frame to our main web page

     # now start the find web elements
