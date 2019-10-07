"""
Modu³ tworz¹cy potrawy w Pythonie.

Zaimportuj modu³ a nastêpnie wywo³aj
makeBreakfast(), makeDinner() lub makeLunch().

"""


__all__ = ['Meal','AngryChefException', 'makeBreakfast', 
    'makeLunch', 'makeDinner', 'Breakfast', 'Lunch', 'Dinner']


# Funkcje pomocnicze.

def makeBreakfast():
    '''Tworzy obiekt Breakfast.'''
    return Breakfast()
    
def makeLunch():
    '''Tworzy obiekt Lunch.'''
    return Lunch()

def makeDinner():
    '''Tworzy obiekt Dinner.'''
    return Dinner()
    
# Klasy wyj¹tków.

class SensitiveArtistException(Exception): 
    '''Wyj¹tek dotycz¹cy przewra¿liwionych artystów.
    
    Klasa bazowa dla typów artystycznych.'''
    pass


class AngryChefException(SensitiveArtistException): 
    '''Wyj¹tek wskazuj¹cy szefa w z³ym humorze.'''
    pass

    
    
    
class Meal:
    '''Przechowuje jedzenie i picie sk³adaj¹ce siê na posi³ek.
    Zgodnie z zasadami obiektowoœci, klasa stosuje metody
    ustawiaj¹ce dla jedzenia i picia.
    
    Wywo³aj printIt, aby ³adnie wyœwietliæ wartoœci.
    '''

    def __init__(self, food='omlet', drink='kawa'):
        '''Inicjalizacja na wartoœci domyœlne.'''
        self.name = 'posi³ek'
        self.food = food
        self.drink = drink
    
    def printIt(self, prefix=''):
        '''£adne wyœwietlenie danych.'''
        print prefix,'Smaczny',self.name,'czyli',self.food,'i',self.drink
          
    # Metoda ustawiaj¹ca dla jedzenia.
    def setFood(self, food='omlet'):
        self.food = food
    
    # Metoda ustawiaj¹ca dla picia.    
    def setDrink(self, drink='kawa'):
        self.drink = drink
        
    # Metoda ustawiaj¹ca dla nazwy.
    def setName(self, name=''):
        self.name = name
        

class Breakfast(Meal):
    '''Jedzenie i picie zwi¹zane ze œniadaniem.'''
        
    def __init__(self):
        '''Inicjalizuj omletem i kaw¹.'''
        Meal.__init__(self, 'omlet', 'kawa')
        self.setName('œniadanie')
        
class Lunch(Meal):
    '''Jedzenie i picie zwi¹zane z lunchem.'''
        
    def __init__(self):
        '''Inicjalizuj kanapk¹ i d¿inem z tonikiem.'''
        Meal.__init__(self, 'kanapka', 'd¿in z tonikiem')
        self.setName('lunch')

    # Przes³ania setFood().
    def setFood(self, food='kanapka'):
        if food != 'kanapka' and food != 'omlet':
            raise AngryChefException
        Meal.setFood(self, food)
        
class Dinner(Meal):
    '''Jedzenie i picie zwi¹zane z obiadem.'''
        
    def __init__(self):
        '''Inicjalizuj stekiem i winem.'''
        Meal.__init__(self, 'stek', 'wino')
        self.setName('obiad')

    def printIt(self, prefix=''):
        '''Wyœwietl opis w jeszcze przyjemniejszy sposób.'''
        print prefix,'Przepyszny',self.name,'czyli',self.food,'i',self.drink       
 
        
def test():
    '''Funkcja testuj¹ca.'''
    
    print 'Testowanie modu³u Meal.'
    
    # Brak argumentów.
    print 'Testowanie klasy Meal.'
    m = Meal()
    
    m.printIt("\t")
    
    
    m = Meal('jajka i szynka', 'herbata')
    m.printIt("\t")
    
    # Testowanie œniadania.
    print 'Testowanie klasy Breakfast.'
    b = Breakfast()
    b.printIt("\t")
    
    b.setName('drugie œniadanie')
    b.printIt("\t")
    
    
    # Testowanie obiadu.
    print 'Testowanie klasy Dinner.'
    d = Dinner()
    d.printIt("\t")
    
    
    # Testowanie lunchu.
    print 'Testowanie klasy Lunch.'
    l = Lunch()
    l.printIt("\t")
    
    print 'Wywo³anie Lunch.setFood().'
    try:
        l.setFood('hotdog')
    except AngryChefException:
        print "\t",'Szef jest z³y. WeŸ omlet.'

# Uruchom testy, jeœli modu³ zostanie uruchomiony jako program.        
if __name__ == '__main__':
    test()
