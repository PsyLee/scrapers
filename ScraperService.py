#!/usr/bin/env python
# coding: utf-8

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8070), requestHandler=RequestHandler)
server.register_introspection_functions()

# Register a function under a different name
def adder_function(x,y):
    return x + y
server.register_function(adder_function, 'add')

def scrapeVrapche():
    pass

# Run the server's main loop
server.serve_forever()
