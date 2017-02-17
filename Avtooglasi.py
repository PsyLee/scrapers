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

def scrapeAvtooglasi():
    # UTF-8 support
    reload(sys)
    sys.setdefaultencoding('utf-8')
    now = datetime.now()
    down = Downloader('http://www.avtooglasi.com.mk/rezultati/show/?vid=0&orderby=0')
    content = down.get_content()
    html = unicode(content)
    sliki = xpath.search(html, '//div[@class="resultLeft"]')
    ostanato = xpath.search(html, '//div[@class="oglasInfoTopContent"]')
    ceni = xpath.search(html, '//a[@class="btn btn-info btn-xs oglasInfoAdditionalPrice"]')
    
    link = {}
    title = {}
    imageUrl = {}
    description = {}
    category = {}
    subcategory = {}
    value = {}
    currency = {}
    region =  {}
    date = {}
    
    i = 0
    
    ads = []
    for slika in sliki:
        imageUrl[i] = xpath.search(slika, '//a[@class="thumbnail resultImg"]/img/@src')[0]
        i = i + 1
    
    i = 0
    
    for cena in ceni:
        price = xpath.get(cena,'//span/span').strip()
        price=price.split(" ")
        if len(price)>1:
            if price[0]=="По":
                price[0]="/"
            if price[1]=="договор":
                price[1]="/"
        
            value[i]=price[0]
            currency[i]=price[1]
            if currency[i]=="&euro;":
                currency[i]="EUR"  
        i = i + 1
        
    i = 0
    
    for advert in ostanato:
        link[i] = xpath.get(advert, '//a[@class="resultMainLink"]/@href')       
        title[i] = xpath.get(advert, '//a[@class="resultMainLink"]/span').strip().replace("\"", "")
        
        path = xpath.search(getDescription(link[i],'//div[@class="centerC"]'), '/div/div[@class="padded"]')
        description[i] = path[1]
        subcategory[i]="/"    
        category[i] = u"Возила"
        
        dodatok = xpath.get(advert, '//span[@class="oglasInfoAdditionalInfo"]')
        dodatok = dodatok.split(" | ")
        region[i] = dodatok[0]
        country = u"Македеонија"
        description[i] = dodatok[1] + u" година, "+ dodatok[2] +", "+ dodatok[3] +", "+ dodatok[4] +", "+ dodatok[5] +", "+ description[i]
        description[i] = description[i].strip().replace("\"", "")

        date[i]=""
        #print description[i]
        datum = dodatok[6].strip()
        datum = datum.split(" ")
        if datum[0]=="Денес":
            datum [0]= str(now.year)+"-"+str(now.month)+"-"+str(now.day)
            date[i]=datum[0]+" "+datum[2]
        elif datum[0]=="Вчера":
            da=datetime.now()-timedelta(days=1)
            datum[0]=str(da.year)+"-"+str(da.month)+"-"+str(da.day)
            date[i]=datum[0]+" "+datum[2]
        elif datum[0]=="пред":
            if datum[2]=="дена":
                da=datetime.now()-timedelta(days=int(datum[1]))
                datum[0]=str(da.year)+"-"+str(da.month)+"-"+str(da.day)
                date[i]=datum[0]
            else:
                if datum[1]=="1":
                    da=datetime.now()-timedelta(days=30)
                    datum[0]=str(da.year)+"-"+str(da.month)+"-"+str(da.day)
                    date[i]=datum[0]
                else:
                    da=datetime.now()-timedelta(days=60)
                    datum[0]=str(da.year)+"-"+str(da.month)+"-"+str(da.day)
                    date[i]=datum[0]
        else:
            date[i]=datum[0]+" "+datum[1]

        #print date[i]
        i = i + 1
        
    for i in link:
        ad = Ad(link[i], title[i], imageUrl[i], description[i], category[i], subcategory[i], value[i], currency[i], region[i], date[i], country)    
        ads.append(ad)
        
    return adsToJson(ads)

# print scrapeAvtooglasi()