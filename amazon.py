from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib




URL = "https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1"

# headers= {
#     'User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
#     }
# # 


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
page=requests.get(URL, headers=headers)

soup1=BeautifulSoup(page.content,"html.parser")

soup2=BeautifulSoup(soup1.prettify(),"html.parser")

title = soup2.find(id="productTitle").get_text()
price = soup2.find(id="acrCustomerReviewText").get_text()
#print(price)
print(title)



 

 