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
def scrapeVipMarket5():
    # UTF-8 support
    reload(sys)
    sys.setdefaultencoding('utf-8')
    now = datetime.now()
    down = Downloader('http://www.vipmarket5.mk/search/')
    content = down.get_content()
    html = unicode(content)
    linkovi = xpath.search(html, '//tr[@class="frame_content"]')
    ads = []
    for l in linkovi:
        link = "http://www.vipmarket5.mk" + xpath.get(l, '//div[@style="width:365px; height:90%; margin-top:10px;"]/b/a/@href')
        title = xpath.get(l, '//div[@style="width:365px; height:90%; margin-top:10px;"]/b/a')
        imageUrl = xpath.get(l, '//div[@style="overflow:hidden; width:150px; height: 146px; margin: 5px;"]/a/img/@src')
        download = Downloader(link)
        cont = download.get_content()
        cont = unicode(cont)
        description = xpath.get(cont, '//div[@class="feature"]/p').strip()
        if description == "":
            description = "/"

        #VNIMANIE! NEMA KATEGORII
        category="/"
        subcategory="/"
        price = xpath.get(l, '//div[@style="margin-top:5px; margin-left:10px;height:155px; overflow:hidden;"]/h4/a')
        if price == u"Цена:По договор":
            value = "/"
            currency = "/"
        else:
            price = price.split(":")
            price = price[1]
            price = price.split(" ")
            value = price[0]
            if price[1]=="&euro;":
                currency = "EUR"
            elif price[1]=="ден.":
                currency = "MKD"
        date = xpath.get(l, '//b[@style="font-weight:bold;"]')
        date = date.split(": ")
        date = date[1]
        date = date.split(".")
        date = date[2]+"-"+date[1]+"-"+date[0]
        country = u"Македонија"

        region = xpath.get(cont, '//div[@style="float:left; width: 140px; overflow:hidden; font-family: Tahoma,Geneva,sans-serif; font-weight:bold"]')
        if region == "":
            region = "/"
        
        ad = Ad(link, title, imageUrl, description, category, subcategory, value, currency, region, date, country)    
        ads.append(ad)
    return adsToJson(ads)
#print scrapeVipMarket5()