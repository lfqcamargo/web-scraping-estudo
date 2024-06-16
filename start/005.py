from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')

for child in bs.find('table', {'id': 'giftList'}).children:
    print(child)

for siblings in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(siblings)

print(bs.find('img',
              {'src': '../img/gifts/img1.jpg'})
              .parent.previous_sibling.get_text())