# Run with C:\Users\User\Developments\PycharmProjects\comp396\.venv\Scripts\python.exe -m src.maincol
import textwrap
import time
import csv
import os

from selenium import webdriver
from PIL import Image
from io import BytesIO
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from input.keys.credentials import aws_access_key_id, aws_secret_access_key
import drivers.driver_chrome as cdriver

import src.open_ig as open_reels
from src.aws import upload_to_s3
from src.categorizor import categorize_images

driver = cdriver.driver

wait5 = cdriver.wait5
wait10 = cdriver.wait10
wait2 = cdriver.wait2

actions = ActionChains(driver)

profile_button = None
profile_name = None

count = 0
path_to_counter = os.path.join("output", "lra", "screenshots", "counter.txt")
with open(path_to_counter, "r") as file:
    count = int(file.read())
with open(path_to_counter, "w") as file:
    file.write(str(count + 1))
global_counter = count

# Important functions
def get_current_reel(driver):
    active_reel = driver.find_element(By.CLASS_NAME, 'xuzhngd')
    current_reel = active_reel.find_element(By.XPATH, '.. /.. /.. / ..')
    return current_reel


def scroll():
    # get document body
    body = driver.find_element(By.TAG_NAME, 'body')
    # click on the body to focus
    body.click()
    body.send_keys(Keys.ARROW_DOWN)


# More complex behaviors
def visit_profile(profile_button):

    pass


def get_reel_duration(current_reel):
    try:
        video_element = current_reel.find_element(By.TAG_NAME, 'video')
        if video_element:
            duration = driver.execute_script("return arguments[0].duration;", video_element)
            return duration
        else:
            print("Video element not found")
            return None

    except Exception as e:
        print(f"An error occurred while getting the reel duration: {e}")
        return None

header = [
    "UPLOADER", "LR"
]
localcounter = 0
thumbnails = []
def upload_file():
    path = os.path.join("output", "lra", "screenshots")
    upload_to_s3(f'{path}{global_counter}sc{localcounter}-new.png',
                 'socialcomputing',
                 f'ig_reels/{global_counter}sc{localcounter}-new.png',
                 aws_access_key_id,
                 aws_secret_access_key)
def open_profile():
    current_reel = driver.find_element(By.CLASS_NAME, 'xuzhngd')
    parent_div = current_reel.find_element(By.XPATH, '.. /.. /..')

    profile_button = parent_div.find_element(By.CSS_SELECTOR, 'img[alt*="profile picture"]')
    print("got profile button")
    user_disorganized = profile_button.get_attribute('alt')
    profile_name = user_disorganized.split(' profile picture')[0]
    print(profile_name)
    profile_button.click()
    print("Arrived at profile")



def scrape(username, password, quit_after):
    global localcounter
    def format_seconds(sometime):
        minutes = int(sometime // 60)
        remaining_seconds = int(sometime % 60)
        formatted_time = f"{minutes:02d}:{remaining_seconds:02d}"
        return formatted_time

    reels_counter = 0
    global header
    pcomlft = 0
    ncomlft = 0


    open_reels.open_reels(username, password)

    actions.move_by_offset(100, 100).click().perform()

    while reels_counter < quit_after:
        try:
            time.sleep(1)
            localcounter += 1

            # get current reel
            current_reel = get_current_reel(driver)
            parent_div = current_reel.find_element(By.XPATH, '.. /.. /..')

            reel_info = driver.execute_script(
                'return Array.from(arguments[0].querySelectorAll(\'span\')).map(el => el.textContent);'
                , current_reel
            )
            seen = set()
            reel_data = [x for x in reel_info if not (x in seen or seen.add(x))]
            expand_caption = False
            if '… more' in reel_data:
                expand_caption = True

            for e in reel_data:
                # this is not elegant but more readable.
                if e == '' or e == ' ' or e == '\n' or e == '•' or e == '•' or e == '… more' or e == 'Like':
                    reel_data.remove(e)
            reel_data = [e for e in reel_data if 'Original audio' not in e]
            if reel_data[-2] == 'Likes':
                reel_data[-2] = -1

            profile_name = reel_data[0]
            open_profile()
            time.sleep(3)


            driver.execute_script("document.body.style.zoom='60%'")



            element = driver.find_element(By.CSS_SELECTOR, "main > *:first-child")

            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(1)

            png = driver.get_screenshot_as_png()
            img = Image.open(BytesIO(png))

            location = element.location
            size = element.size

            left = location['x']
            top = location['y']
            right = left + size['width']
            bottom = top + size['height']

            left = max(0, left)
            top = max(0, top)
            right = min(img.width, right)
            bottom = min(img.height, bottom)

            element_screenshot = img.crop((left, top, right, bottom))
            path_to_sc = os.path.join("output", "lra", "screenshots")
            element_screenshot.save(path_to_sc + f'{global_counter}sc{localcounter}-new.png')
            thumbnails = [f'https://socialcomputing.s3.amazonaws.com/ig_reels/{global_counter}sc{localcounter}-new.png']

            time.sleep(1)
            upload_file()

            driver.back()
            time.sleep(2)
            driver.execute_script("document.body.style.zoom='100%'")
            time.sleep(2)
            scroll()
            time.sleep(2)

            result = categorize_images(thumbnails)
            bias = ''
            result = [x.upper() for x in result]
            if 'LEFT' in result:
                bias = 'L'
            elif 'RIGHT' in result:
                bias = 'R'
            elif 'APOLITICAL' in result:
                bias = 'A'


            #
            # ######## trimming process ######
            # seen = set()
            # reel_data = [x for x in reel_info if not (x in seen or seen.add(x))]
            # expand_caption = False
            # if '… more' in reel_data:
            #     expand_caption = True
            #
            # for e in reel_data:
            #     # this is not elegant but more readable.
            #     if e == '' or e == ' ' or e == '\n' or e == '•' or e == '•' or e == '… more' or e == 'Like':
            #         reel_data.remove(e)
            # reel_data = [e for e in reel_data if 'Original audio' not in e]
            # if reel_data[-2] == 'Likes':
            #     reel_data[-2] = -1
            #
            # url = driver.current_url
            # stripped_remove_instagram_com_url = url.replace("https://www.instagram.com/", "")
            #
            # duration = get_reel_duration(current_reel)
            #
            # # PRINT ###################################################################################################
            # print("╭─────────────────────────────────────────────────────")
            # print("│ " + driver.current_url + " • " + format_seconds(duration))
            # print("│ ⬤ " + reel_data[0] + " • [Fᴏʟʟᴏᴡ]")
            # wrapped_text = textwrap.fill(reel_data[1], 52)
            # formatted_lines = [f"│ {line} " for line in wrapped_text.splitlines()]
            # print('\n'.join(formatted_lines))
            # print("│ ♥ " + str(reel_data[-2]) + " 🗨 " + str(reel_data[-1]) + " ▮" + " 🢅 ")
            # print("╰─────────────────────────────────────────────────────")
            # ###########################################################################################################


            data = [
                [reel_data[0], bias]
            ]
            path_to_lra = os.path.join("output", "lra", "lra_dataset.csv")
            with open(path_to_lra, 'a', newline='', encoding='utf-8') as csvfile:
                csv.writer(csvfile).writerows(data)


            reels_counter += 1
            print(str(reels_counter) + " reels watched. Scrolling...")

        except Exception as e:
            print(f"An error occurred: {e}")
            break

    driver.quit()