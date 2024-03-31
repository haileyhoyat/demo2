from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import date
import csv
import os
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
browser = webdriver.Chrome(options = chrome_options)

browser.get('https://clevelandoh.govqa.us/WEBAPP/_rs/(S(byev33xlbgyh0u2fgikb2om0))/AnswerDetail.aspx?sSessionID=&aid=74904')
print(browser.title)

html_source = browser.page_source

#get files from the webpage
attachment_table = browser.find_elements(By.CSS_SELECTOR, "a.dxbButton_Moderno")

#get the .csv file from the most previous scrape
lst = os.listdir('documents/').sort()
print(lst)
  
browser.quit
  
with open('./GitHub_Action_Results.txt', 'w') as f:
   f.write(f"This was written with a GitHub action {browser.title}")

