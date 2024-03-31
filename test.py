from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://clevelandoh.govqa.us/WEBAPP/_rs/(S(ldxq0tdwkmepsdytv2cfxdsw))/AnswerDetail.aspx?sSessionID=&aid=74904'

#set up Selenium driver to manipulate Chrome browser
options=webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r".\files"
  })
browser = webdriver.Chrome(options=options)
browser.get(url)
html_source = browser.page_source

print('hello')
