#!/usr/bin/env python
# coding: utf-8

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from Reklama5 import scrapeReklama5
from Pazar3 import scrapePazar3
from Avtooglasi import scrapeAvtooglasi
from Avtodelovi import scrapeAvtodelovi
from Koli import scrapeKoli
from BaramDom import scrapeBaramDom
from HaloOglasi import scrapeHaloOglasi
from KupujemProdajem import scrapeKupujemProdajem
from Mobile24 import scrapeMobile24
from MobileBg import scrapeMobileBg
from NadjiDom import scrapeNadjiDom
from NedviznostiMakedonija import scrapeNedviznostiMakedonija
from OglasiRs import scrapeOglasiRs
from PobarajOglasi import scrapePobarajOglasi
from VipMarket5 import scrapeVipMarket5

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler)
server.register_introspection_functions()

# Register a function under a different name
def adder_function(x,y):
    return x + y
server.register_function(adder_function, 'add')

def scrapeReklama5Func():
    rendered = scrapeReklama5()
    return rendered
server.register_function(scrapeReklama5Func, 'scrapeReklama5')

def scrapePazar3Func():
    rendered = scrapePazar3()
    return rendered
server.register_function(scrapePazar3Func, 'scrapePazar3')

def scrapeAvtoDeloviFunc():
    rendered = scrapeAvtodelovi()
    return rendered
server.register_function(scrapeAvtoDeloviFunc, 'scrapeAvtoDelovi')

def scrapeAvtoOglasiFunc():
    rendered = scrapeAvtooglasi()
    return rendered
server.register_function(scrapeAvtoOglasiFunc, 'scrapeAvtoOglasi')

def scrapeKoliFunc():
    rendered = scrapeKoli()
    return rendered
server.register_function(scrapeKoliFunc, 'scrapeKoli')

def scrapeBaramDomFunc():
    rendered = scrapeBaramDom()
    return rendered
server.register_function(scrapeBaramDomFunc, 'scrapeBaramDom')

def scrapeHaloOglasiFunc():
    rendered = scrapeHaloOglasi()
    return rendered
server.register_function(scrapeHaloOglasiFunc, 'scrapeHaloOglasi')

def scrapeKupujemProdajemFunc():
    rendered = scrapeKupujemProdajem()
    return rendered
server.register_function(scrapeKupujemProdajemFunc, 'scrapeKupujemProdajem')

def scrapeMobile24Func():
    rendered = scrapeMobile24()
    return rendered
server.register_function(scrapeMobile24Func, 'scrapeMobile24')

def scrapeMobileBgFunc():
    rendered = scrapeMobileBg()
    return rendered
server.register_function(scrapeMobileBgFunc, 'scrapeMobileBg')

def scrapeNadjiDomFunc():
    rendered = scrapeNadjiDom()
    return rendered
server.register_function(scrapeNadjiDomFunc, 'scrapeNadjiDom')

def scrapeNedviznostiMakedonijaFunc():
    rendered = scrapeNedviznostiMakedonija()
    return rendered
server.register_function(scrapeNedviznostiMakedonijaFunc, 'scrapeNedviznostiMakedonija')

def scrapeOglasiRsFunc():
    rendered = scrapeOglasiRs()
    return rendered
server.register_function(scrapeOglasiRsFunc, 'scrapeOglasiRs')

def scrapePobarajOglasiFunc():
    rendered = scrapePobarajOglasi()
    return rendered
server.register_function(scrapePobarajOglasiFunc, 'scrapePobarajOglasi')

def scrapeVipMarket5Func():
    rendered = scrapeVipMarket5()
    return rendered
server.register_function(scrapeVipMarket5Func, 'scrapeVipMarket5')

# Run the server's main loop
server.serve_forever()
