#!/usr/bin/python


class Fridge:
    """Klasa implementuje lodówkê, do której mo¿na wstawiaæ lub 
    pobieraæ produkty pojedynczo lub w grupach.  
    Lodówka przewchowuje informacjê o liczbie sztuk ka¿dego produktu.
    Zg³osi wyj¹tek, jeœli bêdzie próbowa³o siê pobraæ wiêcej sztuk produktu 
    ni¿ znajduje siê w lodówce.
    Metody:
    has(food_name [, quantity]) - sprawdza, czy produkt food_name znajduje siê w lodówce.  Parametr quantity zostanie ustawiony na 1, jeœli siê go nie przeka¿e.
    has_various(foods) - sprawdza, czy w lodówce znajduj¹ siê produkty ze s³ownika w odpowiedniej liczbie sztuk.
    add_one(food_name) - dodaje do lodówki pojedynczy produkt o nazwie food_name
    add_many(food_dict) - dodaje do lodówki ca³y s³ownik produktów
    get_one(food_name) - pobiera z lodówki pojedynczy produkt o nazwie food_name
    get_many(food_dict) - pobiera z lodówki ca³y s³ownik produktów
    get_ingredients(food) - jeœli przeka¿e siê obiekt zawieraj¹cy metodê __ingredients__ 
            zostanie u¿yta metoda get_many, by przetworzyæ listê sk³adników
    """
    
    def __init__(self, items={}):
        """Opcjonalny parametr przyjmuje s³ownik produktów"""
        if type(items) != type({}):
            raise TypeError, "Obiekt wymaga s³ownika, ale przekazano %s" % type(items)
        self.items = items
        return

    def __add_multi(self, food_name, quantity):
        """
        __add_multi(food_name, quantity) - dodaje kilka sztuk jednego produktu 
        do listy produktów w lodówce.
        
        Metodê nale¿y stosowaæ tylko wewnêtrznie po dokonaniu sprawdzania typów.
        """
        if not self.items.has_key(food_name):
            self.items[food_name] = 0
            
        self.items[food_name] = self.items[food_name] + quantity

    def add_one(self, food_name):
        """
        add_one(food_name) - dodaje do lodówki pojedynczy produkt o nazwie food_name
        Zwraca True.
        Zg³asza wyj¹tek TypeError, jeœli food_name nie jest ci¹giem znaków.
        """
        if type(food_name) != type(""):
            raise TypeError, "add_one wymaga ci¹gu znaków, podano %s" % type(food_name)
        else:
            self.__add_multi(food_name, 1)
        
        return True
        
    def add_many(self, food_dict):
        """
        add_many(food_dict) - dodaje ca³y s³ownik, w którym kluczami s¹ nazwy
            produktów a wartoœciami liczby sztuk
        Metoda nic nie zwraca.
        Zg³asza wyj¹tek TypeError, jeœli food_dict nie jest s³ownikiem
        """
        
        if type(food_dict) != type({}):
            raise TypeError, "add_many wymaga s³ownika, podano %s" % food_dict
        
        for item in food_dict.keys():
            self.__add_multi(item, food_dict[item])
        return

    def has(self, food_name, quantity=1):
        """
        has(food_name, [quantity]) - sprawdza, czy produkt food_name znajduje siê w lodówce.  Parametr quantity przyjmuje domyœlnie wartoœæ 1.
        Zwraca True, jeœli sztuk produktu jest wystarczaj¹co du¿o; w przeciwnym razie zwraca False.
        """
        
        return self.has_various({food_name:quantity})
        
    def has_various(self, foods):
        """
        has_various(foods) - sprawdza, czy lodówka zawiera wystarczaj¹co du¿o sztuk
            produktów wymienionych w s³owniku foods.
        Zwraca True, jeœli sztuk wszystkich produktów jest wystarczaj¹co du¿o;
        zwraca False, jeœli choæ jednego produktu jest za ma³o lub w ogóle nie wystêpuje.
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
        __get_multi(food_name, quantity) - usuwa wiêcej ni¿ jedn¹ sztukê
        produktu. Zwraca liczbê usuniêtych sztuk.
        Zwraca False, jeœli nie by³o w lodówce wystarczaj¹co du¿o sztuk
        produktu food_name.
        Metoda przewidziana jest tylko do u¿ytku wewnêtrznego ju¿ po
        przeprowadzeniu sprawdzania typów.
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
        get_one(food_name) - pobiera z lodówki sztukê produktu food_name.
        Zwraca liczbê sztuk produktu.
        Zwraca False, jeœli produktu nie ma w lodówce.
        """

        if type(food_name) != type(""):
            raise TypeError, "get_one wymaga ci¹gu znaków, przekazano %s" % type(food_name)
        else:
            result = self.__get_multi(food_name, 1)
        return result

    def get_many(self, food_dict):
        """
        get_many(food_dict) - pobiera z lodówki produktu wskazane w s³owniku
        Zwraca s³ownik ze wszystkimi sk³adnikami.
        Nic nie zwraca, jeœli nie ma wystarczaj¹co du¿o sztuk produktów w lodówce  
        lub nie przekazano s³ownika.
        """
        
        if self.has_various(food_dict):
            foods_removed = {}
            for item in food_dict.keys():
                foods_removed[item] = self.__get_multi(item, food_dict[item])
            return foods_removed
        
    def get_ingredients(self, food):
        """
        get_ingredients(food) - jeœli przekazano obiekt zawieraj¹cy metodê __ingredients__ 
            zostanie wywo³ana metoda get_many z list¹ sk³adników.
        """
        try:
            ingredients = self.get_many(food.__ingredients__())
        except AttributeError:
            return False
        
        if ingredients != False:
            return ingredients
   

class Omelet:
    """Klasa reprezentuje omlet. Omlet mo¿e znajdowaæ siê w jednym
    z dwóch stanów: przygotowanych sk³adników i wykonanym.
    Interfejs definiowany przez klasê:
    get_kind() - zwraca ci¹g znaków z nazw¹ rodzaju omletu
    set_kind(kind) - ustawia rodzaj omletu
    set_new_kind(kind, ingredients) - tworzy omlet
    mix() - wywo³ywana po pobraniu wszystkich sk³adników z lodówki
    cook() - przygotowuje omlet ze sk³adników
    """
    def __init__(self, kind="serowy"):
        """__init__(self, kind="serowy")
        Inicjalizuje klasê Omelet.
        Domyœlnie przyjmuje tworzenie omletu serowego.
        """
        self.set_kind(kind)
        return


    def __ingredients__(self):
        """Metoda wewnêtrzna wywo³ywana przez lodówkê lub inny kod 
        wymagaj¹cy dostêpu do sk³adników omletu.
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
            print "Mieszanie %d %s, by powsta³ omlet %s" % (self.from_fridge[ingredient], ingredient, self.kind)
        self.mixed = True

    def make(self):
        if self.mixed == True:
            print "Przygotowanie omletu %s!" % self.kind
            self.cooked = True

