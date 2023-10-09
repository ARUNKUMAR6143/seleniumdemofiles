from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_demodrop():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    dtitle = driver.title
    assert dtitle == "Automation Testing Practice"

    drpcountry = Select(driver.find_element(By.XPATH,"//*[@id='country']"))
    #drpcountry.select_by_visible_text("India")  #india is value in dropdown
    #drpcountry.select_by_value("japan")     #japan is one of the attribute value
    #drpcountry.select_by_index(3)          # index of dropdown value

            #To capture the all options in dropdown and print
    alloptions = drpcountry.options
    print("total options :",len(alloptions))

    for opt in alloptions:
        print(opt.text)

    #select options from dropdown without using bult in meathod
    for single in alloptions:
        if single.text == "India":
            single.click()
            break
    green = driver.find_element(By.XPATH,"//*[@id='colors']/option[3]")
    print(green.text)







