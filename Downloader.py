#!/usr/bin/env python
# coding: utf-8

from webscraping import xpath
import urllib2
import sys

# UTF-8 support
reload(sys)
sys.setdefaultencoding('utf-8')

class Downloader(object):
    def __init__(self, url):
        self.url = url
    #'http://www.pazar3.mk/mk/Listing/Home/Search?CookieLocationId=0&Location=0-%D0%A6%D0%B5%D0%BB%D0%B0-%D0%9C%D0%B0%D0%BA%D0%B5%D0%B4%D0%BE%D0%BD%D0%B8%D1%98%D0%B0&_=1404733181509'
    def get_content(self):
        response = urllib2.urlopen(self.url)
        html = response.read()
        
        #html = unicode(html)
        
        return html