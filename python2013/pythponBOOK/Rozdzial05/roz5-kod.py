#!/usr/bin/python


# Funkcja in_fridge przechodzi w rozdziale kilka modyfikacji.
# Gdy plik zostanie wczytany do interpretera Pythona
# u¿ywana bêdzie jedynie ostatnia jej wersja.

# Pierwsza
def in_fridge():
    try:
        count = fridge[wanted_food]
    except KeyError:
        count = 0
    return count

# Druga, przedstawia sposób tworzenia dokumentacji
def in_fridge ():
    """Funkcja sprawdza, czy w lodwóce znajduje siê dany produkt.
S³ownik fridge musi zostaæ zdefiniowany poza funkcj¹.
Nazwê poszukiwanego produktu nale¿y umieœciæ w zmiennej wanted_food."""
    try: 
        count = fridge[wanted_food] 
    except KeyError:
        count = 0
    return count

# Trzecia
def in_fridge(some_fridge, desired_item):
    """Funkcja sprawdza, czy w lodwóce znajduje siê dany produkt.
Pierwszy parametr jest s³ownikiem.
Drugi parametr okreœla poszukiwany w lodwóce produkt."""
    try:
        count = some_fridge[desired_item]
    except KeyError:
        count = 0
    return count


# To jest pierwsza wersja funkcji make_omelette. Podobnie, jak w przypadku
# pozosta³ych funkcji, u¿ywana jest jedynie ostatnia jej wersja, jeœli
# ca³y skrypt uruchomi siê w interpreterze Pythona. SprawdŸ dzia³anie
# poszczególnych wersji funkcji, czytaj¹c rozdzia³ ksi¹¿ki. 
# W tym celu skopiuj i wklej kod danej funkcji do interpretera lub
# osobnego pliku.

def make_omelet(omelet_type):
    """Przygotowuje omlet.  Mo¿na przekazaæ albo s³ownik
    zawieraj¹cy sk³adniki wymagane do wykonania omletu lub te¿
    wskazaæ rodzaj ompletu do wykonania, który funkcja ju¿ zna."""
    if type(omelet_type) == type({}):
        print "omelet_type to s³ownik ze sk³adnikami"
        return make_food(omelet_type, "specalny")
    elif type(omelet_type) == type(""):
        omelet_ingredients = get_omelet_ingredients(omelet_type)
        return make_food(omelet_ingredients, omelet_type)
    else:
        print "Nie wiem, czy potrafiê tworzyæ taki omlet: %s" % omelet_type

# Oto funkcje pomocnicze dla funkcji make_omelet.

def get_omelet_ingredients(omelet_name):
    """Tworzy s³owniki zawieraj¹ce nazwy sk³adników ró¿nych typów omletów,
a tak¿e ich iloœci"""
    # Wszystkie omlety wymagaj¹ jajka i mleka
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
    Pobiera sk³adniki z ingredients_needed, wypisuje je i zwraca nazwê potrawy"""
    for ingredient in ingredients_needed.keys():
        print "Dodajê %d %s, aby wykonaæ omlet %s" % (ingredients_needed[ingredient], ingredient, food_name)
    print "Wykonano omlet %s" % food_name
    return food_name

# Ta implementacja funkcji make_omelet przedstawia tworzenie jednych
# funkcji wewn¹trz innych, by w ten sposób make_omelet uczyæ bardziej
# zwart¹ i niezale¿n¹.

def make_omelet(omelet_type):
    """Przygotowuje omlet.  Mo¿na przekazaæ albo s³ownik
    zawieraj¹cy sk³adniki wymagane do wykonania omletu lub te¿
    wskazaæ rodzaj ompletu do wykonania, który funkcja ju¿ zna."""
    def get_omelet_ingredients(omelet_name):
        """Tworzy s³owniki zawieraj¹ce nazwy sk³adników ró¿nych typów omletów,
        a tak¿e ich iloœci"""
        ingredients = {"jajko":2, "mleko":1}
        if omelet_name == "serowy":
            ingredients["cheddar"] = 2
        elif omelet_name == "zachodni":
            ingredients["ser_jack"] = 2
	# Tutaj nale¿y umieœciæ pozosta³¹ czêœæ funkcji
	# get_omelet_ingredients. Nie umieœciliœmy jej tu, by zwiêkszyæ 
	# czytelnoœæ kodu
    if type(omelet_type) == type({}):
        print "omelet_type to s³ownik ze sk³adnikami"
        return make_food(omelet_type, "specjalny")
    elif type(omelet_type) == type(""):
        omelet_ingredients = get_omelet_ingredients(omelet_type)
        return make_food(omelet_ingredients, omelet_type)
    else:
        print "Nie wiem, czy potrafiê tworzyæ taki omlet: %s" % omelet_type
    
# Tak implementacja make_omelet zg³asza wyj¹tek.
def make_omelet(omelet_type):
    """Przygotowuje omlet.  Mo¿na przekazaæ albo s³ownik
    zawieraj¹cy sk³adniki wymagane do wykonania omletu lub te¿
    wskazaæ rodzaj ompletu do wykonania, który funkcja ju¿ zna."""
    def get_omelet_ingredients(omelet_name):
        """Tworzy s³owniki zawieraj¹ce nazwy sk³adników ró¿nych typów omletów,
        a tak¿e ich iloœci"""
        ingredients = {"jajko":2, "mleko":1}
        if omelet_name == "serowy":
            ingredients["cheddar"] = 2
        elif omelet_name == "zachodni":
            ingredients["ser_jack"] = 2
	# Tutaj nale¿y umieœciæ pozosta³¹ czêœæ funkcji
	# get_omelet_ingredients. Nie umieœciliœmy jej tu, by zwiêkszyæ 
	# czytelnoœæ kodu
    if type(omelet_type) == type({}):
        print "omelet_type to s³ownik ze sk³adnikami"
        return make_food(omelet_type, "specjalny")
    elif type(omelet_type) == type(""):
        omelet_ingredients = get_omelet_ingredients(omelet_type)
        return make_food(omelet_ingredients, omelet_type)
    else:
        raise TypeError, "Nieznany rodzaj omletu: %s" % omelet_type

