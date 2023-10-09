from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.flipkart.com")
print(" title", driver.title)
time.sleep(10)
driver.close()


# selenium3 update to selenium4  and one change has Service class.
#from selenium.webdriver.chrome.service import Service as ChromeService