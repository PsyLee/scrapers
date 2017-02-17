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
from PyQt4.Qt import dec
def scrapePobarajOglasi():
    # UTF-8 support
    reload(sys)
    sys.setdefaultencoding('utf-8')
    now = datetime.now()
    down = Downloader('http://www.pobaraj.com.mk/lista_na_oglasi/all/1')
    content = down.get_content()
    html = unicode(content)
    site = xpath.get(html, '//ul[@class="lista_na_oglasi"]')
    linkovi = xpath.search(site, '//li')
    ads = []
    for l in linkovi:
        link = "http://www.pobaraj.com.mk" + xpath.get(l, '//a[@class="title"]/@href')
        title = xpath.get(l, '//a[@class="title"]')
        imageUrl = xpath.get(l, '//a[@class="photo"]/img/@src')
        download = Downloader(link)
        cont = download.get_content()
        cont = unicode(cont)
        description = xpath.get(cont, '//div[@class="oglas_prikaz_opis"]').strip()
        if description == "":
            description = "/"
        kategorii = xpath.search(cont, '//a[@class="pateka"]')
        category = kategorii[1]
        if len(kategorii)>2:
            subcategory = kategorii[2]
        else:
            subcategory = "/"
        price = xpath.get(l, '//div[@class="price"]').strip()
        price = price.split("<div ")
        price = price[0].strip()
        price = price.split("Цена: ")
        price = price[1]
        if price == u"по договор":
            value = "/"
            currency = "/"
        else:
            price = price.split(" ")
            value = price[0]
            if price[1] == u"денари":
                currency = "MKD"
            elif price[1] == u"евра":
                currency = "EUR"
            else:
                currency = price[1]
        region = xpath.get(cont, '//div[@class="oglas_prikaz_left"]').strip()
        region = region.split("Град:<")
        region = region[1]
        region = region.split("<b class")
        region = region[0]
        region = region.split("b>")
        region = region[1]
        region = region.strip()
        country = u"Македонија"
        
        datum = xpath.get(l, '//div[@class="oglas_date"]').strip()
        datum = datum.split(": ")
        datum = datum[1]
        datum = datum.split(", ")
        vreme = datum[1]
        datum = datum[0]
        if datum == u"Денес":
            date = str(now.year)+"-"+str(now.month)+"-"+str(now.day)+" "+vreme
        elif datum == u"Вчера":
            da=datetime.now()-timedelta(days=1)
            date = str(da.year)+"-"+str(da.month)+"-"+str(da.day)+" "+vreme
        else:
            datum = datum.split(" ")
            if datum[1]=="Јан":
                datum= str(now.year) + "-1-" + datum[0]
            elif datum[1]=="Фев":
                datum= str(now.year) + "-2-" + datum[0]
            elif datum[1]=="Мар":
                datum= str(now.year) + "-3-" + datum[0]
            elif datum[1]=="Апр":
                datum= str(now.year) + "-4-" + datum[0]
            elif datum[1]=="Мај":
                datum= str(now.year) + "-5-" + datum[0]
            elif datum[1]=="Јун":
                datum= str(now.year) + "-6-" + datum[0]
            elif datum[1]=="Јул":
                datum= str(now.year) + "-7-" + datum[0]
            elif datum[1]=="Авг":
                datum= str(now.year) + "-8-" + datum[0]
            elif datum[1]=="Сеп":
                datum= str(now.year) + "-9-" + datum[0]
            elif datum[1]=="Окт":
                datum= str(now.year) + "-10-" + datum[0]
            elif datum[1]=="Ное":
                datum= str(now.year) + "-11-" + datum[0]
            elif datum[1]=="Дек":
                datum= str(now.year) + "-12-" + datum[0]
            date = datum +" "+ vreme
        ad = Ad(link, title, imageUrl, description, category, subcategory, value, currency, region, date, country)    
        ads.append(ad)
    return adsToJson(ads)
#print scrapePobarajOglasi()