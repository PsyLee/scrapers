#!/usr/bin/env python
# coding: utf-8

import sys
from Downloader import Downloader
from webscraping import xpath
from Utilities import getDescription
from Utilities import adsToJson
from Ad import Ad
from datetime import datetime
from datetime import date, timedelta
from locale import currency

def scrapeKupujemProdajem():
    # UTF-8 support
    reload(sys)
    sys.setdefaultencoding('utf-8')
    now = datetime.now()
    ads = []
    try:
        down = Downloader('http://www.kupujemprodajem.com/search.php?action=list&data[category_id]=&data[group_id]=&data[location_id]=&data[keywords]=&submit[search]=Tra%C5%BEi')
        content = down.get_content()
        html = unicode(content)
        link=""
        title=""
        imageUrl=""
        description="/"
        category="/"
        subcategory="/"
        value="/"
        currency="/"
        region="/"
        date=str(now.year)+"-"+str(now.month)+"-"+str(now.day)
        linkovi = xpath.search(html, '//div[@class="item clearfix"]')
        highlighted = xpath.search(html, '//div[@class="item clearfix adHighlighted"]')
        for h in highlighted:
            linkovi.append(h)
        for l in linkovi:
            try:
                link = "http://www.kupujemprodajem.com/" + xpath.get(l, '//a[@class="adName"]/@href')
                title = xpath.get(l, '//a[@class="adName"]')
                region = xpath.get(l, '//section[@class="locationSec"]').strip()
                region = region.split(" | ")
                region = region[0]
                price = xpath.get(l, '//span[@class="adPrice"]')
                price = price.split("&nbsp;")
                if len(price)==2:
                    value = price[0]
                    value = value.replace(".", "")
                    value = value.split(",")
                    value = value[0]
                    currency = price[1]
                else:
                    value = "/"
                    currency = "/"
        
                if currency=="&euro;":
                    currency = "EUR"
                elif currency == "din":
                    currency = "DIN"
                    
                down = Downloader(link)
                content = down.get_content()
        
                category = xpath.get(content, '//a[@class="crumbs"]')
                description = xpath.get(l, '//section[@class="nameSec"]/p[@class="adDescription"]')
                category = category.split("|")
                category = category[0]
                category = category.strip()
                imageUrl = xpath.get(content, '//div[@class="adThumbnailHolder"]/a/img/@src')
                imageUrl = imageUrl.replace("//", "/")
                imageUrl = imageUrl[1::]
                if imageUrl =="":
                    imageUrl="/"
                description = description.replace("...<p>", "")
                description = description.strip()
                country = u"Србија"
                ad = Ad(link, title, imageUrl, description, category, subcategory, value, currency, region, date, country)    
                ads.append(ad)
            except:
                pass 
    except:
        pass 
     
    return adsToJson(ads)
#print scrapeKupujemProdajem()