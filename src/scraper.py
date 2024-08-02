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

import open_reels as open_reels
import edge_driver as ed

driver = ed.driver

wait5 = ed.wait5
wait10 = ed.wait10
wait2 = ed.wait2

######################################################################################################
# Now in REELS                                                                                       #
######################################################################################################



def get_current_reel(driver):
    active_reel = driver.find_element(By.CLASS_NAME, 'xuzhngd')
    current_reel = active_reel.find_element(By.XPATH, '.. /.. /.. / ..')
    return current_reel


def scroll():
    reels = driver.find_element(By.CSS_SELECTOR, 'div[tabindex="0"]')
    reels.send_keys(Keys.ARROW_DOWN)


def get_like_button(current_reel): #todo debug liking its glitchy sometimes
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

def get_follow_button(current_reel):#todo redo from scratch its too inconsistent
    pass


def get_description(current_reel):#todo redo from scratch its too inconsistent
    pass


def get_reel_duration(current_reel):
    try:
        # # Execute JavaScript to get the video element
        # video_element = driver.execute_script("""
        #     return document.querySelector('.xuzhngd')
        #         .parentElement.parentElement.parentElement.parentElement
        #         .querySelector('video');
        # """)

        video_element = current_reel.find_element(By.TAG_NAME, 'video')



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



def get_save_button(current_reel):#todo redo from scratch its too inconsistent

    pass


def visit_profile(driver):#todo redo from scratch its too inconsistent
    pass


def click_not_interested(driver):#todo redo from scratch its too inconsistent
    pass

header = [
                "account", "session", "url", "reel_like_count", "reel_comment_count",
                "reel_duration", "watch_time_seconds", "watch_time_percentage", "liked",
                "positive_comment", "followed", "shared", "saved", "visited_profile",
                "negative_comment", "not_interested", "datetime"
            ]
def scrape(username,  password, session,watch_time_percentage, liked, positive_comment, followed, shared, saved, visited_profile, negative_comment, not_interested, quit_after):
    counter=0
    global header
    with open('../data/output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)

    time.sleep(1)

    open_reels.open_reels(username, password)
    while counter<= quit_after:
        try:
            time.sleep(1)

            # get current reel
            current_reel = get_current_reel(driver)
            url = driver.current_url
            stripped_remove_instagram_com_url = url.replace("https://www.instagram.com/", "")

            print("---["+driver.current_url+"]---")

            if liked:
                get_like_button(current_reel).click()
                print("+ 1 ❤️")

            pos_com_left = 0
            if len(positive_comment) > 1:
                leave_comment(current_reel, positive_comment)
                pos_com_left = 1
                print("+ 1 👍💬")

            if followed:
                get_follow_button(current_reel).click()
                print("+ 1 🤴")

            if shared:
                get_share_button(current_reel).click()
                print("+ 1 👨‍👦")

            if saved:
                get_save_button(current_reel).click()
                print("+ 1 💾")

            if visited_profile:
                visit_profile(driver).click()
                print("Visited profile")

            neg_com_left = 0
            if len(negative_comment) > 1:
                leave_comment(current_reel, negative_comment)
                neg_com_left = 1
                print("+ 1 👎💬")

            if not_interested:
                click_not_interested(driver)
                print("Not interested")


            # todo fix get_like_count and get_comment_count
            like_count =1# = get_like_count(current_reel)
            comment_count =1#= get_comment_count(current_reel)
            duration = get_reel_duration(current_reel)
            print("Duration: " + str(duration))


            # print reel data
            # print("╔═══════════════════════╗ ♥ "+str(like_count))
            # print("║                       ║ 🗨 "+str(comment_count))
            # print("║ " + format_seconds(duration) + "          ║ 🢅")
            # print("╚═══════════════════════╝ ⇓")
            # uploader = get_profile_button(driver).text
            # print("⬤ " + uploader + " [Fᴏʟʟᴏᴡ]")

            watch_time = duration * watch_time_percentage
            if watch_time < 1.6:
                time.sleep(watch_time)
            else:
                time.sleep(watch_time - 1.6)

            datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            data = [
                [username, session, stripped_remove_instagram_com_url, like_count, comment_count, duration, watch_time,
                watch_time_percentage, liked, pos_com_left, followed, shared, saved, visited_profile, neg_com_left,
                not_interested, datetime]
            ]

            with open('../data/output.csv', 'a', newline='') as csvfile:
                csv.writer(csvfile).writerows(data)



            scroll()
            counter += 1
            print(str(counter) + " reels watched. Scrolling...")

        except Exception as e:
            print(f"An error occurred: {e}")
            break

    driver.quit()


scrape("minesweeper_enthusiast", "marco1231$", 0, 0.5, 0,
       "", 0, 0, 0, 0, "",
       0, 40)