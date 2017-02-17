#!/usr/bin/env python
# coding: utf-8

class Ad(object):
    def __init__(self, url, title, imageUrl, description, category, subcategory, value, currency, region, date, country):
        self.dataDict = {}
        self.url = url
        self.title = title
        self.imageUrl = imageUrl
        self.description = description
        self.category = category
        self.subcategory = subcategory
        self.value = value
        self.currency = currency
        self.region = region
        self.date = date
        self.country = country
        self.setDictionary()
        
    def setDictionary (self):
        addInfo = {}
        addInfo['title'] = self.title
        addInfo['imageUrl'] = self.imageUrl
        addInfo['description'] = self.description
        addInfo['category'] = self.category
        addInfo['subcategory'] = self.subcategory
        addInfo['value'] = self.value
        addInfo['currency'] = self.currency
        addInfo['region'] = self.region
        addInfo['date'] = self.date
        addInfo['country'] = self.country
        self.dataDict [self.url] = addInfo
        
# TEST STUB        
# ad = Ad("http://www.vrapce.mk/ad/31556", "1", "2", "3", "4", "5", "6", "7", "8", "9")
# print ad.dataDict
# 
# dic=[]
# 
# for i in range(0,3):
#     dic.append(ad)
# 
# str = ','.join(str(x.dataDict).replace('\'', '"') for x in dic)
# print str.replace('},{', ',')