import requests
from bs4 import BeautifulSoup

class Content:
    """
    Classe base comum para todos os artigos/páginas
    """
    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """
        Uma função flexível de exibição controla a saída
        """
        print("Novo artigo encontrado no topico: {}".format(self.topic))
        print("URL: {}".format(self.url))
        print("TITLE: {}".format(self.title))
        print("BODY: {}".format(self.body))
        print("=" * 50)

class Website:
    """
    Contém informações sobre a estrutura do site
    """
    def __init__(self, name, url, search_url, result_listing,
                 result_url, absolute_url, title_tag, body_tag):
        self.name = name
        self.url = url
        self.search_url = search_url
        self.result_listing = result_listing
        self.result_url = result_url
        self.absolute_url = absolute_url
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
        child_obj = page_obj.select(selector)        
        if child_obj is not None and len(child_obj) > 0:
            return child_obj[0].text.strip()
        return ''
    
    def search(self, topic, site):
        bs = self.get_page(site.search_url + topic)
        search_results = bs.select(site.result_listing)
        for result in search_results:
            url = result.select(site.result_url)[0].attrs["href"]
            if(site.absolute_url):
                bs = self.get_page(url)
            else:
                bs = self.get_page(site.url + url)
            
            if bs is None:
                print("Algo deu errado na pagina ou url")
                return
            
            title = self.safe_get(bs, site.title_tag)
            body = self.safe_get(bs, site.body_tag)
            if title != '' and body != '':
                content = Content(topic, url, title, body)
                content.print()

    
crawler = Crawler()

site_data = [
    ['BRPOX', 'https://brpox.portalonline.org/',
     'https://brpox.portalonline.org/?s=', 'div.posts-wrapper article',
     'h2.blog-entry-title a', True, 'h1', 'div.nv-content-wrap.entry-content']
]

websites = []
for row in site_data:
    websites.append(Website(row[0], row[1], row[2], row[3],
                            row[4], row[5], row[6], row[7]))

topics = ['whatsapp']
for topic in topics:
    print("INFORMAÇÃO SOBRE: " + topic) 
    for target_site in websites:
        crawler.search(topic, target_site)