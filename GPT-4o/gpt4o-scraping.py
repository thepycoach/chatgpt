from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openai import OpenAI
import time

web = 'https://www.adamchoi.co.uk/bttsresult/detailed'

driver = webdriver.Chrome()
driver.get(web)
driver.maximize_window()

time.sleep(2)

while True:
    test = driver.get_screenshot_as_base64()
    # Scroll down to bottom
    driver.find_element(by='xpath', value='//body').send_keys(Keys.PAGE_DOWN)
    # Get the current scroll position
    scroll_position = driver.execute_script("return window.pageYOffset + window.innerHeight;")
    scroll_height = driver.execute_script("return document.body.scrollHeight;")

    client = OpenAI(api_key='paste api here')

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You're a data analyst. Extract the information from the tables. Return only the data in JSON format"
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{test}"
                        }
                    }
                ]
            }
        ],
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response.choices[0].message.content)

    # Check if we have reached the end of the page
    if scroll_position >= scroll_height:
        break

driver.quit()



