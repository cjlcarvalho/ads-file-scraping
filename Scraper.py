#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests 
from Crawler import Crawler

class Scraper(object):
    
    def __init__(self, page, folder):
        self.page = page
        self.folder = folder
        
    def getFiles(self):
        crawler = Crawler(self.page)
        
        try:
            while(True):
                files = crawler.getFileLinks()
                for name, link in files:
                    print("Downloading " + name + "...")
                    localFileName = self.folder + "/" + name
                    request = requests.get(link, stream=True)
                    with open(localFileName, 'wb') as f:
                        for chunk in request.iter_content(chunk_size=1024):
                            if chunk:
                                f.write(chunk)
                print("Downloaded.")
                crawler.nextPage()
        except Exception as e:
            print(e)
         

