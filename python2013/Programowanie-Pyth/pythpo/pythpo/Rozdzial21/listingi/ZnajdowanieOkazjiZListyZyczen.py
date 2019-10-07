import copy
import re
import amazon

class BargainFinder:
    """Klasa, kt�ra dla podanej listy produkt�w Amazon znajduje te,
    kt�re spe�aniaj� wymogi znacz�cej okazji."""

    def __init__(self, bargainCoefficient=.25, bargainCutoff=3.00):
        """Zmienna bargainCoefficient okre�la, jak ma�o musi kosztowa�
        u�ywany prokdukt w por�wnaniu z nowym, nby uzna� go za okazj�.
        Domy�lny wsp�czynnik wynosi .25, co oznacza, �e cena u�ywanego
        produktu musi by� co najmniej czterokrotnie mniejsza od ceny 
        nowego produktu w Amazon.

        Zmienna bargainCutoff znajduje tanie okazje. 
        Domy�lna warto�� bargainCutoff wynosi 3, wi�c element uznawany
        za okazyjny musi kosztowa� mniej ni� $3.00, nawet je�li istnieje
        nowy produkt o cenie tylko nieco wy�szej ni� $3.00."""
        if bargainCoefficient >= 1:
            raise Exception, 'Nie ma sensu poszukiwa� okazji kosztuj�cych ' \
            + 'wi�cej ni� nowe produkty!'
        self.coefficient = bargainCoefficient
        self.cutoff = bargainCutoff
        
    def printBargains(self, items):
        """Znajd� okazj� wewn�trz listy i wy�wietl j� w postaci listy na 
        ekranie."""
        bargains = self.getBargains(items)
        printedHeader = 0
        if bargains:
            print ('Oto u�ywane produkty dost�pne za mniej ni� $%.2f ' + \
                  'lub za mniej ni� %.2d%% ceny nowego produktu:') \
                  % (self.cutoff, self.coefficient*100)
            prices = bargains.keys()
            prices.sort()
            for usedPrice in prices:
                for bargain, amazonPrice in bargains[usedPrice]:
                    savings = ''
                    if amazonPrice:
                        percentageSavings = (1-(usedPrice/amazonPrice)) * 100
                        savings = '(Oszcz�dzasz %.2d%% z ceny $%.2f) ' \
                                  % (percentageSavings, amazonPrice)
                    print ' $%.2f %s%s' % (usedPrice, savings,
                                           bargain.ProductName)
        else:
            print "Niestety nie znaleziono �adnych okazji."

    def getBargains(self, items):
        "Przeszukaj list� w poszukiwaniu okazji."
        bargains = {}
        for item in items:
            bargain = False
            amazonPrice = self.getPrice(item, "OurPrice")
            usedPrice = self.getPrice(item, "UsedPrice")
            if usedPrice:
                if usedPrice < self.cutoff:
                    bargain = True
                if amazonPrice:
                    if (amazonPrice * self.coefficient) > usedPrice:
                        bargain = True
            if bargain:
                #Sortujemy okazje na podstawie ich ceny, by najta�szy
                #element pojawi� si� jako pierwszy.
                bargainsForPrice = bargains.get(usedPrice, None)
                if not bargainsForPrice:
                    bargainsForPrice = []
                    bargains[usedPrice] = bargainsForPrice
                bargainsForPrice.append((item, amazonPrice))
        return bargains

    def getPrice(self, item, priceField):
        """Pobiera nazwane pole z cen� (np. "OurPrice",
        "UsedPrice") i pr�buje zamieni� warto�� tekstow� ceny na liczb�."""
        price = getattr(item, priceField, None)
        if price:
            price = self._parseCurrency(price)
        return price
    
    def _parseCurrency(self, currency):
        """Prosty spos�b zamiany kwoty walutowej zapisanej jako tekst na 
        warto�� zmiennoprzecinkow�: usuwamy wszystko poza liczbami, znakiem
        kropki i znakiem minusa."""
        return float(self.IRRELEVANT_CURRENCY_CHARACTERS.sub('', currency))
    IRRELEVANT_CURRENCY_CHARACTERS = re.compile("[^0-9.-]")

from OnDemandAmazonList import OnDemandAmazonList
def getWishList(subscriptionID, wishListID):
    "Zwraca iteracyjn� wersj� listy �ycze�."
    kwds = {'license_key' : subscriptionID,
            'wishlistID' : wishListID,
            'type' : 'lite'}
    return OnDemandAmazonList(amazon.searchByWishlist, kwds)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print 'U�ycie: %s [ID subskrypcji] [ID listy �ycze�]' % sys.argv[0]
        sys.exit(1)
    subscriptionID, wishListID = sys.argv[1:]
    wishList = getWishList(subscriptionID, wishListID)
    BargainFinder().printBargains(wishList)
