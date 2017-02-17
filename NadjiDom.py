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

def scrapeNadjiDom():
    # UTF-8 support
    reload(sys)
    sys.setdefaultencoding('utf-8')
    now = datetime.now()
    down = Downloader('http://www.nadjidom.com/sr/search?mode=quick&ad_type=1&description=&&')
    content = down.get_content()
    html = unicode(content)
    link=""
    title=""
    imageUrl=""
    description="/"
    category=u"Недвижнини"
    subcategory="/"
    value="/"
    currency="/"
    region="/"
    date=""
    ads = []
    linkovi = xpath.search(html, '//div[@class="listContainer gold gainlayout"]')
    links = xpath.search(html, '//div[@class="listContainer silver gainlayout"]')
    for l in links:
        linkovi.append(l)
    links = xpath.search(html, '//div[@class="listContainer  gainlayout"]')
    for l in links:
        linkovi.append(l)
    
    down = Downloader('http://www.nadjidom.com/sr/search?mode=quick&ad_type=2&description=&&')
    content = down.get_content()
    html = unicode(content)
    lin = xpath.search(html, '//div[@class="listContainer gold gainlayout"]')
    for l in lin:
        linkovi.append(l)
    links = xpath.search(html, '//div[@class="listContainer silver gainlayout"]')
    for l in links:
        linkovi.append(l)
    links = xpath.search(html, '//div[@class="listContainer  gainlayout"]')
    for l in links:
        linkovi.append(l)
    
    down = Downloader('http://www.nadjidom.com/sr/search?mode=quick&ad_type=3&description=&&')
    content = down.get_content()
    html = unicode(content)
    li = xpath.search(html, '//div[@class="listContainer  gainlayout"]')
    for l in li:
        linkovi.append(l)
    links = xpath.search(html, '//div[@class="listContainer silver gainlayout"]')
    for l in links:
        linkovi.append(l)
    links = xpath.search(html, '//div[@class="listContainer gold gainlayout"]')
    for l in links:
        linkovi.append(l)

    print len(linkovi)   
     
    for l in linkovi:
        link = xpath.get(l, '//div[@class="pictureContainer"]/a/@href')
        title = xpath.get(l, '//div[@class="pictureContainer"]/@title')
        title = title.replace("&nbsp;", " ")
        region = xpath.get(l, '//div[@class="cityName"]')
        price = xpath.get(l, '//div[@class="listPrice"]')
        if price == "Dogovor":
            value = "/"
            currency = "/"
        else:
            price = price.replace(".", "")
            price = price.split("&nbsp;")
            value = price[0]
            currency = price[1]
            if currency == "€":
                currency = "EUR"
        datum = xpath.get(l, '//div[@class="date_update"]/span')
        datum = datum.split("/")
        datum[2]="20"+datum[2]
        date = datum[2]+"-"+datum[1]+"-"+datum[0]
        subcategory = xpath.get(l, '//div[@class="type_name ext-font-f1-v1"]')
        download = Downloader(link)
        cont = download.get_content()
        cont = unicode(cont)
        imageUrl = xpath.get(cont, '//a[@class="lightbox"]/@href')
        country = u"Србија"
        description = xpath.get(cont, '//div[@class="leftBlock"]/div/p')
        if description == "":
            description="/"
    ad = Ad(link, title, imageUrl, description, category, subcategory, value, currency, region, date, country)    
    ads.append(ad)
    
    return adsToJson(ads)
#print scrapeNadjiDom()