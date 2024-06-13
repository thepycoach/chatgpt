from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

web = 'https://www.adamchoi.co.uk/bttsresult/detailed'

driver = webdriver.Chrome()
driver.get(web)
driver.maximize_window()

while True:
    # Scroll down to bottom
    driver.find_element(by='xpath', value='//body').send_keys(Keys.PAGE_DOWN)
    # Get the current scroll position
    scroll_position = driver.execute_script("return window.pageYOffset + window.innerHeight;")
    scroll_height = driver.execute_script("return document.body.scrollHeight;")

    time.sleep(1)
    # Check if we have reached the end of the page
    if scroll_position >= scroll_height:
        break

driver.quit()
