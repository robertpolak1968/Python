"""
Modu� tworz�cy potrawy w Pythonie.

Zaimportuj modu� a nast�pnie wywo�aj
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
    
# Klasy wyj�tk�w.

class SensitiveArtistException(Exception): 
    '''Wyj�tek dotycz�cy przewra�liwionych artyst�w.
    
    Klasa bazowa dla typ�w artystycznych.'''
    pass


class AngryChefException(SensitiveArtistException): 
    '''Wyj�tek wskazuj�cy szefa w z�ym humorze.'''
    pass

    
    
    
class Meal:
    '''Przechowuje jedzenie i picie sk�adaj�ce si� na posi�ek.
    Zgodnie z zasadami obiektowo�ci, klasa stosuje metody
    ustawiaj�ce dla jedzenia i picia.
    
    Wywo�aj printIt, aby �adnie wy�wietli� warto�ci.
    '''

    def __init__(self, food='omlet', drink='kawa'):
        '''Inicjalizacja na warto�ci domy�lne.'''
        self.name = 'posi�ek'
        self.food = food
        self.drink = drink
    
    def printIt(self, prefix=''):
        '''�adne wy�wietlenie danych.'''
        print prefix,'Smaczny',self.name,'czyli',self.food,'i',self.drink
          
    # Metoda ustawiaj�ca dla jedzenia.
    def setFood(self, food='omlet'):
        self.food = food
    
    # Metoda ustawiaj�ca dla picia.    
    def setDrink(self, drink='kawa'):
        self.drink = drink
        
    # Metoda ustawiaj�ca dla nazwy.
    def setName(self, name=''):
        self.name = name
        

class Breakfast(Meal):
    '''Jedzenie i picie zwi�zane ze �niadaniem.'''
        
    def __init__(self):
        '''Inicjalizuj omletem i kaw�.'''
        Meal.__init__(self, 'omlet', 'kawa')
        self.setName('�niadanie')
        
class Lunch(Meal):
    '''Jedzenie i picie zwi�zane z lunchem.'''
        
    def __init__(self):
        '''Inicjalizuj kanapk� i d�inem z tonikiem.'''
        Meal.__init__(self, 'kanapka', 'd�in z tonikiem')
        self.setName('lunch')

    # Przes�ania setFood().
    def setFood(self, food='kanapka'):
        if food != 'kanapka' and food != 'omlet':
            raise AngryChefException
        Meal.setFood(self, food)
        
class Dinner(Meal):
    '''Jedzenie i picie zwi�zane z obiadem.'''
        
    def __init__(self):
        '''Inicjalizuj stekiem i winem.'''
        Meal.__init__(self, 'stek', 'wino')
        self.setName('obiad')

    def printIt(self, prefix=''):
        '''Wy�wietl opis w jeszcze przyjemniejszy spos�b.'''
        print prefix,'Przepyszny',self.name,'czyli',self.food,'i',self.drink       
 
        
def test():
    '''Funkcja testuj�ca.'''
    
    print 'Testowanie modu�u Meal.'
    
    # Brak argument�w.
    print 'Testowanie klasy Meal.'
    m = Meal()
    
    m.printIt("\t")
    
    
    m = Meal('jajka i szynka', 'herbata')
    m.printIt("\t")
    
    # Testowanie �niadania.
    print 'Testowanie klasy Breakfast.'
    b = Breakfast()
    b.printIt("\t")
    
    b.setName('drugie �niadanie')
    b.printIt("\t")
    
    
    # Testowanie obiadu.
    print 'Testowanie klasy Dinner.'
    d = Dinner()
    d.printIt("\t")
    
    
    # Testowanie lunchu.
    print 'Testowanie klasy Lunch.'
    l = Lunch()
    l.printIt("\t")
    
    print 'Wywo�anie Lunch.setFood().'
    try:
        l.setFood('hotdog')
    except AngryChefException:
        print "\t",'Szef jest z�y. We� omlet.'

# Uruchom testy, je�li modu� zostanie uruchomiony jako program.        
if __name__ == '__main__':
    test()
