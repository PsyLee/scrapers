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

def scrapeOglasiRs():
    # UTF-8 support
    reload(sys)
    sys.setdefaultencoding('utf-8')
    now = datetime.now()
    down = Downloader('http://www.oglasi.rs/pretraga/0/0/')
    content = down.get_content()
    html = unicode(content)

    linkovi = xpath.search(html, '//li[@class="clearfix"]')
    ads = []
    for l in linkovi:
        link = xpath.get(l, '//a[@class="ogl_id"]/@href')
        title = xpath.get(l, '//h2/a[@class="ogl_id"].text()')
        imageUrl ="http://oglasi.rs" + xpath.get(l, '//a[@class="ogl_id"]/img/@src')
        price = xpath.get(l, '//div[@class="ad-price"]/h3')
        datum = xpath.get(l, '//div[@class="right-side"]/div/p/strong')
        datum = datum.split(".")
        date = datum[2]+"-"+datum[1]+"-"+datum[0]
        price = price.split(" ")
        price[0] = price[0].replace(".","")
        currency = price[1]
        value = price[0]
        value = value.split(",")
        value = value[0]
        download = Downloader(link)
        ad = download.get_content()
        ad = unicode(ad)
        description = xpath.search(ad, '//div[@class="description"]/p')
        description = description[1].strip()
        category="/"
        subcategory="/"
        loc = xpath.search(ad, '//div[@class="description"]/ul[@class="clearfix"]')
        lo = xpath.search(loc[0], '//li')
        region = lo[1]
        region = region.split("(")
        region = region[0]
        region = region.strip()
        country = u"Србија"
        ad = Ad(link, title, imageUrl, description, category, subcategory, value, currency, region, date, country)    
        ads.append(ad)
    return adsToJson(ads)

#print scrapeOglasiRs()