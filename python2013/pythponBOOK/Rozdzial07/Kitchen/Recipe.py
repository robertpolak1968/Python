class Recipe:
    """
    Klasa zawiera przepisy na omlet.
    """
    
    def __init__(self):
        self.set_default_recipes()
        return
    
    def set_default_recipes(self):
        self.recipes = {"serowy" : {"jajko":2, "mleko":1, "ser":1},
                        "grzybowy" : {"jajko":2, "mleko":1, "ser":1, "grzyb":2},
                        "cebulowy" : {"jajko":2, "mleko":1, "ser":1, "cebula":1}}
    
    def get(self, name):
        """
        get(name) - zwraca s³ownik ze sk³adnikami potrzebnymi do wykonania
        omletu o podanej nazwie.
        Gdy podano nieznany rodzaj omletu, zwraca False.
        """
        try:
            recipe = self.recipes[name]
            return recipe
        except KeyError:
            return False
    
    def create(self, name, ingredients):
        """
        create(name, ingredients) - dodaje omlet o nazwie name ze sk³¹dnikami
        ingredients do s³ownika przepisów.
        """
        
        self.recipes[name] = ingredients
    
if __name__ == '__main__':
    r = Recipe()
    if r.recipes != {"serowy" : {"jajko":2, "mleko":1, "ser":1},
                        "grzybowy" : {"jajko":2, "mleko":1, "ser":1, "grzyb":2},
                        "cebulowy" : {"jajko":2, "mleko":1, "ser":1, "cebula":1}}:
        print "B³¹d: domyœlna lista przepisów nie jest poprawna"
    cheese_omelette = r.get("serowy")
    if cheese_omelette != {"jajko":2, "mleko":1, "ser":1}:
        print "B³¹d: sk³adniki omletu serowego nie s¹ poprawne"
    western_ingredients = {"jajko":2, "mleko":1, "ser":1, "szynka":1, "pieprz":1, "cebula":1}
    r.create("zachodni", western_ingredients)
    if r.get("zachodni") != western_ingredients:
        print "Nieudane ustawienie sk³adników omletu zachodniego"

