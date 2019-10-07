import math
from threading import Thread
import time

class SquareRootCalculator:

    """Klasa wykorzystuje osobny w�tek do policzenia wielu pierwiast�w kwadratowych.
    Co sekund� sprawdza, czy zadanie zosta�o wykonane."""

    def __init__(self, target):
        """W��cza w�tek kalkulatora a nast�pnie co pewnien czas
        sprawdza post�py prac."""
        self.results = []
        counter = self.CalculatorThread(self, target)
        print "W��czam w�tek kalkulatora..."
        counter.start()
        while len(self.results) < target:
            print "%d pierwiast�w kwadratowych policzono do tej pory." % len(self.results)
            time.sleep(1)
        print "Policzono %s pierwiastk�w kwadratowych; ostatni to sqrt(%d)=%f" % \
              (target, len(self.results), self.results[-1])
              
    class CalculatorThread(Thread):
        """Osobny w�tek wykonuj�cy odpowiednie obliczenia."""

        def __init__(self, controller, target):
            """Inicjalizuje w�tek i dodatkowo tworzy go w�tkiem demona
            aby skrypt nie musia� oczekiwa� na jego zako�czenie."""
            Thread.__init__(self)
            self.controller = controller
            self.target = target
            self.setDaemon(True)

        def run(self):
            """Wylicza pierwiastki kwadratowe od 1 do zadanej warto�ci."""
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
            print "U�ycie: %s [liczba pierwiast�w kwadratowych do wyliczenia]" \
                  % sys.argv[0]    
    SquareRootCalculator(limit)
