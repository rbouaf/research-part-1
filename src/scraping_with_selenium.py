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

# specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome()

# wait variables
wait5 = WebDriverWait(driver, 5)
wait10 = WebDriverWait(driver, 10)

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


############################################################################################################

# not_button = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]')))
# Assuming you have already logged in and are on the "Save Login Info" screen
# try:
#     # Wait for the "Save Login Info" button and click "Not Now"
#     not_now_button = wait10.until(
#         EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))
#     )
#     not_now_button.click()
# except Exception as e:
#     print("Error encountered:", e)

# try:
#     # Wait for the "Save Login Info" button and click "Not Now"
#     not_now_button = wait10.until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[role="button"][tabindex="0"]'))
#     )
#     not_now_button.click()
# except Exception as e:
#     print("Error encountered:", e)

# Print page source for debugging
# print(driver.page_source)

# try:
#     # Wait for the "Not Now" button to be clickable and then click it
#     not_now_button = wait10.until(
#         EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now") or contains(text(), "Not now")]'))
#     )
#     not_now_button.click()
# except Exception as e:
#     print("Error encountered:", e)

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

time.sleep(5)


reels = driver.find_element(By.CSS_SELECTOR, 'div[tabindex="0"]')
counter = 0
while True:
    try:
        # Wait for the reel video element to be present and then find it
        # reel_element = wait5.until(EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]//video')))
        #
        # # Perform actions on the reel element if needed (e.g., extracting information)
        # # Example: print the reel source URL
        # print(reel_element.get_attribute('src'))

        # # Wait for a few seconds to simulate viewing the reel
        # time.sleep(3)

        # Move to the next reel by simulating a right arrow key press
        counter+=1
        print("Scrolling down "+str(counter))
        reels.send_keys(Keys.ARROW_DOWN)
        time.sleep(3)

        # Optionally, add a break condition to stop scrolling after a certain number of reels
    except Exception as e:
        print(f"An error occurred: {e}")
        break