from lxml import html
import requests

class Crawler(object):
    
    adsSite = 'https://ads.ifba.edu.br/'
    tree = None
    
    def __init__(self, page):
        self.page = self.adsSite + page
    
    def getFileLinks(self):
        p = requests.get(self.page)
        self.tree = html.fromstring(p.content)
        
        links = [ 'https://ads.ifba.edu.br/' + i for i in self.tree.xpath("//div[@class='table-responsive']//" + \
                                                          "table//td//a[@class='fgalname fileLink']/@href") ]
        
        names = self.tree.xpath("//div[@class='table-responsive']//table//td//a[@class='fgalname fileLink']/text()")
        
        result = []
        for i in range(len(names)):
            result += [[ names[i], links[i] ]]
        
        return result
        
    def nextPage(self):
        nextPage = self.tree.xpath("//div[@class='clearboth']//ul[@class='pagination']//li[not(@class='disabled')]//a[@class='prevnext next']/@href")
        
        if(nextPage):
            self.page = self.adsSite + nextPage
        else:
            raise Exception("All your pages have been crawled.")
        
        
     

