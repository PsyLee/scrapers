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

def scrapeHaloOglasi():
    # UTF-8 support
    reload(sys)
    sys.setdefaultencoding('utf-8')
    now = datetime.now()
    down = Downloader('http://www.halooglasi.com/naslovna.240.html?search_text=&sortColumn=VremeDodavanja')
    content = down.get_content()
    html = unicode(content)
    celo = xpath.get(html, '//div[@class="results_container"]')
    linkovi = xpath.search(celo, '//div[@class="result_brza"]')
    ads = []
    for l in linkovi:
        link = xpath.get(l, '//div[@style="height:auto;"]/h2/a/@href')
        link = "http://www.halooglasi.com" + link
        download = Downloader(link)
        cont = download.get_content()
        cont = unicode(cont)
        title = xpath.get(cont, '//div[@class="detail_bar_nek"]/h2').strip()
        if title == "":
            title = xpath.get(cont, '//div[@class="detail_bar"]/h2').strip()
        imageUrl= xpath.get(l, '//a[@class="thumb"]/img/@src')
        imageUrl = "http://www.halooglasi.com" + imageUrl
        
        description= xpath.get(l, '//div[@class="text_ogl"]/p')
        
        kategorija = xpath.get(l, '//div[@class="brza_link"]').strip()
        kategorija = kategorija.split("\r\n\t\t\t\t\t\t\r\n\t\t\t\t\t\t")
        kategorija = kategorija[1]
        kategorija = kategorija.split(" > ")
        category=kategorija[0]
        if len(kategorija)>2:
            subcategory=kategorija[1]
        else:
            kategorija = kategorija[1].split("'>")
            kategorija = kategorija[1]
            kategorija = kategorija.split("<")
            subcategory = kategorija[0]
        price = xpath.get(cont, '//div[@class="price"]').strip() #price
        if price == "":
            price = xpath.get(cont, '//div[@class="price deal"]').strip()#price deal
        price = price.replace(".", "")
        price = price.replace("din", " DIN")
        price = price.replace("&euro;", " EUR")
        if price == "Dogovor":
            value = "/"
            currency = "/"
        else:
            price = price.split(" ")
            value = price[0]
            currency = price[1]
        date_loc = xpath.search(l, '//div[@class="datum_grad"]/h6/span')
        date_loc[0] = date_loc[0].strip()
        date = date_loc[0].split("\r\n")
        date = date[0]
        date = date.replace(".","")
        date = date.split(" ")
        if date[1]=="Jan":
            date[1]="1"
        elif date[1]=="Feb":
            date[1]="2"
        elif date[1]=="Mar":
            date[1]="3"
        elif date[1]=="Apr":
            date[1]="4"
        elif date[1]=="Maj":
            date[1]="5"
        elif date[1]=="Jun":
            date[1]="6"
        elif date[1]=="Jul":
            date[1]="7"
        elif date[1]=="Avg":
            date[1]="8"
        elif date[1]=="Sep":
            date[1]="9"
        elif date[1]=="Okt":
            date[1]="10"
        elif date[1]=="Nov":
            date[1]="11"
        elif date[1]=="Dec":
            date[1]="12"
        date = date[2]+"-"+date[1]+"-"+date[0]
        l = date_loc[1].strip()
        l = l.split("&nbsp;")
        region = l[0]
        country = u"Србија"

        ad = Ad(link, title, imageUrl, description, category, subcategory, value, currency, region, date, country)    
        ads.append(ad)
        
    return adsToJson(ads)

#print scrapeHaloOglasi()