from selenium import webdriver
import time

web = 'https://www.adamchoi.co.uk/bttsresult/detailed'

driver = webdriver.Chrome()
driver.get(web)
driver.maximize_window()

time.sleep(2)
driver.save_screenshot('screenshot.png')

driver.quit()


