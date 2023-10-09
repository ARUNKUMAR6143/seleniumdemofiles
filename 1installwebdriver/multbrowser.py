from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import time

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
driver.get("https://www.flipkart.com")
print(" title", driver.title)
time.sleep(10)
driver.close()



driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get("https://www.flipkart.com")
print(" title", driver.title)
time.sleep(10)
driver.close()


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://www.flipkart.com")
driver.get("https://www.amazon.in")
print(" title", driver.title)
time.sleep(10)
driver.close()
