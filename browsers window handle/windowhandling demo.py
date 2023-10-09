from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_window():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()

        #we can handles windows to know the id's first

    windowID = driver.current_window_handle  # single ------ current_window_handle
    print("onebrewserid",windowID)                              # windowsID like this 82E88D547EB84CF78A9FD3A9B1641B28

       #  we can opening another window
    driver.find_element(By.XPATH,"//img[1]").click()

    windowIDS = driver.window_handles # multiple ----- window_handles
    print("all",windowIDS)

    #  windowsids return list of 2 windows ids
    parent = windowIDS[0]
    child = windowIDS[1]
    print(parent)
    print(child)

     # now we can move one window to another window
         # Approach1
    driver.switch_to.window(parent)
    driver.switch_to.window(child)

           # Approach2
    #for wind in windowIDS:  # all windows opening one by one
        #driver.switch_to.window(wind)  #swiching one window to another window
        #print(driver.title)  # printing titles

        #based on our choice closing the window

    for wind in windowIDS:
        driver.switch_to.window(wind)
        #if driver.title == "Automation Testing Practice":        # parent close
        if driver.title == "Wikipedia, the free encyclopedia":   # child close
        #if driver.title == "Automation Testing Practice" or "Wikipedia, the free encyclopedia":
                                      #parentclose                 # childclose
                driver.close()


