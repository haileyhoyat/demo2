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

# get the .csv file from the most previous scrape
# os.dir returns documents in random order
# get document that has the most recent date
dirlistint = []
dirlist = os.listdir('documents/')
for file in dirlist:
  dirlistint.append(int(file.split(".")[0]))
most_recent = str(max(dirlistint)) + '.csv'
print(dirlistint)
print("Most recent : " + str(max(dirlistint)))

#for each file on the webpage
for file in attachment_table:

  #get the file name
  file_name = file.find_element(By.CSS_SELECTOR, "span").text
  
  #get the .csv file from the most previous scrape
  arr = most_recent
  
  #assume that the file on the webpage is a new file that was not on the webpage from the most previous scrape
  is_new_file = True

  #check if the file on the webpage is listed from the most previous scrape
  with open('documents/'+arr, newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
      #if the file on the webpage is listed from the most previous scrape, 
      #the file is not a newly added file therefore is_new_file is false
      #break, and continue onto the next file on the webpage
      if file_name == row[0]:
        is_new_file = False
        break
      
  #if file on the webpage is not listed from the most previous scrape, the file is a newly added file
  if is_new_file:
    print(file_name)

  #list out all documents on webpage on the date of the scrape.
  #get the file name, file id, and today's date
  # file_name = file.find_element(By.CSS_SELECTOR, "span").text
  file_id = file.get_attribute("id")
  time_stamp = date.today().strftime("%Y%m%d")

  #create a new .csv (titled as today's date) to note down the files that are on the webpage today
  with open("documents/" + time_stamp+".csv", "a", newline="") as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow([file_name, file_id, time_stamp])
  
browser.quit
  
#with open('./GitHub_Action_Results.txt', 'w') as f:
   #f.write(f"This was written with a GitHub action")

