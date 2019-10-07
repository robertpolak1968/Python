from Meal import *

print 'Tworzê obiekt Breakfast'
breakfast = makeBreakfast()

breakfast.printIt("\t")

print 'Tworzê obiekt Lunch'
lunch = makeLunch()

try:
    lunch.setFood('ciasteczka')
except AngryChefException:
    print "\t",'Nie mo¿na jeœæ ciasteczek na lunch.'
    print "\t",'Szef jest z³y. Wybierz omlet.'
