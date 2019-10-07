import math
from threading import Thread
import time

class SquareRootCalculator:

    """Klasa wykorzystuje osobny w¹tek do policzenia wielu pierwiastów kwadratowych.
    Co sekundê sprawdza, czy zadanie zosta³o wykonane."""

    def __init__(self, target):
        """W³¹cza w¹tek kalkulatora a nastêpnie co pewnien czas
        sprawdza postêpy prac."""
        self.results = []
        counter = self.CalculatorThread(self, target)
        print "W³¹czam w¹tek kalkulatora..."
        counter.start()
        while len(self.results) < target:
            print "%d pierwiastów kwadratowych policzono do tej pory." % len(self.results)
            time.sleep(1)
        print "Policzono %s pierwiastków kwadratowych; ostatni to sqrt(%d)=%f" % \
              (target, len(self.results), self.results[-1])
              
    class CalculatorThread(Thread):
        """Osobny w¹tek wykonuj¹cy odpowiednie obliczenia."""

        def __init__(self, controller, target):
            """Inicjalizuje w¹tek i dodatkowo tworzy go w¹tkiem demona
            aby skrypt nie musia³ oczekiwaæ na jego zakoñczenie."""
            Thread.__init__(self)
            self.controller = controller
            self.target = target
            self.setDaemon(True)

        def run(self):
            """Wylicza pierwiastki kwadratowe od 1 do zadanej wartoœci."""
            for i in range(1, self.target+1):
                self.controller.results.append(math.sqrt(i))

if __name__ == '__main__':
    import sys
    limit = None
    if len(sys.argv) > 1:
        limit = sys.argv[1]
        try:
            limit = int(limit)
        except ValueError:
            print "U¿ycie: %s [liczba pierwiastów kwadratowych do wyliczenia]" \
                  % sys.argv[0]    
    SquareRootCalculator(limit)
