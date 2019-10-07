#!/usr/bin/python

import os
import cgitb
cgitb.enable()

#Poni�sza lista zawiera zmienne �rodowiskowe zdefiniowane przez standard CGI.
#Poza tymi 17 predefiniowanymi zmiennymi ka�dy nag��wek ��dania HTTP
#otrzymuje w�asn� zmienn� �rodowiskow� z przedrostkiem "HTTP_".
#Na przyk�ad nag��wek "User-Agent" zostaje umieszczony w "HTTP_USER_AGENT".
CGI_ENVIRONMENT_KEYS = [ 'SERVER_SOFTWARE',
                         'SERVER_NAME',
                         'GATEWAY_INTERFACE',
                         'SERVER_PROTOCOL',
                         'SERVER_PORT',
                         'REQUEST_METHOD',
                         'PATH_INFO',
                         'PATH_TRANSLATED',
                         'SCRIPT_NAME',
                         'QUERY_STRING',
                         'REMOTE_HOST',
                         'REMOTE_ADDR',
                         'AUTH_TYPE',
                         'REMOTE_USER',
                         'REMOTE_IDENT',
                         'CONTENT_TYPE',
                         'CONTENT_LENGTH' ]

#Najpierw wy�wietl nag��wki odpowiedzi. Potrzebujemy tylko Content-type.
print "Content-type: text/plain\n"

#Wy�wietl nazwy zmiennych �rodowiskowych i ich warto�ci.
print "Oto nag��wki z w�asnie wykonanego ��dania HTTP:"
for key, value in os.environ.items():
    if key.find('HTTP_') == 0 or key in CGI_ENVIRONMENT_KEYS:
        print key, "=>", value
