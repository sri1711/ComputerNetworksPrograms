from xmlrpc.client import ServerProxy

proxy = ServerProxy("http://localhost:8000/")

print('ADD : ',proxy.a(1,2))
print('SUB : ',proxy.s(2,1))
print('MUL : ',proxy.m(1,2))
print('MOD : ',proxy.mo(1,2))
print('DIV : ',proxy.d(2,2))

