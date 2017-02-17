#!/usr/bin/env python
# coding: utf-8
from webscraping import xpath
import urllib2
import sys
from Downloader import Downloader
import json
from Ad import Ad
from datetime import datetime
from datetime import date, timedelta
from Utilities import adsToJson
from Utilities import getDescription
import re
from pydoc import describe
from urllib2 import quote

def scrapePazar3():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    down = Downloader('http://www.pazar3.mk/mk/Listing/Home/Search?CookieLocationId=0&Location=0-%D0%A6%D0%B5%D0%BB%D0%B0-%D0%9C%D0%B0%D0%BA%D0%B5%D0%B4%D0%BE%D0%BD%D0%B8%D1%98%D0%B0&_=1404733181509')
    content = down.get_content()
    content = unicode(content)
    dump = json.loads(content)
    t = dump["data"]
    ads = []
    items = t["Items"]
    now = datetime.now()
    for f in items:
        title = f["Title"]
        title = title.replace("\"", "")
        category = f["Category"]["Name"]
        
        if f["Price"]=="":
            value = "/"
        else:
            value = f["Price"]
        
        if f["Currency"]=="ЕУР":
            currency = "EUR"
        elif f["Currency"]=="":
            currency = "/"
        else:
            currency = f["Currency"]
            
        region = f["Location"]["Name"]
        link = "http://www.pazar3.mk/mk/Listing/AdDetail/Index/"+ f["IdSeo"]
        country = u"Македонија"

        imagedate = str(f["ImageDate"])
        imagetitle = str(f["ImageTitle"])
        if imagedate == 'None' or imagetitle == 'None':
            imageUrl = "/"
        else:        
            imageUrl = "http://media.pazar3.mk/ImageHandler.ashx?date="+f["ImageDate"]+"&guid="+f["ImageTitle"]+"&width=300&height=225&isVideo=false"
        
        description = ""
        description = getDescription(link, '//div[@class="well well-small noback nomargin hidden-overflow"]')
        
        if description is None:
            description = "/"
        else:
            description = description.strip()
            description = description.replace("\"", "")
                
        subcategory = "/"
        d = f["CreateDate"].split(" ")
        if len(d)==2:
            if d[0]=="Денес":
                d[0]=str(now.year)+"-"+str(now.month)+"-"+str(now.day)
            elif d[0]=="Вчера":
                da=datetime.now()-timedelta(days=1)
                d[0]=str(da.year)+"-"+str(da.month)+"-"+str(da.day)
                
            date=d[0]+" "+d[1]
        else:
            if d[1]=="јан":
                date="1-"+d[0]+" "+d[2]
            elif d[1]=="фев":
                date="2-"+d[0]+" "+d[2]
            elif d[1]=="мар":
                date="3-"+d[0]+" "+d[2]
            elif d[1]=="апр":
                date="4-"+d[0]+" "+d[2]
            elif d[1]=="мај":
                date="5-"+d[0]+" "+d[2]
            elif d[1]=="јун":
                date="6-"+d[0]+" "+d[2]
            elif d[1]=="јул":
                date="7-"+d[0]+" "+d[2]
            elif d[1]=="авг":
                date="8-"+d[0]+" "+d[2]
            elif d[1]=="сеп":
                date="9-"+d[0]+" "+d[2]
            elif d[1]=="окт":
                date="10-"+d[0]+" "+d[2]
            elif d[1]=="ное":
                date="11-"+d[0]+" "+d[2]
            elif d[1]=="дек":
                date="12-"+d[0]+" "+d[2]
            date = str(now.year)+"-"+date
        if currency == u"МКД":
            currency = "MKD"
        ad = Ad(link, title, imageUrl, description, category, subcategory, value, currency, region, date, country)    
        #print link, title, imageUrl, description, category, subcategory, value, currency, region, date
        ads.append(ad)
        
    first = t["FirstPositionItems"]
    for f in first:
        title = f["Title"]
        title = title.replace("\"", "")
        category = f["Category"]["Name"]
        
        if f["Price"]=="":
            value = "/"
        else:
            value = f["Price"]
        
        if f["Currency"]=="ЕУР":
            currency = "EUR"
        elif f["Currency"]=="":
            currency = "/"
        else:
            currency = f["Currency"]
            
        region = f["Location"]["Name"]
        link = "http://www.pazar3.mk/mk/Listing/AdDetail/Index/"+ f["IdSeo"]
        country = u"Македонија"
        imagedate = str(f["ImageDate"])
        imagetitle = str(f["ImageTitle"])
        if imagedate == 'None' or imagetitle == 'None':
            imageUrl = "/"
        else:        
            imageUrl = "http://media.pazar3.mk/ImageHandler.ashx?date="+f["ImageDate"]+"&guid="+f["ImageTitle"]+"&width=300&height=225&isVideo=false"
        
        description = ""
        description = getDescription(link, '//div[@class="well well-small noback nomargin hidden-overflow"]')

        if description is None:
            description = "/"
        else:
            description = description.strip()
            description = description.replace("\"", "")
        
        subcategory = "/"
        d = f["CreateDate"].split(" ")
        if len(d)==2:
            if d[0]=="Денес":
                d[0]=str(now.year)+"-"+str(now.month)+"-"+str(now.day)
            elif d[0]=="Вчера":
                da=datetime.now()-timedelta(days=1)
                d[0]=str(da.year)+"-"+str(da.month)+"-"+str(da.day)
                
            date=d[0]+" "+d[1]
        else:
            if d[1]=="јан":
                date="1-"+d[0]+" "+d[2]
            elif d[1]=="фев":
                date="2-"+d[0]+" "+d[2]
            elif d[1]=="мар":
                date="3-"+d[0]+" "+d[2]
            elif d[1]=="апр":
                date="4-"+d[0]+" "+d[2]
            elif d[1]=="мај":
                date="5-"+d[0]+" "+d[2]
            elif d[1]=="јун":
                date="6-"+d[0]+" "+d[2]
            elif d[1]=="јул":
                date="7-"+d[0]+" "+d[2]
            elif d[1]=="авг":
                date="8-"+d[0]+" "+d[2]
            elif d[1]=="сеп":
                date="9-"+d[0]+" "+d[2]
            elif d[1]=="окт":
                date="10-"+d[0]+" "+d[2]
            elif d[1]=="ное":
                date="11-"+d[0]+" "+d[2]
            elif d[1]=="дек":
                date="12-"+d[0]+" "+d[2]
            date = str(now.year)+"-"+date
#         print date
        if currency == u"МКД":
            currency = "MKD"
        ad = Ad(link, title, imageUrl, description, category, subcategory, value, currency, region, date, country)    
        #print link, title, imageUrl, description, category, subcategory, value, currency, region, date
        ads.append(ad)
    
    return adsToJson(ads)

# print scrapePazar3()