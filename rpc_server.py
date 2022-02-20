from xmlrpc.server import SimpleXMLRPCServer
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b

server = SimpleXMLRPCServer(("localhost",8000))
server.register_function(add,'a')
server.register_function(sub,'s')
server.register_function(mul,'m')
server.register_function(div,'d')
server.register_function(mod,'mo')
server.serve_forever()