# Import dependencies
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.proxy import Proxy, ProxyType

# Set up the proxy to use Mitmproxy
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = '127.0.0.1:8080'
proxy.ssl_proxy = '127.0.0.1:8080'

# Set up Chrome options to use Mitmproxy
chrome_options = Options()
chrome_options.add_argument('--proxy-server=http://127.0.0.1:8080')

# Initialize the WebDriver with options
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

# this method works too
driver.get('https://www.instagram.com/reels/')
print("Opened Reels")

time.sleep(5)


reels = driver.find_element(By.CSS_SELECTOR, 'div[tabindex="0"]')
counter = 0
while True:
    try:
        
        # Move to the next reel by simulating a right arrow key press
        counter+=1
        print("Scrolling down "+str(counter))
        reels.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)

        # get thumnail and store as current_thumbnail
        current_thumbnail = driver.find_element(By.CSS_SELECTOR, 'img[class="xz74otr x1bs05mj x5yr21d x10l6tqk x1d8287x x19991ni xwzpupj xuzhngd"]')
        link = current_thumbnail.get_attribute('src')
        print(link)

        # get second screenshot

        # Optionally, add a break condition to stop scrolling after a certain number of reels
    except Exception as e:
        print(f"An error occurred: {e}")
        break

    # current video (the active one)
    # xz74otr x1bs05mj x5yr21d x10l6tqk x1d8287x x19991ni xwzpupj // xuzhngd // 
    # this is the id of our active video
    
    # next video
    # xz74otr x1bs05mj x5yr21d // x1ptxcow // x10l6tqk x1d8287x x19991ni xwzpupj
    # this is the id of all other videos (ids don't change, they have as a serverside var)
    
    