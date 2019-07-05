from bs4 import BeautifulSoup

import requests

req= requests.get('https://www.brainyquote.com/quote_of_the_day')

soup = BeautifulSoup(req.text,'lxml')

qs = soup.find('div',{'class': 'clearfix'})


quotation = qs.find_all('a')

for line in quotation:
    print(line.text)
