import requests
#import bs4
import parser

res = requests.get('http://www.prabhukalyansamal.esy.es')
print(type(res))
print(res.text)
pr = parser(res.text,'html')
#pr = bs4.BeautifulSoup(res.text,'html')
print(type(soup))
print(pr.select('title'))
print(pr.select('.body'))
for i in soup.select('.p'):
    print(i.text)
