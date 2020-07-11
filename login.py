from selenium import webdriver

import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("file:///C:/Users/admin/Desktop/Crazy%20foods/assignment/index.html")

driver.maximize_window()

time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/span[1]/ol/div[1]/a").click()

driver.find_element_by_xpath("/html/body/div[2]/div/span[2]/div/div[1]/div/form/input[1]").send_keys("harpreet_kaur@gmail.com")

driver.find_element_by_name("password").send_keys("Punjab@123")

time.sleep(2)

driver.find_element_by_xpath("/html/body/div[2]/div/span[2]/div/div[1]/div/form/button").click()

time.sleep(2)

driver.quit()
