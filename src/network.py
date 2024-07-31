from seleniumwire import webdriver
from seleniumwire.utils import decode as decodesw
import json

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
import time

import edge_driver as ed

def show_request_urls(driver, target_url):
    driver.get(target_url)
    urls=[]
    for request in driver.requests:
        if request.response:
            urls.append({"url": request.url})
    return urls

def show_response(driver, target_url):
    driver.get(target_url)
    resps = []
    for request in driver.requests:
        try:
            data = decodesw(
                request.response.body,
                request.response.headers.get("Content-Encoding", "identity")
            )
            resp = json.loads(data.decode("utf-8"))
            resps.append(resp)
        except:
            pass

        return resps

def main():
    keywords= ["api","graphql","edge","instagram","cdn","instagram.com",".jpg",".png",".mp4",".webp",".jpeg",".gif",".svg",".js",".css",".ico",".json",".xml",".php",".asp",".aspx",".jsp",".svg",".woff",".ttf",".eot",".otf",".woff2",".webm",".mp3",".wav",".ogg",".flac",".aac",".m4a",".opus",".flv",".avi",".mov",".wmv",".mpg",".mpeg",".mkv",".webm",".mp4",".m4v",".3gp",".3g2",".pdf",".doc",".docx",".xls",".xlsx",".ppt",".pptx",".txt",".rtf",".csv",".tsv",".zip",".rar",".7z",".tar",".gz",".bz2",".xz",".pdf",".epub",".mobi",".azw",".azw3",".djvu",".fb2",".ibooks",".cbz",".cbr",".cb7",".cbt",".cba",".chm",".lit",".prc",".pdb",".pml",".rb",".tr2",".tr3",".oxps",".xps",".ps",".eps",".ai",".indd",".pct",".pict",".pnt",".bmp",".dib",".gif",".jpeg",".jpg",".jpe",".jp2",".j2k",".jpf",".jpx",".jpm",".mj2",".svg",".svgz",".ai",".eps",".psd",".psb",".tiff",".tif",".tga",".tpic",".xcf",".fig",".webp",".pdf",".eps",".ps",".ai",".indd",".pct",".pict",".pnt",".bmp",".dib",".gif",".jpeg",".jpg",".jpe",".jp2",".j2k",".jpf",".jpx",".jpm",".mj2"]
    driver = webdriver.Edge(seleniumwire_options={"disable_encoding":True})

    target_url = "https://www.instagram.com/"

    urls = show_request_urls(driver,target_url)
    resps= show_response(driver,target_url)

    for url in urls:
        # for kw in keywords:
        #     if kw in url["url"]:
        #         print(url)
        print(url)

    with open("../data/requests/data.json", "w") as file:
        json.dump(resps, file)

    driver.close()

if __name__ == "__main__":
    main()