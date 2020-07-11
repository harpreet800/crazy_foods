from selenium import webdriver

import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("file:///C:/Users/admin/Desktop/Crazy%20foods/assignment/index.html")

driver.maximize_window()

time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/span[1]/ol/div[3]/a").click()

time.sleep(2)
driver.quit()