#!/usr/bin/env python
# coding: utf-8
from webscraping import xpath
from Downloader import Downloader
import sys
import urlparse, urllib

def adsToJson(dic):
    return ','.join(str(x.dataDict).replace('\'', '"').replace('u"', '"') for x in dic).replace('},{', ',')

def getDescription(link, path):
    try:
        reload(sys)
        sys.setdefaultencoding('utf-8')
        down = Downloader(fixurl(link))
        html = down.get_content()
#         print html
        html = unicode(html)
        description = xpath.get(html, path)
        return description
    except: 
        pass
    
def fixurl(url):
    # turn string into unicode
    if not isinstance(url,unicode):
        url = url.decode('utf8')

    # parse it
    parsed = urlparse.urlsplit(url)

    # divide the netloc further
    userpass,at,hostport = parsed.netloc.rpartition('@')
    user,colon1,pass_ = userpass.partition(':')
    host,colon2,port = hostport.partition(':')

    # encode each component
    scheme = parsed.scheme.encode('utf8')
    user = urllib.quote(user.encode('utf8'))
    colon1 = colon1.encode('utf8')
    pass_ = urllib.quote(pass_.encode('utf8'))
    at = at.encode('utf8')
    host = host.encode('idna')
    colon2 = colon2.encode('utf8')
    port = port.encode('utf8')
    path = '/'.join(  # could be encoded slashes!
        urllib.quote(urllib.unquote(pce).encode('utf8'),'')
        for pce in parsed.path.split('/')
    )
    query = urllib.quote(urllib.unquote(parsed.query).encode('utf8'),'=&?/')
    fragment = urllib.quote(urllib.unquote(parsed.fragment).encode('utf8'))

    # put it back together
    netloc = ''.join((user,colon1,pass_,at,host,colon2,port))
    return urlparse.urlunsplit((scheme,netloc,path,query,fragment))

# print fixurl("http://www.pazar3.mk/mk/Listing/AdDetail/Index/1719428-Двособен-стан--убава-состојба-Карпош-4")    
# print getDescription(fixurl("http://www.pazar3.mk/mk/Listing/AdDetail/Index/1719428-Двособен-стан--убава-состојба-Карпош-4"), '//div[@class="well well-small noback nomargin hidden-overflow"]')