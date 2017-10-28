#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests, configs, os
from Crawler import Crawler

class Scraper(object):

    bar = "\\" if os.name == "nt" else "/"
    
    def __init__(self, page, folder):
        self.page = page
        self.folder = folder
        
    def getFiles(self):
        crawler = Crawler(self.page)
        
        try:
            while True:
                files = crawler.getFileLinks()
                for name, link in files:
                    if "file" in link:
                        print("Entering subfolder " + name + "...")
                        subfolder = self.folder + self.bar + name
                        if not os.path.exists(subfolder):
                            os.makedirs(subfolder)
                        scraper = Scraper(link, subfolder)
                        scraper.getFiles()
                    else:
                        print("Downloading " + name + "...")
                        localFileName = self.folder + self.bar + name
                        request = requests.get(configs.ADS_SITE + "/" + link, stream=True)
                        with open(localFileName, 'wb') as f:
                            for chunk in request.iter_content(chunk_size=1024):
                                if chunk:
                                    f.write(chunk)
                crawler.nextPage()
        except Exception as e:
            print(e)
         

