import SOAPpy
bittywiki = SOAPpy.SOAPProxy("http://localhost:8002/", "urn:BittyWiki")
bittywiki.getPage("UtworzonoPrzezSOAP")
bittywiki.save("UtworzonoPrzezSOAP", "Ta strona zostala utworzona przy uzyciu SOAP.")
bittywiki.getPage("UtworzonoPrzezSOAP")
 
