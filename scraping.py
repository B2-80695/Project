from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from urllib.parse import urlparse

browser=webdriver.Chrome()
browser.get("https://www.moneycontrol.com/stocks/marketstats/nsegainer/index.php")
section = browser.find_element(By.ID,"mc_content")
rows= section.find_elements(By.TAG_NAME,"tr")
count = 1
for row in rows:
    print(row)
    count+=1
    if count==5:
        break

browser.quit()