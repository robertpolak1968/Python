#!/usr/bin/python


# Funkcja in_fridge przechodzi w rozdziale kilka modyfikacji.
# Gdy plik zostanie wczytany do interpretera Pythona
# u�ywana b�dzie jedynie ostatnia jej wersja.

# Pierwsza
def in_fridge():
    try:
        count = fridge[wanted_food]
    except KeyError:
        count = 0
    return count

# Druga, przedstawia spos�b tworzenia dokumentacji
def in_fridge ():
    """Funkcja sprawdza, czy w lodw�ce znajduje si� dany produkt.
S�ownik fridge musi zosta� zdefiniowany poza funkcj�.
Nazw� poszukiwanego produktu nale�y umie�ci� w zmiennej wanted_food."""
    try: 
        count = fridge[wanted_food] 
    except KeyError:
        count = 0
    return count

# Trzecia
def in_fridge(some_fridge, desired_item):
    """Funkcja sprawdza, czy w lodw�ce znajduje si� dany produkt.
Pierwszy parametr jest s�ownikiem.
Drugi parametr okre�la poszukiwany w lodw�ce produkt."""
    try:
        count = some_fridge[desired_item]
    except KeyError:
        count = 0
    return count


# To jest pierwsza wersja funkcji make_omelette. Podobnie, jak w przypadku
# pozosta�ych funkcji, u�ywana jest jedynie ostatnia jej wersja, je�li
# ca�y skrypt uruchomi si� w interpreterze Pythona. Sprawd� dzia�anie
# poszczeg�lnych wersji funkcji, czytaj�c rozdzia� ksi��ki. 
# W tym celu skopiuj i wklej kod danej funkcji do interpretera lub
# osobnego pliku.

def make_omelet(omelet_type):
    """Przygotowuje omlet.  Mo�na przekaza� albo s�ownik
    zawieraj�cy sk�adniki wymagane do wykonania omletu lub te�
    wskaza� rodzaj ompletu do wykonania, kt�ry funkcja ju� zna."""
    if type(omelet_type) == type({}):
        print "omelet_type to s�ownik ze sk�adnikami"
        return make_food(omelet_type, "specalny")
    elif type(omelet_type) == type(""):
        omelet_ingredients = get_omelet_ingredients(omelet_type)
        return make_food(omelet_ingredients, omelet_type)
    else:
        print "Nie wiem, czy potrafi� tworzy� taki omlet: %s" % omelet_type

# Oto funkcje pomocnicze dla funkcji make_omelet.

def get_omelet_ingredients(omelet_name):
    """Tworzy s�owniki zawieraj�ce nazwy sk�adnik�w r�nych typ�w omlet�w,
a tak�e ich ilo�ci"""
    # Wszystkie omlety wymagaj� jajka i mleka
    ingredients = {"jajko":2, "mleko":1}
    if omelet_name == "serowy":
        ingredients["cheddar"] = 2
    elif omelet_name == "zachodni":
        ingredients["ser_jack"] = 2
        ingredients["szynka"]         = 1
        ingredients["pieprz"]      = 1
        ingredients["cebula"]       = 1
    elif omelet_Name == "grecki":
        ingredients["ser_feta"] = 2
        ingredients["szpinak"]     = 2
    else:
        print "Niestety tego nie ma w menu!"
        return None
    return ingredients

def make_food(ingredients_needed, food_name):
    """make_food(ingredients_needed, food_name)
    Pobiera sk�adniki z ingredients_needed, wypisuje je i zwraca nazw� potrawy"""
    for ingredient in ingredients_needed.keys():
        print "Dodaj� %d %s, aby wykona� omlet %s" % (ingredients_needed[ingredient], ingredient, food_name)
    print "Wykonano omlet %s" % food_name
    return food_name

# Ta implementacja funkcji make_omelet przedstawia tworzenie jednych
# funkcji wewn�trz innych, by w ten spos�b make_omelet uczy� bardziej
# zwart� i niezale�n�.

def make_omelet(omelet_type):
    """Przygotowuje omlet.  Mo�na przekaza� albo s�ownik
    zawieraj�cy sk�adniki wymagane do wykonania omletu lub te�
    wskaza� rodzaj ompletu do wykonania, kt�ry funkcja ju� zna."""
    def get_omelet_ingredients(omelet_name):
        """Tworzy s�owniki zawieraj�ce nazwy sk�adnik�w r�nych typ�w omlet�w,
        a tak�e ich ilo�ci"""
        ingredients = {"jajko":2, "mleko":1}
        if omelet_name == "serowy":
            ingredients["cheddar"] = 2
        elif omelet_name == "zachodni":
            ingredients["ser_jack"] = 2
	# Tutaj nale�y umie�ci� pozosta�� cz�� funkcji
	# get_omelet_ingredients. Nie umie�cili�my jej tu, by zwi�kszy� 
	# czytelno�� kodu
    if type(omelet_type) == type({}):
        print "omelet_type to s�ownik ze sk�adnikami"
        return make_food(omelet_type, "specjalny")
    elif type(omelet_type) == type(""):
        omelet_ingredients = get_omelet_ingredients(omelet_type)
        return make_food(omelet_ingredients, omelet_type)
    else:
        print "Nie wiem, czy potrafi� tworzy� taki omlet: %s" % omelet_type
    
# Tak implementacja make_omelet zg�asza wyj�tek.
def make_omelet(omelet_type):
    """Przygotowuje omlet.  Mo�na przekaza� albo s�ownik
    zawieraj�cy sk�adniki wymagane do wykonania omletu lub te�
    wskaza� rodzaj ompletu do wykonania, kt�ry funkcja ju� zna."""
    def get_omelet_ingredients(omelet_name):
        """Tworzy s�owniki zawieraj�ce nazwy sk�adnik�w r�nych typ�w omlet�w,
        a tak�e ich ilo�ci"""
        ingredients = {"jajko":2, "mleko":1}
        if omelet_name == "serowy":
            ingredients["cheddar"] = 2
        elif omelet_name == "zachodni":
            ingredients["ser_jack"] = 2
	# Tutaj nale�y umie�ci� pozosta�� cz�� funkcji
	# get_omelet_ingredients. Nie umie�cili�my jej tu, by zwi�kszy� 
	# czytelno�� kodu
    if type(omelet_type) == type({}):
        print "omelet_type to s�ownik ze sk�adnikami"
        return make_food(omelet_type, "specjalny")
    elif type(omelet_type) == type(""):
        omelet_ingredients = get_omelet_ingredients(omelet_type)
        return make_food(omelet_ingredients, omelet_type)
    else:
        raise TypeError, "Nieznany rodzaj omletu: %s" % omelet_type

