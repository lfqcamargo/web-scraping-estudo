from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTittle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        print(e)
        return None
    
    return title

title = getTittle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Ttitle could not be found')
else:
    print(title)