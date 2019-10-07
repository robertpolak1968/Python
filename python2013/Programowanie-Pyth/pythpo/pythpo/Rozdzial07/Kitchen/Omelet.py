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
