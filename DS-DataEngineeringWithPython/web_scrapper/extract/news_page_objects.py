from common import config
import requests
import codecs
import bs4
import re

class NewsPage:
    def __init__(self, news_site_uid, url):
        self._config = config()['news_sites'][news_site_uid]
        self._queries = self._config['queries']
        self._url = url
        self._html = None
        self._visit(url)

    def _select(self, query_string):
        return self._html.select(query_string)

    def _visit(self, url):
        response = requests.get(url)
        response.raise_for_status()
        html = response.content
        unicode_str = html.decode('utf8')
        encoded_str = unicode_str.encode("ascii",'ignore')
        self._html = bs4.BeautifulSoup(encoded_str, "html.parser")
        #self._html = bs4.BeautifulSoup(response.text,'html.parser')


class HomePage(NewsPage):
    
    def __init__(self, news_site_uid, url):
        super().__init__(news_site_uid,url)

    @property
    def article_links(self):
        query_val = self._queries['homepage_article_links']
        link_list  = [link.a['href'] for link in  self._select(query_val ) if link and link.a and link.a.has_attr('href')]
        return set(link_list)

class ArticlePage(NewsPage):
    def __init__(self, news_site_uid,url):
        super().__init__(news_site_uid,url)

    @property
    def title(self):
        result = self._select(self._queries['article_title'])
        return result[0].text if len(result) else ''

    @property
    def body(self):
        result = self._select(self._queries['article_body'])
        return result[0].text if len(result) else ''
    
    @property
    def url(self):
        return  self._url
        
    
    

