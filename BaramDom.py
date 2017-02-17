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
def scrapeBaramDom():
    # UTF-8 support
    reload(sys)
    sys.setdefaultencoding('utf-8')
    now = datetime.now()
    down = Downloader('http://www.baramdom.com/')
    content = down.get_content()
    html = unicode(content)
    p = xpath.get(html, '//div[@class="box post"]')
    linkovi = xpath.search(p, '//div[@class="content"]')
    ads = []
    for l in linkovi:
        link = "http://www.baramdom.com" + xpath.get(l, '//div[@class="post-title"]/h2/a/@href')
        title = xpath.get(l, '//div[@class="post-title"]/h2/a')
        imageUrl = xpath.get(l, '//a[@class="grouped"]/img/@src')
        if imageUrl == "":
            imageUrl = "http://www.baramdom.com/img/apartment_noimage.png"
        else:
            imageUrl = "http://www.baramdom.com" + imageUrl
        download = Downloader(link)
        cont = download.get_content()
        cont = unicode(cont)
        description = xpath.get(cont, '//p[@class="post_add_desc"]')
        description = description.strip()
        category = u"Недвижнини"
        ost = xpath.get(l, '//p[@class="add-title"]')
        ost = ost.strip()
        ost = ost.split(" во ")
        region = ost[1]
        country = u"Македонија"
        k = ost[0]
        k = k.split("ам ")
        subcategory = k[1]
        price = xpath.get(cont, '//div[@class="post-add"]/p[@class="last"]').strip()
        price = price.split(" ")
        if len(price)==3:
            value = "/"
            currency = "/"
        else:
            value = price[0]
            currency = price[1]
            if currency == "Euro.":
                currency = "EUR"
            elif currency == u"Ден.":
                currency = "MKD"
        date = xpath.get(l, '//div[@class="fl"]')
        date = date.strip()
        date = date.split(">")
        date = date[1]
        date = date.strip()
        date = date.split(" ")
        date = date[0]
        date = date.split("-")
        date = date[2]+"-"+date[1]+"-"+date[0]
        ad = Ad(link, title, imageUrl, description, category, subcategory, value, currency, region, date, country)    
        ads.append(ad)
    return adsToJson(ads)
#print scrapeBaramDom()