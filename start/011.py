import requests
from bs4 import BeautifulSoup

class Content:
    """
    Classe base comum para todos os artigos/páginas
    """
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """
        Uma função flexível de exibição controla a saída
        """
        print("URL: {}".format(self.url))
        print("TITLE: {}".format(self.title))
        print("BODY: {}".format(self.body))
        print("=" * 50)

class Website:
    """
    Contém informações sobre a estrutura do site
    """
    def __init__(self, name, url, title_tag, body_tag) -> None:
        self.name = name
        self.url = url
        self.title_tag = title_tag
        self.body_tag = body_tag

class Crawler:

    def get_page(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')
    
    def safe_get(self, page_obj, selector):
        selected_elements = page_obj.select(selector)
        if selected_elements is not None and len(selected_elements) > 0:
            return '\n'.join(
                [elem.get_text() for elem in selected_elements]
            )
        return ''
    
    def parse(self, site, url):
        bs = self.get_page(url)
        if bs is not None:
            title = self.safe_get(bs, site.title_tag)
            body = self.safe_get(bs, site.body_tag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()

crawler = Crawler()

site_data = [
    ['O\'Reilly Media', 'http://oreilly.com',
     'h1', 'div#titlePromo'],
    ['Reuters', 'httlp://www.reuters.com', 'h1',
     'div.article-body__content__17Yit']
]

websites = []
for row in site_data:
    websites.append(Website(row[0], row[1], row[2], row[3]))

crawler.parse(websites[0], 'http://shop.oreilly.com/product/'\
              '0636920028154.do')
crawler.parse(websites[1], 'http://www.reuters.com/article/'\
              'us-usa-epa-pruitt-idUSKBN19W2D0')
