from Meal import *

print 'Tworz� obiekt Breakfast'
breakfast = makeBreakfast()

breakfast.printIt("\t")

print 'Tworz� obiekt Lunch'
lunch = makeLunch()

try:
    lunch.setFood('ciasteczka')
except AngryChefException:
    print "\t",'Nie mo�na je�� ciasteczek na lunch.'
    print "\t",'Szef jest z�y. Wybierz omlet.'
