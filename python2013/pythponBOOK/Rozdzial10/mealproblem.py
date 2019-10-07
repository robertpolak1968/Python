import Meal

print 'Tworzê obiekt Breakfast'
Meal = Meal.makeBreakfast()

Meal.printIt("\t")

print 'Tworzê obiekt Lunch'
lunch = Meal.makeLunch()

try:
    lunch.setFood('ciasteczka')
except Meal.AngryChefException:
    print "\t",'Nie mo¿na jeœæ ciasteczek na lunch.'
    print "\t",'Szef jest z³y. Wybierz omlet.'
