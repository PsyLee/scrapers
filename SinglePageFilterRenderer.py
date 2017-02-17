#!/usr/bin/env python
# coding: utf-8

import sys
from webscraping import xpath
from SinglePageRenderer import SinglePageRenderer
import re

reload(sys)
sys.setdefaultencoding('utf-8')
  
def filterContent(url, filterXpath):
    renderedWebPage = SinglePageRenderer(url)  
    html = renderedWebPage.frame.toHtml()
    html = unicode(html)
#     print html
    return re.sub( '\s+', ' ', xpath.get(html, filterXpath) ).strip()

#TEST STUB    
# url = 'http://www.vrapce.mk/ad/33645' 
# filterXpath = '//div[@class="detailsDescription"]'
# print filterContent(url, filterXpath)

