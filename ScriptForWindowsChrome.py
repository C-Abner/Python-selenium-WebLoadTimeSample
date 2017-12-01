# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import datetime

chrome_path = "C:\selenium_driver_chrome\chromedriver.exe"
web = webdriver.Chrome(chrome_path)

input('Press Any Key to continue')
time1 = time.time()

web.get('http://www.cwb.gov.tw/V7/')
delay = 30 # seconds

try:
    web.implicitly_wait(30)
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

time2 = time.time()
interval = time2 - time1
print ("final_name:\t", interval)
input('Press Any Key to continue')

web.close()
