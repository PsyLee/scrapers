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

def scrapeAvtodelovi():
    # UTF-8 support
    reload(sys)
    sys.setdefaultencoding('utf-8')
    now = datetime.now()
    down = Downloader('http://www.avtooglasi.com.mk/avtodelovi/site/?page=0&orderby=0')
    content = down.get_content()
    html = unicode(content)
    celo = xpath.get(html, '//table[@class="table table-hover table-condensed"]')

    sliki = xpath.search(celo, '//div[@style="width: 120px;float:left;"]')
    ostanato = xpath.search(celo, '//div[@style="width: 568px;float:left;"]')
       
    ads = []
    for t in sliki:

        l = xpath.search(t, '/a/@href')
        link = l[0]
        tl = xpath.search(t, '/a/@title')
        subcategory = tl[0]
        img = xpath.search(t, '//img/@src')
        imageUrl = img[0]        
        dn = Downloader(link)
        cont = dn.get_content()
        ost = unicode(cont)
        os = xpath.search(ost, '//div[@class="centerC"]')
        category = u"Автоделови"
        tl = xpath.search(os[0], '//h3[@style="margin-top: 5px;"]')
        title = tl[0].strip().replace("\"", "")
        ds = xpath.search(os[0], '//div[@style="padding: 5px;"]')
        description = ds[1].strip().replace("\"", "")
        val = xpath.search(os[0], '//table[@class="table table-condensed"]')
        l = xpath.search(val[1], '//tr/td/strong')
        region = l[1].strip()
        country = u"Македонија"
        v = xpath.get(os[0], '//span[@class="label label-info"]')
        v = v.strip()
        v = v.split(" ")
        if v[1]=="&euro;":
            currency = "EUR"
        else:
            currency = "MKD"
        value =  v[0]
        sve = xpath.search(os[0], '//table[@class="table table-condensed"]')
        d = xpath.search(sve[0], '//tr/td/strong')
        dat = d[1].strip().split(" ")
        if len(dat)>2:
            if dat[0] == u"Денес":
                date = str(now.year)+"-"+str(now.month)+"-"+str(now.day)+" "+dat[2]
            elif dat[0] == u"Вчера":
                da=datetime.now()-timedelta(days=1)
                date= str(da.year)+"-"+str(da.month)+"-"+str(da.day)+" "+dat[2]
            elif dat[0] == u"пред":
                if dat[2] == u"дена":
                    da=datetime.now()-timedelta(days=int(dat[1]))
                    date=str(da.year)+"-"+str(da.month)+"-"+str(da.day)
                elif dat[2] == u"месец":
                    da=datetime.now()-timedelta(days=30)
                    date=str(da.year)+"-"+str(da.month)+"-"+str(da.day)
                else:
                    da=datetime.now()-timedelta(days=60)
                    date=str(da.year)+"-"+str(da.month)+"-"+str(da.day)
        else:
            date = ""
            da=datetime.now()-timedelta(days=90)
            date=str(da.year)+"-"+str(da.month)+"-"+str(da.day)
#         print date   

        ad = Ad(link, title, imageUrl, description, category, subcategory, value, currency, region, date, country)    
        ads.append(ad)
        
    return adsToJson(ads)

# print scrapeAvtodelovi()