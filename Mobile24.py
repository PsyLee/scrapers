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

def scrapeMobile24():
    # UTF-8 support
    reload(sys)
    sys.setdefaultencoding('utf-8')
    now = datetime.now()
    #http://www.mobile24.mk/avtomobili/'
    down = Downloader('http://www.mobile24.mk/avtomobili/')
    content = down.get_content()
    html = unicode(content)
    linkovi = xpath.search(html, '//tr[@class="t0"]')
    lin = xpath.search(html, '//tr[@class="t1"]')
    for l in lin:
        linkovi.append(l)
    #http://www.mobile24.mk/motocikli/
    down = Downloader('http://www.mobile24.mk/motocikli/')
    content = down.get_content()
    html = unicode(content)
    linko = xpath.search(html, '//tr[@class="t0"]')
    lin = xpath.search(html, '//tr[@class="t1"]')
    for l in lin:
        linkovi.append(l)
    for l in linko:
        linkovi.append(l)
    #http://www.mobile24.mk/kombinja/
    down = Downloader('http://www.mobile24.mk/kombinja/')
    content = down.get_content()
    html = unicode(content)
    linko = xpath.search(html, '//tr[@class="t0"]')
    lin = xpath.search(html, '//tr[@class="t1"]')
    for l in lin:
        linkovi.append(l)
    for l in linko:
        linkovi.append(l)
    #http://www.mobile24.mk/kamioni/
    down = Downloader('http://www.mobile24.mk/kamioni/')
    content = down.get_content()
    html = unicode(content)
    linko = xpath.search(html, '//tr[@class="t0"]')
    lin = xpath.search(html, '//tr[@class="t1"]')
    for l in lin:
        linkovi.append(l)
    for l in linko:
        linkovi.append(l)
    #http://www.mobile24.mk/prikolki/
    down = Downloader('http://www.mobile24.mk/prikolki/')
    content = down.get_content()
    html = unicode(content)
    linko = xpath.search(html, '//tr[@class="t0"]')
    lin = xpath.search(html, '//tr[@class="t1"]')
    for l in lin:
        linkovi.append(l)
    for l in linko:
        linkovi.append(l)
    #http://www.mobile24.mk/avtobusi/
    down = Downloader('http://www.mobile24.mk/avtobusi/')
    content = down.get_content()
    html = unicode(content)
    linko = xpath.search(html, '//tr[@class="t0"]')
    lin = xpath.search(html, '//tr[@class="t1"]')
    for l in lin:
        linkovi.append(l)
    for l in linko:
        linkovi.append(l)
    #http://www.mobile24.mk/gumiiavtodelovi/
    down = Downloader('http://www.mobile24.mk/gumiiavtodelovi/')
    content = down.get_content()
    html = unicode(content)
    linko = xpath.search(html, '//tr[@class="t0"]')
    lin = xpath.search(html, '//tr[@class="t1"]')
    for l in lin:
        linkovi.append(l)
    for l in linko:
        linkovi.append(l)
    
    ads = []
    for l in linkovi:
        link = xpath.get(l, '//a[@class="listing-title"]/@href')
        title = xpath.get(l, '//a[@class="listing-title"]/b')
        imageUrl = xpath.get(l, '//td[@class="image"]/a/img/@src')
        download = Downloader(link)
        cont = download.get_content()
        cont = unicode(cont)
        desc = xpath.search(cont, '//div[@class="item-left"]/div[@class="fieldset rounded4"]/div')
        if len(desc)==4:
            description = desc[1]
        else:
            description = desc[0]
        category=u"Возила"
        subcategory="/"
        price = xpath.get(l, '//td[@class="price"].text()')
        value = xpath.get(l, '//td[@class="price"]/span')
        value = value.replace(",","")
        price = price.split("span>")
        price = price[2]
        price = price.split("<")
        price = price[0]
        currency = price
        if currency == u"денари":
            currency = "MKD"
        if value == u"По договор":
            value = "/"
            currency = "/"
        region = xpath.get(l, '//span[@class="city"]')
        date = str(now.year)+"-"+str(now.month)+"-"+str(now.day)
        country = u"Македонија"

        ad = Ad(link, title, imageUrl, description, category, subcategory, value, currency, region, date, country)    
        ads.append(ad)
    return adsToJson(ads)

# print scrapeMobile24()