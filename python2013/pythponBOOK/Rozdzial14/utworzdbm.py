#!/usr/bin/env python

import anydbm

db = anydbm.open('witryny', 'c')

# Dodaj element.
db['www.python.org'] = 'G��wna witryna Pythona'

print db['www.python.org']

# Zamknij i zapisz na dysku.
db.close()
