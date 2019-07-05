from bs4 import  BeautifulSoup
from  termcolor  import colored
import requests

req= requests.get("https://www.indiatoday.in/top-stories")

soup= BeautifulSoup(req.text,'html.parser')

news_box = soup.find('div', {'class': 'view view-category-wise-content-list view-id-category_wise_'
                                      'content_list view-display-id-section_wise_content_listing view-dom-id- custom'})

last_links=soup.find(class_='item-list')
last_links.decompose()
pages_links=soup.find('h2',class_='element-invisible')
pages_links.decompose()
all_news = news_box.find_all('p')
headlines= news_box.find_all('h2')

count=1
number=1
for news in all_news:
    print(count,")",news.text)
    count+=1
for heading in headlines:
    print(colored(number,'green'),colored(heading.text, 'blue'))
    number += 1
