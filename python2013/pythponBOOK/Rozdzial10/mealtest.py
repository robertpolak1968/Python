import Meal

print 'Tworz� obiekt Breakfast'
breakfast = Meal.makeBreakfast()

breakfast.printIt("\t")

print 'Tworz� obiekt Lunch'
lunch = Meal.makeLunch()

try:
    lunch.setFood('ciasteczka')
except Meal.AngryChefException:
    print "\t",'Nie mo�na je�� ciasteczek na lunch.'
    print "\t",'Szef jest z�y. Wybierz omlet.'
