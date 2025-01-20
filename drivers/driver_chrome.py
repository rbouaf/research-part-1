from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

from selenium import webdriver

# Set up Chrome options to use Mitmproxy
chrome_options = Options()
# chrome_options.add_argument('--proxy-server=http://127.0.0.1:8080')
# chrome_options.add_argument('--headless')  # Enable headless mode
# chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems

driver = webdriver.Chrome(options=chrome_options)

# wait variables
wait5 = WebDriverWait(driver, 5)
wait10 = WebDriverWait(driver, 10)
wait2 = WebDriverWait(driver, 2)
