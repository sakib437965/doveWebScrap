from configparser import LegacyInterpolation
from itertools import count
from traceback import print_tb
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from datetime import datetime
import time
import getpass
import datetime

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

import pandas as pd

#setting chrome driver path
path = "C:/Users/HP/Desktop/Study/chromedriver"
ser = Service(path)
driver = webdriver.Chrome(service=ser)

url = 'https://www.dove.org/'


# calculating start time of algorithm
start_time = time.time()

#calling the website url
driver.get(url)

#maximizing the browser window
driver.maximize_window()

# setting boolean parameter for page limit
page_limit = True

if page_limit == True:
    max_pages = 100
else: max_pages = 0



# declaring lists to store scraped data
documentaryName_list = []
approvedFor_list = []
category_list = []

## Navigating through menu link to reach to documentary page

driver.find_element(By.CLASS_NAME, value="clicker-hamburger").click()
driver.find_element(By.XPATH, value='//ul//li//a[contains(text(),"Documentary")]').click()


# iterating over first 100 pages to scrap required data
for i in range(max_pages):

    doc_name = driver.find_elements(by=By.XPATH, value='//div[@class="content-info"]//h4[@class="info-title"]')
    for name in range(len(doc_name)):
        documentaryName_list.append(doc_name[name].text)

    approved_for = driver.find_elements(by=By.XPATH, value='//div[@class="content-approved"]//strong')
    for items in range(len(approved_for)):
        approvedFor_list.append(approved_for[items].text)

    categories = driver.find_elements(by=By.XPATH, value='//div[@class="content-info"]//span[@class="info-category"]')
    for category in range(len(categories)):
     category_list.append(categories[category].text)

# using time.sleep for a slight delay in code to interact and find all the elements
    time.sleep(1)
    #driver.implicitly_wait(1)



# creating a dictionary to store the scraped data in previous step
    data_dictionary = {'name': documentaryName_list, 'approved_for': approvedFor_list, 'category': category_list}

# storing the scraped data in csv file
    dataframe = pd.DataFrame(data_dictionary)
    #dataframe.to_csv('data.csv', mode='a', index=False, header=False, encoding="cp1252")
    dataframe.to_csv('data.csv' , index=False)

# pagination xpath to go from first page till 100th page
    driver.find_element(By.XPATH, value="//span//a//span[@class='fas fa-caret-right item-icon']").click()


# calculating end time of algorithm to check the performance in terms of time (seconds)
print("--- %s seconds ---" % (time.time() - start_time))

# closing the driver instance and browser window
driver.quit()
