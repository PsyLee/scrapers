#!/usr/bin/env python
# coding: cp1251
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
def scrapeMobileBg():
    # cp1251 support
    reload(sys)
    sys.setdefaultencoding('cp1251')
    now = datetime.now()
    down = Downloader('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71wxzy&f1=1')
    #http://www.mobile.bg/71ydeh
    #http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71wxzy&f1=1
    content = down.get_content()
    html = unicode(content)
    linkovi = xpath.search(html, '//form[@name="search"]/table[@class="tablereset"]')
    linkovi = linkovi[3:len(linkovi)-4]
    
    links = []
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71xw69&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71xwi1&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71xwr0&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71xx7g&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71xxjy&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71xzyr&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71y06e&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71y0dk&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71y0q6&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71y16v&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71y1ep&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71y2ih&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71y2x5&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71y34p&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71y3ex&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71y3wj&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71y449&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71y4wz&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71y5qh&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71y5yv&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71y6az&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71y6kg&f1=1')
    links.append('http://www.mobile.bg/pcgi/mobile.cgi?act=3&slink=71y6qz&f1=1')
     
    for link in links:
        dole = Downloader(link)
        content = dole.get_content()
        html = unicode(content)
        lin = xpath.search(html, '//form[@name="search"]/table[@class="tablereset"]')
        lin = lin[3:len(lin)-4]
        for li in lin:
            linkovi.append(li)
            linkot = xpath.get(li, '//td[@class="valgtop"]/a[@class="mmm"]/@href')

    ads = []
    for l in linkovi:
        link = xpath.get(l, '//td[@class="valgtop"]/a[@class="mmm"]/@href')
        title = xpath.get(l, '//td[@class="valgtop"]/a[@class="mmm"]').strip()
        imageUrl = xpath.get(l, '//a[@class="photoLink"]/img/@src')
        download = Downloader(link)
        cont = download.get_content()
        cont = unicode(cont)
        description = xpath.get(cont, '//td[@style="font-size:13px;"]').strip()
        description = description.split("<a href")
        description = description[0]
        if description == "» ":
            description = "/"
        else:
            description = description[0:len(description)-19]
        description = description = description.replace("\"", "")
        category = u"Возила"
        subcategory = "/"
        price = xpath.get(l, '//span[@class="price"]').strip()
        if price == u"Договаряне":
            value = "/"
            currency = "/"
        else:
            price = price.split(" ")
            if len(price)==2:
                value = price[0]
                currency = price[1]
            elif len(price)==3:
                currency = price[2]
                value = price[0]+price[1]
            else:
                currency = price[3]
                value = price[0]+price[1]+price[2]
            if currency == "лв.":
                currency = "BGN"        
        region = xpath.get(cont, '//td[@style="padding:10px"]').strip()
        region = region.split("Регион: ")
        region = region[1]
        region = region.split(" ")
        region = region[0]
        region = region.replace("<a","").strip()
        date = str(now.year)+"-"+str(now.month)+"-"+str(now.day)
        country = u"Бугарија"
        
        ad = Ad(link, title, imageUrl, description, category, subcategory, value, currency, region, date, country)    
        ads.append(ad)
    return adsToJson(ads)
#print scrapeMobileBg()