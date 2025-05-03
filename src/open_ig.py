from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

import drivers.driver_chrome as driver_chrome

driver = driver_chrome.driver
wait5 = driver_chrome.wait5
wait10 = driver_chrome.wait10
wait2 = driver_chrome.wait2


def open_reels(username, password):
    driver.get("https://www.instagram.com/")
    print("⎣ instagram.com ⎦")
    # logging in
    username_field = wait10.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password_field = wait10.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    # enter username
    username_field.clear()
    username_field.send_keys(username)
    # enter password
    password_field.clear()
    password_field.send_keys(password)
    print("⎡" + username + "⎤")
    print("⎣", end="")
    for p in range(0, len(username)):
        print("*", end="")
    print("⎦")
    # submit
    wait2.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    print("╭──────╮")
    print("│SUBMIT│")
    print("╰──────╯")
    time.sleep(9)

    # click on not now button 1
    # wrap in ty except
    try:
        for i in range(5):
            try:
                element_text = "Not now"
                not_now_button = wait10.until(EC.element_to_be_clickable((By.XPATH, f"//*[text()='{element_text}']")))

                not_now_button.click()
                print("[Not now]")
                break
            except Exception as e:
                print(f"Attempt {i + 1} failed: {e}")
                time.sleep(2)
    except Exception as e:
        print(f"Failed to click Not now button: {e}")

    # click on not now button 2
    # Not_Now_button = wait10.until(EC.element_to_be_clickable((By.XPATH,
    #                                                           '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
    time.sleep(1)
    try:
        Not_Now_button = wait10.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
        Not_Now_button.click()
        print("[Not Now]")
    except Exception as e:
        print(f"Failed to click Not Now button: {e}")

    driver.get('https://www.instagram.com/reels/')
    print('⎣ www.instagram.com/reels/ ⎦')
