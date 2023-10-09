from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

ops = webdriver.ChromeOptions()
ops.headless == True


driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
driver.get("https://www.facebook.com")
driver.maximize_window()
fb_title = driver.title
assert fb_title == "Facebook – log in or sign up"
print(" title", driver.title)
time.sleep(5)
driver.find_element(By.ID,"email").send_keys("aeuns@gamil.com")
driver.find_element(By.NAME,"pass").send_keys("aeuns@gamil.com")
driver.find_element(By.XPATH,"//*[@name='login']").click()
time.sleep(10)
driver.close()