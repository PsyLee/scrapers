#!/usr/bin/env python
# coding: utf-8

from webscraping import xpath
import urllib2
import sys
import re
from datetime import datetime
from Ad import Ad
from Downloader import Downloader
from Utilities import getDescription
from Utilities import adsToJson

def scrapeReklama5():
    # UTF-8 support
    reload(sys)
    sys.setdefaultencoding('utf-8')
    down = Downloader('https://www.reklama5.mk/Search')
    html = down.get_content()
    
    html = unicode(html)
    
    requestedWebPageUrl = 'https://www.reklama5.mk'
    
    adverts = xpath.search(html, '//div[@class="OglasResults"]')
    ads = []
    for advert in adverts:
        link = requestedWebPageUrl + xpath.get(advert, '//a[@class="SearchAdTitle"]/@href')
            
        title = xpath.get(advert, '//a[@class="SearchAdTitle"].text()').strip().replace("\"", "")
        
        description= getDescription(link, '//div[@class="oglasTitle"]/p[@class="oglasTitle"]').strip().replace("\"", "")
        
        subcategory="/"    
        imageUrl = xpath.get(advert, '//img[@class="thumbnail thumbs"]/@src')
        if imageUrl == "/Content/images/noImage2.jpg":
            imageUrl = requestedWebPageUrl + imageUrl
        
        price=xpath.get(advert,'//div[@class="text-left text-success"]')
        price=re.sub( '\s+', ' ', price ).strip()
        price=price.split(" ")
        
        if price[0]=="По":
            price[0]="/"
        if price[1]=="Договор":
            price[1]="/"
      
        value=price[0]
        currency=price[1]
        if currency=="€":
            currency="EUR"
        if currency == u"МКД":
            currency = "MKD"
        region=xpath.get(advert,'//p[@class="clear-margin"]')
        region = region.split("&gt;")
        region = region[0].strip()
        country = u"Македонија"
        date=xpath.get(advert,'//div[@class="text-center clear-padding adDate"]')
        date=re.sub( '\s+', ' ', date ).strip()
        time=xpath.get(advert,'//div[@class="text-center clear-padding adDate"]')
        time=re.sub( '\s+', ' ', time ).strip()
        if date.split()[0] == u"Денес" and time.split()[0]:
                date = datetime.now()
                datum = str(date.year)+"-"+str(date.month)+"-"+str(date.day)
                vreme = time.split(" ")[1]               
                p=datum +" "+ vreme
                date = p
        category=xpath.get(advert,'//p[@class="adCategoryName"]/a')
        
        ad = Ad(link, title, imageUrl, description, category, subcategory, value, currency, region, date, country)    
        #print link, title, imageUrl, description, category, subcategory, value, currency, region, date
        ads.append(ad)
        
    return adsToJson(ads) 

# print scrapeReklama5()