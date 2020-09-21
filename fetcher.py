import requests
from bs4 import BeautifulSoup
import json
from rename import rename


class HTMLFetcher(object):
    def __init__(self, baseURL: str = ''):
        super().__init__()
        self.base = baseURL
        if not baseURL.endswith('/') and baseURL != '':
            self.base += '/'
        
        self.prefixList = ['/', './']

    def fetch(self, url: str,
              params: dict = None,
              selector: str = None):
        for item in self.prefixList:
            if url.startswith(item):
                url.replace(item, '', 1)

        res = requests.get(self.base + url, params=params, headers={"user-agent": "Chrome/81"})
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        
        soup = BeautifulSoup(res.text, features='html.parser')

        if selector is None:
            return soup
        
        return soup.select_one(selector)
        

class WallpaperFetcher(object):
    def __init__(self):
        super().__init__()
        config_obj = json.load(open('./config.json'))
        self.url = config_obj['url']
        self.params = config_obj['params']
        self.selector = config_obj['selector']
        self.filename = config_obj['filebase'] + '.jpg'

    def fetch(self, destination: str):
        delimiter = '/'
        if destination.count('\\') >= 1:
            delimiter = '\\'

        file_name = rename(self.filename)
        img_url = HTMLFetcher().fetch(self.url, self.params, self.selector)['src']
        
        img_res = requests.get(f"{img_url}")
        img_res.raise_for_status()

        with open(f"{destination}{delimiter}{file_name}", 'wb+') as file:
            file.write(img_res.content)
