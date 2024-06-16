from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

#name_list = bs.find_all('span', {'class': 'green'})
name_list = bs.find_all(text='the prince')
for name in name_list:
    print(name.get_text())

print((name_list))    