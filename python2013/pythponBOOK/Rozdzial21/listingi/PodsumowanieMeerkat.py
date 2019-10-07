import xmlrpclib

class MeerkatSummary:
    """Wymienia kana³y pasuj±ce do zadenego kryterium w kolejno¶ci malej±cej
    na podstawie liczby pasuj±cych historii."""

    SERVER_URL = 'http://www.oreillynet.com/meerkat/xml-rpc/server.php'

    def __init__(self):
        "Utworzenie referencji do serwera Meerkat."

        #Przekazanie 'verbose=True' do konstruktora serwera spowoduje
        #wy¶wietlanie tekstu odpowiedzi i ¿±dania dla ka¿ego wywo³ania XML-RPC,
        #co pozwala ³atwo poznaæ szczegó³y dzia³ania protoko³u.
        #verbose = True

        verbose = False
        server = xmlrpclib.ServerProxy(self.SERVER_URL, verbose=verbose)
        self.meerkat = server.meerkat

    def findChannels(self, searchTerm):
        "Sprawd¼, które kana³y maj± najwiêcej wpisów na zadany temat."
        channelTotals = {}
        items = self.meerkat.getItems({'search' : searchTerm,
                                       'channels' : True})
        for item in items:
            channel = item['channel']
            totalForChannel = channelTotals.get(channel, 0)
            totalForChannel += 1
            channelTotals[channel] = totalForChannel
        totalAndChannel = [(a,b) for b,a in channelTotals.items()]
        totalAndChannel.sort()
        totalAndChannel.reverse()
        print 'Raport Meerkat dla "%s":' % searchTerm
        for total, channel in totalAndChannel:
            print "%2d %s" % (total, channel)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print "U¿ycie: %s [szukany termin]" % sys.argv[0]
        sys.exit(1)
    else:
        MeerkatSummary().findChannels(sys.argv[1])
