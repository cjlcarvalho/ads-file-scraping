from lxml import html
import requests
import configs

class Crawler(object):

    tree = None
    
    def __init__(self, page):
        self.page = configs.ADS_SITE + "/" + page
    
    def getFileLinks(self):
        p = requests.get(self.page)
        self.tree = html.fromstring(p.content)
        
        links = self.tree.xpath("//div[@class='table-responsive']//" + \
                                "table//td//a[@class='fgalname fileLink']/@href")
        
        names = self.tree.xpath("//div[@class='table-responsive']//table//td//a[@class='fgalname fileLink']/text()")
        
        result = []
        for i in range(len(names)):
            result.append([names[i], links[i]])
        
        return result
        
    def nextPage(self):
        nextPage = self.tree.xpath("//div[@class='clearboth']//ul[@class='pagination']" + \
                                   "//li[not(@class='disabled')]//a[@class='prevnext next']/@href")
        
        if(nextPage):
            self.page = configs.ADS_SITE + nextPage[0]
        else:
            raise Exception("Page " + self.page + " is crawled.")
        
        
     

