import scrapy
import pandas as pd
import time
from datetime import datetime
from scrapy import Request

#setting the limit for number of pages to be scrapped
page_limit = True
pages = 0
if page_limit == True:
    pages = 100
else:
    pages = 0

#Creating excel file by specifying the column names
with open('data.csv', 'w') as f:
    f.write("Name, Approved For,Documentary Category\n")

# calculating start time of algorithm
start_time = datetime.now()
class DoveSpider(scrapy.Spider):
    name = 'dove'
    allowed_domains = ['dove.org']
    start_urls = ["https://dove.org/reviews/genre/documentary/"]
    for i in range(2 , pages+1):
        start_urls.append('https://dove.org/reviews/genre/documentary/page/' + str(i))


    def parse(self, response):
        #creating xpaths for Web elements

        docName_xpath = '//div[@class="content-info"]//h4[@class="info-title"]/text()'
        approvedFor_xpath = '//div[@class="content-approved"]//strong/text()'
        documentaryCategory_xpath = '//div[@class="content-info"]//span[@class="info-category"]/text()'


        #getting the values of web elements from xpaths

        getDocName = response.xpath(docName_xpath).getall()
        getApprovedfor = response.xpath(approvedFor_xpath).getall()
        getDocumentaryCategory = response.xpath(documentaryCategory_xpath).getall()


        #putting all the data in dictionary that we retrived in above steps

        dictionary = {'value1': getDocName, 'value2': getApprovedfor, 'value3' :getDocumentaryCategory }
        dataframe = pd.DataFrame(dictionary)

        #writing the data in excel file
        dataframe.to_csv('data.csv', mode='a', index=False, header=False)


        #calculating end time of algorithm to check the performance in terms of time (seconds)
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))