from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.edge.options import Options
from seleniumwire import webdriver
from selenium import webdriver

# Set up Chrome options to use Mitmproxy
c_options = Options()
# edge_options.add_argument('--proxy-server=http://127.0.0.1:8080')
# edge_options.add_argument('--headless')  # Enable headless mode
# edge_options.add_argument('--disable-gpu')  # Disable GPU acceleration
c_options.add_argument('--no-sandbox')  # Bypass OS security model
c_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems

driver = webdriver.Chrome(options=c_options)

def custom_driver(custom_options):
    return webdriver.Edge(options=custom_options)

# wait variables
wait5 = WebDriverWait(driver, 5)
wait10 = WebDriverWait(driver, 10)
wait2 = WebDriverWait(driver, 2)
