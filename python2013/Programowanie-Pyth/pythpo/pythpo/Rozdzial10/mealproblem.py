import Meal

print 'Tworz� obiekt Breakfast'
Meal = Meal.makeBreakfast()

Meal.printIt("\t")

print 'Tworz� obiekt Lunch'
lunch = Meal.makeLunch()

try:
    lunch.setFood('ciasteczka')
except Meal.AngryChefException:
    print "\t",'Nie mo�na je�� ciasteczek na lunch.'
    print "\t",'Szef jest z�y. Wybierz omlet.'
