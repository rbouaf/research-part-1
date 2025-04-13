import textwrap

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv

import scraper_simulated_user.open_ig as open_reels
import drivers.driver_chrome as CHROME_DRIVER
import scraper_simulated_user.conditions as conditions
# Import dependencies
from selenium import webdriver
from PIL import Image
from io import BytesIO
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.chrome.service import Service

from data_input.keys.credentials import aws_access_key_id, aws_secret_access_key

from src.aws import upload_to_s3
from src.categorize import categorize_images
driver = CHROME_DRIVER.driver

wait5 = CHROME_DRIVER.wait5
wait10 = CHROME_DRIVER.wait10
wait2 = CHROME_DRIVER.wait2


# bug fixed, when search by style, you have to use style*="value" instead of style="value" for contains() search
import os
from openai import OpenAI

#internal imports
from data_input.topic_list.topic_list import list_topics
from data_input.keys.openai_key import openai_api_key

with open('../data_input/topic_list/topic_list.txt', 'r') as file: topics = file.read()
os.environ["OPENAI_API_KEY"] = openai_api_key
def counter():
    with open("junk/sc_counter.txt", "r") as file:
        count = int(file.read())
    with open("junk/sc_counter.txt", "w") as file:
        file.write(str(count + 1))
    return count


global_counter = counter()


def categorize_images(thumbnails):
  descriptions = []
  errors = []
  n=0
  for thumbnail in thumbnails:
    completion = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {"role": "system",
          "content": [{"type": "text",
                      "text":
                      "You are a precise image analyst. YOU ABSOLUTELY MUST PICK 3  OF THE MOST RELEVANT TOPICS FROM THE FOLLOWING LIST: "+(topics)+" . DO NOT SAY ANYTHING IF ITS NOT A TOPIC FROM THIS LIST. IF YOU DONT KNOW EXACTLY, TAKE A GUESS, IT DOESNT HAVE TO BE PERFECT. IF THE PICTURE HAS A CAPTION, IT POSSIBLY INCLUDES THE 'COMEDY' TOPIC."}],
        },
          {
            "role": "user",
            "content": [
              {
                "type": "text",
                "text": "WHAT IS IN THE SET OF IMAGES? DESCRIBE IT USING 3 TOPICS FROM THE AFORMENTIONED LIST, IN THIS FORMAT: topic1, topic2, topic3"
              },
              {
                "type": "image_url",
                "image_url": {
                  "url": thumbnail # use current thumbnail url from the array
                }
              }
            ]
          }
        ]
    )
  cur_post = completion.choices[0].message.content.split(", ")
  for index, value in enumerate(cur_post):
    if value not in list_topics:
            errors.append(f"Invalid topic at image {n}, {index}, contained {value} from {cur_post}")

  descriptions.append(completion.choices[0].message.content)
  n+=1

  print(descriptions)
  print(errors)

# Important functions
def get_current_reel(driver):
    active_reel = driver.find_element(By.CLASS_NAME, 'xuzhngd')
    current_reel = active_reel.find_element(By.XPATH, '.. /.. /.. / ..')
    return current_reel


def scroll():
    # get document body
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.ARROW_DOWN)


# clicking on elements (harder than it seems)
def click_like(current_reel):  #todo debug liking its glitchy sometimes
    # get like button
    like_button = current_reel.find_element(By.CSS_SELECTOR, '[aria-label="Like"]')
    like_button = like_button.find_element(By.XPATH, '.. /.. /.. /.. ')
    like_button.click()


def click_follow(current_reel):
    # divs = current_reel.find_elements(By.TAG_NAME, 'div')
    # follow = None
    # for d in divs:
    #     if d.text.strip() == "Follow":
    #         follow = d
    #         break
    #
    # if follow:
    #     while True:
    #         print(follow.text.strip() + " - not following yet")
    #         driver.execute_script("arguments[0].focus(); arguments[0].click();", follow)
    #         time.sleep(1)
    #         if follow.text == "Following":
    #             break
    #
    # else:
    #     print('Element not found')
    #     return None

    # driver.execute_script("const elements = arguments[0].querySelectorAll('div');const targetText = 'Follow';"
    #                       "elements.forEach(element => {"
    #                       "if (element.textContent.trim() === targetText) {"
    #                       "targetElement = element;}});"
    #                       "targetElement.click();"
    #                       "targetElement.click();"
    #                       , current_reel)
    # "var event = new KeyboardEvent('keydown', { key: 'Enter', keyCode: 13, bubbles: true });"
    # "targetElement.dispatchEvent(event);"

    # const elements = document.querySelector('.xuzhngd').parentElement.parentElement.parentElement.parentElement.querySelectorAll('div');
    #
    # const targetText = 'Follow';
    # let targetElement = null;
    #
    # elements.forEach(element => {
    #   if (element.textContent.trim() === targetText) {
    #     targetElement = element;
    #   }
    # });
    # console.log(targetElement);
    # targetElement.focus()
    # var event = new KeyboardEvent('keydown', { key: 'Enter', keyCode: 13, bubbles: true });
    # targetElement.dispatchEvent(event);
    pass


def click_not_interested(current_reel):  #todo redo from scratch its too inconsistent
    pass


def click_save(current_reel):  #todo debug save its glitchy sometimes
    pass


# More complex behaviors
def visit_profile(profile_button):  #todo redo from scratch its too inconsistent
    pass


def leave_comment(current_reel, comment):  #todo debug comment its glitchy sometimes
    comment_button = current_reel.find_element(By.CSS_SELECTOR, '[aria-label="Comment"]')
    comment_button.click()


def share(current_reel):  #todo debug share its glitchy sometimes
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

def upload_file():
    upload_to_s3(f'data/screenshots/{global_counter}sc{localcounter}-new.png',
                 'socialcomputing',
                 f'ig_reels/{global_counter}sc{localcounter}-new.png',
                 aws_access_key_id,
                 aws_secret_access_key)

left = 575
top = 25
right = 1560
bottom = 1125
client = OpenAI()
localcounter = 0
thumbnails = []
global left_profile_list
global right_profile_list
global leftover_errorcheck
profile_button = None
profile_name = None

def get_political_alignment():
    global left_profile_list, right_profile_list, leftover_errorcheck
    current_reel = driver.find_element(By.CLASS_NAME, 'xuzhngd')
    print("got current reel")
    # get parent div
    parent_div = current_reel.find_element(By.XPATH, '.. /.. /..')
    print("got parent div")
    profile_button = parent_div.find_element(By.CSS_SELECTOR, 'img[alt*="profile picture"]')
    print("got profile button")
    user_disorganized = profile_button.get_attribute('alt')
    profile_name = user_disorganized.split(' profile picture')[0]
    print(profile_name)
    profile_button.click()
    print("Arrived at profile")
    time.sleep(5)
    driver.execute_script("document.body.style.zoom='50%'")
    png = driver.get_screenshot_as_png()
    im = Image.open(BytesIO(png))
    im = im.crop((left, top, right, bottom))
    im.save('data/screenshots/' + f'{global_counter}sc{localcounter}-new.png')

    thumbnails = [f'https://socialcomputing.s3.amazonaws.com/ig_reels/{global_counter}sc{localcounter}-new.png']
    print(thumbnails)

    time.sleep(1)
    upload_file()

    # Categorize the images using OpenAI's GPT-4o model, checks for errors, and prints
    print(categorize_images(thumbnails))
    result = categorize_images(thumbnails)
    # I will then, depending on what the categorize function returns, either save the username, or not
    if result == 'LEFT':
        left_profile_list += profile_name
        if result == 'RIGHT':
            right_profile_list += profile_name
        else:
            leftover_errorcheck += profile_name

    print(len(left_profile_list))
    print(len(right_profile_list))
    print(len(leftover_errorcheck))
    # then, I'll return to the reels page
    driver.get('https://www.instagram.com/reels/')
    print("Went back to Reels")


header = [
    "username","session","account", "alignment", "followers"
]



def scrape(username, password, session, watch_time_percentage, liked, pos_comment_left,
           followed, shared, saved, profile_visited,
           neg_comment_left, clicked_not_interested, quit_after, condition):
    def format_seconds(time):
        minutes = int(time // 60)
        remaining_seconds = int(time % 60)
        formatted_time = f"{minutes:02d}:{remaining_seconds:02d}"
        return formatted_time

    counter = 0
    global header
    pcomlft = 0
    ncomlft = 0

    time.sleep(1)

    open_reels.open_reels(username, password)

    actions = ActionChains(driver)
    actions.move_by_offset(100, 100).click().perform()

    while counter <= quit_after:
        try:
            time.sleep(1)
            # get current reel
            current_reel = get_current_reel(driver)

            reel_info = driver.execute_script(
                'return Array.from(arguments[0].querySelectorAll(\'span\')).map(el => el.textContent);'
                , current_reel
            )

            ######## trimming process ######
            seen = set()
            reel_data = [x for x in reel_info if not (x in seen or seen.add(x))]
            for e in reel_data:
                # this is not elegant but more readable.
                if e == '' or e == ' ' or e == '\n' or e == '•' or e == '•' or e == '… more' or e == 'Like':
                    reel_data.remove(e)
            reel_data = [e for e in reel_data if 'Original audio' not in e]
            if reel_data[-2] == 'Likes':
                reel_data[-2] = -1

            url = driver.current_url
            stripped_remove_instagram_com_url = url.replace("https://www.instagram.com/", "")

            duration = get_reel_duration(current_reel)
            print("╭─────────────────────────────────────────────────────")
            print("│ " + driver.current_url + " • " + format_seconds(duration))
            print("│ ⬤ " + reel_data[0] + " • [Fᴏʟʟᴏᴡ]")
            wrapped_text = textwrap.fill(reel_data[1], 52)
            formatted_lines = [f"│ {line} " for line in wrapped_text.splitlines()]
            print('\n'.join(formatted_lines))
            print("│ ♥ " + str(reel_data[-2]) + " 🗨 " + str(reel_data[-1]) + " ▮" + " 🢅 ")
            print("╰─────────────────────────────────────────────────────")


            alignment = get_political_alignment(current_reel)


            watch_time = duration * watch_time_percentage
            print(format_seconds(watch_time) + "/" + format_seconds(duration) + " watched.")

            if watch_time < 1.6:
                time.sleep(watch_time)
            else:
                time.sleep(watch_time - 1.6)

            datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            data = [
                [username, session, account, alignment, followers, datetime]
            ]

            with open('data_output/lra_dataset.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csv.writer(csvfile).writerows(data)

            scroll()
            counter += 1
            print(str(counter) + " reels watched. Scrolling...")

        except Exception as e:
            print(f"An error occurred: {e}")
            break

    driver.quit()

# todo: fix click_like
# todo: fix click_save
# todo: fix click_follow
# todo: fix click_not_interested

# todo: fix leave_comment
# todo: fix visit_profile
# todo: fix share
