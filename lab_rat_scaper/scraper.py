import textwrap

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv

import lab_rat_scaper.open_ig as open_reels
import lab_rat_scaper.driver_edge as ed
import lab_rat_scaper.conditions as conditions
driver = ed.driver

wait5 = ed.wait5
wait10 = ed.wait10
wait2 = ed.wait2


# bug fixed, when search by style, you have to use style*="value" instead of style="value" for contains() search


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


header = [
    "account", "session", "url", "reel_like_count", "reel_comment_count",
    "reel_duration", "watch_time_seconds", "watch_time_percentage", "liked",
    "positive_comment", "followed", "shared", "saved", "visited_profile",
    "negative_comment", "not_interested", "uploader", "caption", "datetime"
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

            # CONDITIONAL BEHAVIOR
            if (condition == 1) or (condition == 2 and conditions.if_in_user_db(reel_data[0])):
                if liked:
                    click_like(current_reel)
                    print("+ 1 ❤️", end=" ")
                if saved:
                    click_save(current_reel)
                    print("+ 1 💾", end=" ")
                if followed:
                    click_follow(current_reel)
                    print("+ 1 🤴", end=" ")
                if clicked_not_interested:
                    click_not_interested(driver)
                    print("Not interested", end=" ")
                if shared:
                    share(current_reel)
                    print("+ 1 👨‍👦", end=" ")
                if profile_visited:
                    visit_profile(current_reel)
                    print("Visited profile", end=" ")
                if len(pos_comment_left) > 1:
                    leave_comment(current_reel, pos_comment_left)
                    pcomlft = 1
                    print("+ 1 👍💬", end=" ")
                if len(neg_comment_left) > 1:
                    leave_comment(current_reel, neg_comment_left)
                    ncomlft = 1
                    print("+ 1 👎💬", end=" ")

            watch_time = duration * watch_time_percentage
            print(format_seconds(watch_time) + "/" + format_seconds(duration) + " watched.")

            if watch_time < 1.6:
                time.sleep(watch_time)
            else:
                time.sleep(watch_time - 1.6)

            datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            data = [
                [username, session, stripped_remove_instagram_com_url, reel_data[-2], reel_data[-1], duration,
                 watch_time, watch_time_percentage, liked, pcomlft, followed, shared,
                 saved, profile_visited, ncomlft,
                 clicked_not_interested, reel_data[0], reel_data[1], datetime]
            ]

            with open('data_output/data_output.csv', 'a', newline='', encoding='utf-8') as csvfile:
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
