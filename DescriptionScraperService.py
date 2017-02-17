#!/usr/bin/env python
# coding: utf-8

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SinglePageFilterRenderer

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8001), requestHandler=RequestHandler)
server.register_introspection_functions()

# Register a function under a different name
def adder_function(x,y):
    return x + y
server.register_function(adder_function, 'add')

def scrapeVrapcheAdDescription(url, xpath):
    return SinglePageFilterRenderer.filterContent(url, xpath)
server.register_function(scrapeVrapcheAdDescription, 'scrapeVrapcheAdDescription')

# Run the server's main loop
server.serve_forever()