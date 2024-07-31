# Import dependencies
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
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

import open_reels as rls
import edge_driver as ed

driver = ed.driver

wait5 = ed.wait5
wait10 = ed.wait10
wait2 = ed.wait2

rls.open_reels()
######################################################################################################
# Now in REELS                                                                                       #
######################################################################################################

debug_counter = 0


def get_current_reel(driver):
    active_reel = driver.find_element(By.CLASS_NAME, 'xuzhngd')
    current_reel = active_reel.find_element(By.XPATH, '.. /.. /.. / ..')
    return current_reel


def scroll():
    global debug_counter
    reels = driver.find_element(By.CSS_SELECTOR, 'div[tabindex="0"]')

    # debug
    debug_counter += 1
    print("Scrolling down " + str(debug_counter))
    reels.send_keys(Keys.ARROW_DOWN)


def click_like_button(current_reel): #todo debug liking its glitchy sometimes
    # get like button
    like_button = current_reel.find_element(By.CSS_SELECTOR, '[aria-label="Like"]')
    like_button = like_button.find_element(By.XPATH, '.. /.. /.. /.. ')
    like_button.click()


def get_like_count(current_reel): #todo debug get_like_count its glitchy sometimes
    like_button = current_reel.find_element(By.CSS_SELECTOR, '[aria-label="Like"]')
    like_element = like_button.find_element(By.XPATH, '.. /.. /.. /.. /.. /.. ')
    like_count_button = like_element.find_element(By.XPATH, './*[1]')
    like_count_button = like_count_button.find_element(By.CLASS_NAME, 'html-span')
    like_count = like_count_button.text
    return like_count

def get_comment_count(current_reel): #todo debug get_comment_count its glitchy sometimes
    comment_count = current_reel.find_element(By.CSS_SELECTOR, '[aria-label="Comment"]')
    comment_count = comment_count.find_element(By.XPATH, '.. ')
    comment_count = comment_count.find_element(By.CLASS_NAME, 'html-div')
    comment_count = comment_count.find_element(By.XPATH, './*')
    comment_count = comment_count.find_element(By.XPATH, './*')
    comment_count = comment_count.find_element(By.XPATH, './*')
    comment_count = comment_count.text
    return comment_count


def leave_comment(current_reel, comment): #todo debug comment its glitchy sometimes
    comment_button = current_reel.find_element(By.CSS_SELECTOR, '[aria-label="Comment"]')
    comment_button.click()



def get_share_button(current_reel):#todo debug share its glitchy sometimes
    pass


def get_profile_button(driver):
    current_reel = get_current_reel(driver)
    element = current_reel.find_element(By.CSS_SELECTOR, '[aria-label*=" reels"]')
    get_child = element.find_element(By.XPATH, "./*")
    get_profile_name= get_child.find_element(By.XPATH, "./*[2]")
    return get_profile_name

def click_follow_button(current_reel):
    pass


def get_description(current_reel):
    pass


def get_reel_duration(driver):
    try:
        # # Execute JavaScript to get the video element
        # video_element = driver.execute_script("""
        #     return document.querySelector('.xuzhngd')
        #         .parentElement.parentElement.parentElement.parentElement
        #         .querySelector('video');
        # """)

        video_element = get_current_reel(driver)
        video_element = video_element.find_element(By.TAG_NAME, 'video')



        if video_element:
            # Get the duration of the video element
            duration = driver.execute_script("return arguments[0].duration;", video_element)
            return duration
        else:
            print("Video element not found")
            return None





    except Exception as e:
        print(f"An error occurred while getting the reel duration: {e}")
        return None


def format_seconds(time):
    minutes = int(time // 60)
    remaining_seconds = int(time % 60)
    formatted_time = f"{minutes:02d}:{remaining_seconds:02d}"
    return formatted_time

time.sleep(1)


while True:
    try:
        time.sleep(1)

        # get current reel
        current_reel = get_current_reel(driver)
        print("---["+driver.current_url+"]---")
        # like
        # click_like_button(current_reel)
        # print("+ 1 ❤️")

        # get reel data
        like_count = get_like_count(current_reel)
        comment_count = get_comment_count(current_reel)
        duration = get_reel_duration(driver)
        print("debug 3")


        # print reel data
        print("╔═══════════════════════╗ ♥ "+str(like_count))
        print("║                       ║ 🗨 "+str(comment_count))
        print("║ " + format_seconds(duration) + "          ║ 🢅")
        print("╚═══════════════════════╝ ⇓")
        uploader = get_profile_button(driver).text
        print("⬤ " + uploader + " [Fᴏʟʟᴏᴡ]")

        if duration < 1.6:
            time.sleep(duration)
        else:
            time.sleep(duration - 1.6)

        scroll()






    except Exception as e:
        print(f"An error occurred: {e}")
        break
