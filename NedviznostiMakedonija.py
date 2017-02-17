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
def scrapeNedviznostiMakedonija():
    # UTF-8 support
    reload(sys)
    sys.setdefaultencoding('utf-8')
    now = datetime.now()
    down = Downloader('http://www.nedviznostimakedonija.com.mk/Default.aspx?search=1')
    content = down.get_content()
    html = unicode(content)
    linkovi = xpath.search(html, '//div[@class="boxesResultNewTop"]')
    ads = []
    for l in linkovi:
        link = "http://www.nedviznostimakedonija.com.mk/" + xpath.get(l, '//a[@class="subjectLook nobackim"]/@href')
        title = xpath.get(l, '//a[@class="subjectLook nobackim"]').strip()
        imageUrl = "http://www.nedviznostimakedonija.com.mk/" + xpath.get(l, '//a[@class="nobackim"]/img/@src')
        download = Downloader(link)
        cont = download.get_content()
        cont = unicode(cont)
        description = xpath.get(cont, '//span[@id="Body1_DetailControl1_FormView1_Label5"]')
        category = u"Недвижнини"
        subcategory="/"
        price = xpath.get(l, '//div[@style="float:right; color:#1b5474; font-size:14px; font-weight:bold;"]/span')
        price = price.split(" ")
        price[0] = price[0].replace(".","")
        if price[1] == "&#8364;":
            price[1]="EUR"
        else:
            price[1]="MKD" 
        value = price[0]
        currency = price[1]
        region = xpath.get(cont, '//span[@id="Body1_DetailControl1_FormView1_cityDescriptionLabel"]')
        country = u"Македонија"
        date = xpath.get(cont, '//span[@id="Body1_DetailControl1_FormView1_LabelDate"]')
        date = date.split(".")
        date = date[2]+"-"+date[1]+"-"+date[0]
        ad = Ad(link, title, imageUrl, description, category, subcategory, value, currency, region, date, country)    
        ads.append(ad)
    return adsToJson(ads)
#print scrapeNedviznostiMakedonija()