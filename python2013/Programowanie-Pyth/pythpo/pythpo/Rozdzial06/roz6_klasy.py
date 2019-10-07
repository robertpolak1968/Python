#!/usr/bin/python


class Fridge:
    """Klasa implementuje lod�wk�, do kt�rej mo�na wstawia� lub 
    pobiera� produkty pojedynczo lub w grupach.  
    Lod�wka przewchowuje informacj� o liczbie sztuk ka�dego produktu.
    Zg�osi wyj�tek, je�li b�dzie pr�bowa�o si� pobra� wi�cej sztuk produktu 
    ni� znajduje si� w lod�wce.
    Metody:
    has(food_name [, quantity]) - sprawdza, czy produkt food_name znajduje si� w lod�wce.  Parametr quantity zostanie ustawiony na 1, je�li si� go nie przeka�e.
    has_various(foods) - sprawdza, czy w lod�wce znajduj� si� produkty ze s�ownika w odpowiedniej liczbie sztuk.
    add_one(food_name) - dodaje do lod�wki pojedynczy produkt o nazwie food_name
    add_many(food_dict) - dodaje do lod�wki ca�y s�ownik produkt�w
    get_one(food_name) - pobiera z lod�wki pojedynczy produkt o nazwie food_name
    get_many(food_dict) - pobiera z lod�wki ca�y s�ownik produkt�w
    get_ingredients(food) - je�li przeka�e si� obiekt zawieraj�cy metod� __ingredients__ 
            zostanie u�yta metoda get_many, by przetworzy� list� sk�adnik�w
    """
    
    def __init__(self, items={}):
        """Opcjonalny parametr przyjmuje s�ownik produkt�w"""
        if type(items) != type({}):
            raise TypeError, "Obiekt wymaga s�ownika, ale przekazano %s" % type(items)
        self.items = items
        return

    def __add_multi(self, food_name, quantity):
        """
        __add_multi(food_name, quantity) - dodaje kilka sztuk jednego produktu 
        do listy produkt�w w lod�wce.
        
        Metod� nale�y stosowa� tylko wewn�trznie po dokonaniu sprawdzania typ�w.
        """
        if not self.items.has_key(food_name):
            self.items[food_name] = 0
            
        self.items[food_name] = self.items[food_name] + quantity

    def add_one(self, food_name):
        """
        add_one(food_name) - dodaje do lod�wki pojedynczy produkt o nazwie food_name
        Zwraca True.
        Zg�asza wyj�tek TypeError, je�li food_name nie jest ci�giem znak�w.
        """
        if type(food_name) != type(""):
            raise TypeError, "add_one wymaga ci�gu znak�w, podano %s" % type(food_name)
        else:
            self.__add_multi(food_name, 1)
        
        return True
        
    def add_many(self, food_dict):
        """
        add_many(food_dict) - dodaje ca�y s�ownik, w kt�rym kluczami s� nazwy
            produkt�w a warto�ciami liczby sztuk
        Metoda nic nie zwraca.
        Zg�asza wyj�tek TypeError, je�li food_dict nie jest s�ownikiem
        """
        
        if type(food_dict) != type({}):
            raise TypeError, "add_many wymaga s�ownika, podano %s" % food_dict
        
        for item in food_dict.keys():
            self.__add_multi(item, food_dict[item])
        return

    def has(self, food_name, quantity=1):
        """
        has(food_name, [quantity]) - sprawdza, czy produkt food_name znajduje si� w lod�wce.  Parametr quantity przyjmuje domy�lnie warto�� 1.
        Zwraca True, je�li sztuk produktu jest wystarczaj�co du�o; w przeciwnym razie zwraca False.
        """
        
        return self.has_various({food_name:quantity})
        
    def has_various(self, foods):
        """
        has_various(foods) - sprawdza, czy lod�wka zawiera wystarczaj�co du�o sztuk
            produkt�w wymienionych w s�owniku foods.
        Zwraca True, je�li sztuk wszystkich produkt�w jest wystarczaj�co du�o;
        zwraca False, je�li cho� jednego produktu jest za ma�o lub w og�le nie wyst�puje.
        """
        
        try:
            for food in foods.keys():
                if self.items[food] < foods[food]:
                    return False
            return True
        except KeyError:
            return False
   
    def __get_multi(self, food_name, quantity):
        """
        __get_multi(food_name, quantity) - usuwa wi�cej ni� jedn� sztuk�
        produktu. Zwraca liczb� usuni�tych sztuk.
        Zwraca False, je�li nie by�o w lod�wce wystarczaj�co du�o sztuk
        produktu food_name.
        Metoda przewidziana jest tylko do u�ytku wewn�trznego ju� po
        przeprowadzeniu sprawdzania typ�w.
        """
        
        try:
            if not self.has(food_name, quantity):
                return False
            self.items[food_name] = self.items[food_name] - quantity
        except KeyError:
            return False
        return quantity

    def get_one(self, food_name):
        """
        get_one(food_name) - pobiera z lod�wki sztuk� produktu food_name.
        Zwraca liczb� sztuk produktu.
        Zwraca False, je�li produktu nie ma w lod�wce.
        """

        if type(food_name) != type(""):
            raise TypeError, "get_one wymaga ci�gu znak�w, przekazano %s" % type(food_name)
        else:
            result = self.__get_multi(food_name, 1)
        return result

    def get_many(self, food_dict):
        """
        get_many(food_dict) - pobiera z lod�wki produktu wskazane w s�owniku
        Zwraca s�ownik ze wszystkimi sk�adnikami.
        Nic nie zwraca, je�li nie ma wystarczaj�co du�o sztuk produkt�w w lod�wce  
        lub nie przekazano s�ownika.
        """
        
        if self.has_various(food_dict):
            foods_removed = {}
            for item in food_dict.keys():
                foods_removed[item] = self.__get_multi(item, food_dict[item])
            return foods_removed
        
    def get_ingredients(self, food):
        """
        get_ingredients(food) - je�li przekazano obiekt zawieraj�cy metod� __ingredients__ 
            zostanie wywo�ana metoda get_many z list� sk�adnik�w.
        """
        try:
            ingredients = self.get_many(food.__ingredients__())
        except AttributeError:
            return False
        
        if ingredients != False:
            return ingredients
   

class Omelet:
    """Klasa reprezentuje omlet. Omlet mo�e znajdowa� si� w jednym
    z dw�ch stan�w: przygotowanych sk�adnik�w i wykonanym.
    Interfejs definiowany przez klas�:
    get_kind() - zwraca ci�g znak�w z nazw� rodzaju omletu
    set_kind(kind) - ustawia rodzaj omletu
    set_new_kind(kind, ingredients) - tworzy omlet
    mix() - wywo�ywana po pobraniu wszystkich sk�adnik�w z lod�wki
    cook() - przygotowuje omlet ze sk�adnik�w
    """
    def __init__(self, kind="serowy"):
        """__init__(self, kind="serowy")
        Inicjalizuje klas� Omelet.
        Domy�lnie przyjmuje tworzenie omletu serowego.
        """
        self.set_kind(kind)
        return


    def __ingredients__(self):
        """Metoda wewn�trzna wywo�ywana przez lod�wk� lub inny kod 
        wymagaj�cy dost�pu do sk�adnik�w omletu.
        """
        return self.needed_ingredients
        
    def get_kind(self):
        return self.kind
    
    def set_kind(self, kind):
        possible_ingredients = self.__known_kinds(kind)
        if possible_ingredients == False:
            return False
        else:
            self.kind = kind
            self.needed_ingredients = possible_ingredients
        
    def set_new_kind(self, name, ingredients):
        self.kind = name
        self.needed_ingredients = ingredients
        return

    def __known_kinds(self, kind):
        if kind == "serowy":
            return {"jajko":2, "mleko":1, "ser":1}
        elif kind == "grzybowy":
            return {"jajko":2, "mleko":1, "ser":1, "grzyb":2}
        elif kind == "cebulowy":
            return {"jajko":2, "mleko":1, "ser":1, "cebula":1}
        else:
            return False

    def get_ingredients(self, fridge):
        self.from_fridge = fridge.get_ingredients(self)
        
    def mix(self):
        for ingredient in self.from_fridge.keys():
            print "Mieszanie %d %s, by powsta� omlet %s" % (self.from_fridge[ingredient], ingredient, self.kind)
        self.mixed = True

    def make(self):
        if self.mixed == True:
            print "Przygotowanie omletu %s!" % self.kind
            self.cooked = True

