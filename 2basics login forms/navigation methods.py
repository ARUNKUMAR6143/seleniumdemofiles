from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.browserstack.com/guide/handle-web-tables-in-selenium")
driver.maximize_window()
print("\nTitle ",driver.title)
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Documentation").click()
time.sleep(5)

driver.back()
time.sleep(5)

# navigations commands
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.close()