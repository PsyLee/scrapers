#!/usr/bin/env python
# coding: utf-8

from webscraping import xpath
import urllib2
import sys
import re
from datetime import datetime
from Ad import Ad
from Downloader import Downloader
from datetime import date, timedelta
from datetime import datetime
from Utilities import getDescription
from Utilities import adsToJson

def scrapeKoli():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    down = Downloader('http://koli.com.mk/polovni_lista.aspx')
    html = down.get_content()
    html = unicode(html)
    requestedWebPageUrl = 'http://koli.com.mk/polovni_lista.aspx'
    adverts = xpath.search(html, '//table[@id="dlRezultati"]')
    ads = []
    links = xpath.search(html, '//a[@class="linkovi_desno_golemi"]/@href')
    da = datetime.now()
    for l in links:
        link = "http://koli.com.mk/"+l
        d = Downloader(link)
        ad = d.get_content()
        ad = unicode(ad)
        description=u"Опрема: "+ xpath.get(ad, '//span[@id="lblOprema"]')+" \nOpis: "+xpath.get(ad, '//span[@id="lblOpis"]')
        title = xpath.get(ad, '//span[@id="lblMarkaModel"].text()').strip()
        imageUrl = 'http://koli.com.mk/' + xpath.get(ad, '//img[@id="slika"]/@src')
        subcategory="/"   
        category=u"Возила"
        region=xpath.get(ad,'//span[@id="lblGrad"].text()')
        country = u"Македонија"
        value=xpath.get(ad,'//span[@id="lblMomentalnaCena"]').strip()
        currency="EUR"
        date=""
        d = xpath.get(ad, '//span[@id="lblDenovi"]').strip()
        d = d.split(" ")
        if len(d)==1:
            if d[0]==u"минута":
                date=str(da.year)+"-"+str(da.month)+"-"+str(da.day)
            elif d[0]==u"час":
                date=str(da.year)+"-"+str(da.month)+"-"+str(da.day)
            elif d[0]==u"ден":
                da=datetime.now()-timedelta(days=1)
                date=str(da.year)+"-"+str(da.month)+"-"+str(da.day)
            elif d[0]==u"месец":
                da=datetime.now()-timedelta(days=30)
                date=str(da.year)+"-"+str(da.month)+"-"+str(da.day)
            elif d[0]==u"секунда":
                date=str(da.year)+"-"+str(da.month)+"-"+str(da.day)
        else:
            if d[1]==u"месеци":
                da=datetime.now()-timedelta(days=int(d[0]*30))
                date=str(da.year)+"-"+str(da.month)+"-"+str(da.day)
            elif d[1]==u"дена":
                da=datetime.now()-timedelta(days=int(d[0]))
                date=str(da.year)+"-"+str(da.month)+"-"+str(da.day)
            elif d[1]==u"минути":
                date=str(da.year)+"-"+str(da.month)+"-"+str(da.day)
            elif d[1]==u"часа":
                date=str(da.year)+"-"+str(da.month)+"-"+str(da.day)
            elif d[1]==u"секунди":
                date=str(da.year)+"-"+str(da.month)+"-"+str(da.day)
        
        ad = Ad(link, title, imageUrl, description, category, subcategory, value, currency, region, date, country) 
        ads.append(ad) 
        
    return adsToJson(ads)
    
print scrapeKoli()
