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
# Set up Chrome options to use Mitmproxy
edge_options = Options()
# edge_options.add_argument('--proxy-server=http://127.0.0.1:8080')
# edge_options.add_argument('--headless')  # Enable headless mode
# edge_options.add_argument('--disable-gpu')  # Disable GPU acceleration
edge_options.add_argument('--no-sandbox')  # Bypass OS security model
edge_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
# edge_options.add_extension('C:\\Users\\Admin\\Programs\\PycharmProjects\\comp396\\drivers\\xy_extension.crx')
driver = webdriver.Edge(options=edge_options)


# wait variables
wait5 = WebDriverWait(driver, 5)
wait10 = WebDriverWait(driver, 10)
wait2 = WebDriverWait(driver, 2)
