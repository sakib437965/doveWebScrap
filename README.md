# doveWebScrap


#How to run scrapy code 
clone the project to your local repository(directory)
open the project in IDE (pyCharm)
Open terminal in IDE and change the directory where spider folder is located in local system using 'cd' command. For example 'cd "path of spider folder"
run sipder with command " scrapy crawl dove" 


#How to run Selenium code
clone the selenium project to your local directory
open the project in IDE (pyCharm)
download chrome web driver from the link " https://chromedriver.storage.googleapis.com/index.html?path=100.0.4896.60/" . you can change the chrome web driver version according to your Chrome browser version.
In doveSelenium.py file change the "path" variable with the path of chorme webdriver where it is located in your system for example in the code change the below line with the path of chromedriver.exe file
path = "C:/Users/HP/Desktop/Study/chromedriver" 
execute the code and it will open chrome browser window and maximize it and start scrapping data
