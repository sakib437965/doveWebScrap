
#importing necessary libraries
from urllib import request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np
import re
import ssl
import time

# variable to calculate the time it takes soupd to scrape data
start_time=time.time()

ssl._create_default_https_context = ssl._create_unverified_context


# setting boolean parameter for page limit
page_limit= True
if page_limit == True:
    max_pages=100
else: max_pages=200

# declaring lists to store scraped data
category_list=[]
documentaryName_list=[]
approvedFor_list=[]

# iterating over max_pages number of pages to scrap required data
for page in range(max_pages):
    req=requests.get(f"http://dove.org/reviews/genre/documentary/page/{page}/", headers={"User-Agent":"Mozilla/5.0"})
    soup=BeautifulSoup(req.content, "html.parser")

    cat=soup.select('div.content-info span:nth-child(1)')
    for i in range(len(cat)):
        category_list.append(cat[i].text)

    tit = soup.select('div.content-info h4:nth-child(2)')
    for i in range(len(tit)):
        documentaryName_list.append(tit[i].text)

    con = soup.select('div.content-approved strong:nth-child(1)')
    for i in range(len(con)):
        approvedFor_list.append(con[i].text)

# creating a dictionary to store the scraped data in previous step
dict={'category':category_list, 'title':documentaryName_list,'content':approvedFor_list}
df=pd.DataFrame(dict)
print(df)
# storing the scraped data in csv file
df.to_csv('bs4.csv')

# printing the time
print("--- %s seconds ---" % (time.time() - start_time))
