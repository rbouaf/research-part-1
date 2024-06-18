# Import dependencies
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import requests
from bs4 import BeautifulSoup
import re
import json
import os
from urllib.parse import urlparse
import csv
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType


with open("../data/counter.txt", "r") as file:
    count = int(file.read())
with open("../data/counter.txt", "w") as file:
    file.write(str(count + 1))
print(count)


# Setting up
# Set up the proxy to use Mitmproxy
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = '127.0.0.1:8080'
proxy.ssl_proxy = '127.0.0.1:8080'

# Set up Chrome options to use Mitmproxy
chrome_options = Options()
chrome_options.add_argument('--proxy-server=http://127.0.0.1:8080')

# Initialize the WebDriver with options
driver = webdriver.Chrome(options=chrome_options)

# wait variables
wait5 = WebDriverWait(driver, 5)
wait10 = WebDriverWait(driver, 10)


######################################################################################################
# open the webpage
driver.get("https://www.instagram.com/")

username = wait10.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = wait10.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
# enter username and password
username.clear()
username.send_keys("minesweeper_enthusiast")  # username
password.clear()
password.send_keys("marco1231$")  # password
button = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()  # clicking submit button

# Logged in now

# click on not now buttons
def click_not_now_button(driver, retries=5):
    for i in range(retries):
        try:
            # Wait for the "Not Now" button to be clickable
            not_now_button = wait10.until(
                EC.element_to_be_clickable((By.XPATH,
                                            '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'))
            )
            # Click the "Not Now" button using JavaScript
            driver.execute_script("arguments[0].click();", not_now_button)
            print("Clicked 'not now' button")
            break
        except Exception as e:
            print(f"Attempt {i + 1} failed: {e}")
            time.sleep(2)  # Wait before retrying
click_not_now_button(driver)

# click on not now button
Not_Now_button = wait10.until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'))
)
Not_Now_button.click()
print("Clicked 'Not Now'")


# click on reels
# search_button = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="Reels"]')))
# search_button.click()

# this method works too
driver.get('https://www.instagram.com/reels/')
print("Opened Reels")

time.sleep(3)
######################################################################################################
# Now in REELS
reels = driver.find_element(By.CSS_SELECTOR, 'div[tabindex="0"]')
debug_counter = 0
while True:
    try:
        #debug
        time.sleep(300)
        debug_counter+=1
        print("Scrolling down "+str(debug_counter))

        # Scroll down to load more reels
        reels.send_keys(Keys.ARROW_DOWN)

        # Optionally, add a break condition to stop scrolling after a certain number of reels
    except Exception as e:
        print(f"An error occurred: {e}")
        break