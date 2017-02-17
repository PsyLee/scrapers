#!/usr/bin/env python
# coding: utf-8

class Link(object):
    def __init__(self, url, imageUrl):
        self.dataDict = {}
        self.url = url
        self.imageUrl = imageUrl
        self.setDictionary()
        
    def setDictionary (self):
        addInfo = {}
        addInfo['imageUrl'] = self.imageUrl
        self.dataDict [self.url] = addInfo

