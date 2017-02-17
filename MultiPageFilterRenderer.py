import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

from webscraping import xpath

class MultiPageFilterRenderer(QWebPage):  
    def __init__(self, urls, xpathFilter):
        self.xpathFilter = xpathFilter  
        self.app = QApplication(sys.argv)  
        QWebPage.__init__(self)  
        self.loadFinished.connect(self._loadFinished)  
        self.urls = urls  
        self.data = {} # store downloaded HTML in a dict  
        self.crawl()  
        self.app.exec_()  
          
    def crawl(self):  
        if len(self.urls)>0:  
          url = self.urls.pop(0) 
          #print 'Downloading', url  
          self.mainFrame().load(QUrl(url))  
        else:  
          self.app.quit()  
          
    def push(self, l):
        self.urls.append(l)
        
    def _loadFinished(self, result):  
        frame = self.mainFrame()  
        url = str(frame.url().toString())  
        html = frame.toHtml()
        html = unicode(html)  
        self.data[url] = xpath.search(html, self.xpathFilter)  
        self.crawl()  
        
# TEST STUB  
#urls = [u'http://www.vrapce.mk/ad/31515', u'http://www.vrapce.mk/ad/15389', u'http://www.vrapce.mk/ad/27998', u'http://www.vrapce.mk/ad/24257', u'http://www.vrapce.mk/ad/19107', u'http://www.vrapce.mk/ad/14938', u'http://www.vrapce.mk/ad/14093', u'http://www.vrapce.mk/ad/14287', u'http://www.vrapce.mk/ad/14285', u'http://www.vrapce.mk/ad/14095', u'http://www.vrapce.mk/ad/14283', u'http://www.vrapce.mk/ad/31674', u'http://www.vrapce.mk/ad/31501', u'http://www.vrapce.mk/ad/18958', u'http://www.vrapce.mk/ad/33154', u'http://www.vrapce.mk/ad/2306', u'http://www.vrapce.mk/ad/32088', u'http://www.vrapce.mk/ad/29153', u'http://www.vrapce.mk/ad/23524', u'http://www.vrapce.mk/ad/20304', u'http://www.vrapce.mk/ad/4108', u'http://www.vrapce.mk/ad/22328', u'http://www.vrapce.mk/ad/3279', u'http://www.vrapce.mk/ad/13233', u'http://www.vrapce.mk/ad/2827', u'http://www.vrapce.mk/ad/24813', u'http://www.vrapce.mk/ad/18957', u'http://www.vrapce.mk/ad/5466', u'http://www.vrapce.mk/ad/31556', u'http://www.vrapce.mk/ad/29668']  
# url = [u'http://www.vrapce.mk/']
# urls = []
# r = MultiPageFilterRenderer(url, '//a[@class="advertImage3Inner"]/@href')  
# urls = r.data['http://www.vrapce.mk/'] 
# print urls
# description = 
#     print description