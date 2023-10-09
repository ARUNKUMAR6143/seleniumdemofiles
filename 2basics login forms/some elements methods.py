from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
print(driver.title)
#elements methods

print(driver.current_url)
print(driver.page_source)

hdg = driver.find_element(By.XPATH,"//*[@align='center']/h1").text
print(hdg)
driver.find_element(By.LINK_TEXT,"Register").click()
hdg = driver.find_element(By.XPATH,"//*[@class='container center']/child::h2").text
print(hdg)
name = driver.find_element(By.XPATH,"//*[@placeholder='First Name']")

# elements methods its retun true or false
print(name.is_displayed())  # is there or not
print(name.is_enabled())    # working or not
print(name.is_selected())   # selected or not used to check boxes
print(name.location)        # locations its return x , y values
name.submit()               # enter button
name.get_attribute()        # its get attributes value of element form html

