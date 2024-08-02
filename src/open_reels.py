from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
import time
from seleniumwire import webdriver
from seleniumwire.utils import decode as decodesw
from bs4 import BeautifulSoup
import re
import json
import os
from urllib.parse import urlparse
import csv
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import edge_driver as ed

driver = ed.driver

wait5 = ed.wait5
wait10 = ed.wait10
wait2 = ed.wait2


def open_reels(username, password):
    driver.get("https://www.instagram.com/")
    print("[ instagram.com ]")
    # logging in
    username_field = wait10.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password_field = wait10.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    # enter username
    username_field.clear()
    username_field.send_keys(username)
    # enter password
    password_field.clear()
    password_field.send_keys(password)
    print("[ " + username + " ]")
    print("[ *************** ]")
    # submit
    wait2.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    print("       [ SUBMIT ]")


    # click on not now button 1
    for i in range(5):
        try:
            # Wait for the "Not Now" button to be clickable
            # not_now_button = wait10.until(
            #     EC.element_to_be_clickable((By.XPATH
            #                                 ,
            #                                 '//*[@id="mount_0_0_ty"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div'))
            # )
            element_text = "Not now"
            not_now_button = wait10.until(EC.element_to_be_clickable((By.XPATH, f"//*[text()='{element_text}']")))

            # Click the "Not Now" button using JavaScript
            # driver.execute_script("arguments[0].click();", not_now_button)
            not_now_button.click()
            print(">[ Not now ]<")
            break
        except Exception as e:
            print(f"Attempt {i + 1} failed: {e}")
            time.sleep(2)

    # click on not now button 2
    Not_Now_button = wait10.until(EC.element_to_be_clickable
                                  ((By.XPATH,
                                    '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
    Not_Now_button.click()
    print(">[ Not Now ]<")

    # open reels
    driver.get('https://www.instagram.com/reels/')
    print("Opened Reels")






# with open("../data/logging_client_events/counter.txt", "r") as file:
#     count = int(file.read())
# with open("../data/logging_client_events/counter.txt", "w") as file:
#     file.write(str(count + 1))
# print(count)
# with open("../data/logging_client_events/counter.txt", "r") as file:
#     count_updated = int(file.read())
# print(count_updated)

# Setting up
# Set up the proxy to use Mitmproxy
# proxy = Proxy()
# proxy.proxy_type = ProxyType.MANUAL
# proxy.http_proxy = '127.0.0.1:8080'
# proxy.ssl_proxy = '127.0.0.1:8080'

# Set up Chrome options to use Mitmproxy
# edge_options = Options()
# # edge_options.add_argument('--proxy-server=http://127.0.0.1:8080')
# # chrome_options.add_argument('--headless')  # Enable headless mode
# # chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
# edge_options.add_argument('--no-sandbox')  # Bypass OS security model
# edge_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
#
# driver = webdriver.Edge(options=edge_options)
#
# # wait variables
# wait5 = WebDriverWait(driver, 5)
# wait10 = WebDriverWait(driver, 10)
# wait2 = WebDriverWait(driver, 2)





# click on reels
# search_button = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="Reels"]')))
# search_button.click()
# this method works too
