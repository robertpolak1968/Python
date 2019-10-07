import xmlrpclib
server = xmlrpclib.ServerProxy("http://localhost:8001/")
#Ewentualnie użyj następującego wywołania:
#server = xmlrpclib.ServerProxy("http://localhost/cgi-bin/bittywiki-xmlrpc.cgi")
bittywiki = server.bittywiki
#bittywiki.getPage("UtworzoneWXMLRPC")
bittywiki.save("UtworzoneWXMLRPC", "Ta strona zostala utworzona przy uzyciu XML-RPC.")
bittywiki.getPage("UtworzoneWXMLRPC")
