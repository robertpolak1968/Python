import os, os.path
import re
from stat import *

# To pierwsza wersja. U�yj jej przy pierwszym wywo�aniu
# testu test_find.py
def find (where='.*', content=None, start='.', ext=None, logic=None):
    return ([])

# To druga wersja. Dodaje niekt�re funkcje, ale nie
# oblewa niekt�re teksty.
def find (where='.*', content=None, start='.', ext=None, logic=None):
   context = {}
   context['gdzie'] = where
   context['zawarto��'] = content
   context['zwr��'] = []

   os.path.walk (start, find_file, context)

   return context['zwr��']

def find_file (context, dir, files):
   for file in files:
      # Wydob�d� informacje na temat pliku.
      path = os.path.join (dir, file)
      path = os.path.normcase (path)
      try:
         ext = os.path.splitext (file)[1][1:]
      except:
         ext = ''
      stat = os.stat(path)
      size = stat[ST_SIZE]

      # Nie traktuj filder�w jak pliki.
      if S_ISDIR(stat[ST_MODE]): continue

      # Dokonaj filtracji na podstawie oryginalnych parametr�w find()
      if not re.search (context['gdzie'], file): continue

      # Filtracj� zawarto�ci wykonuj jako ostatni�, by zminimalizowa�
      # koszt wyszukiwania.
      if context['zawarto��']:
         f = open (path, 'r')
         match = 0
         for l in f.readlines():
            if re.search(context['zawarto��'], l):
               match = 1
               break
         f.close()
         if not match: continue

      # Utw�rz zwracan� warto�� dla wszystkich plik�w spe�niaj�cych podane kryteria.
      file_return = (path, file, ext, size)
      context['zwr��'].append (file_return)


# To trzecia, najbardziej rozbudowana wersja. Udaje jej si�
# sprosta� wszystkim testom z test_find.py.

def find (where='.*', content=None, start='.', ext=None, logic=None):
   context = {}
   context['gdzie'] = where
   context['zawarto��'] = content
   context['zwr��'] = []
   context['rozszerzenie'] = ext
   context['logika'] = logic

   os.path.walk (start, find_file, context)

   return context['zwr��']

def find_file (context, dir, files):
   for file in files:
      # Pobierz informacje na temat pliku.
      path = os.path.join (dir, file)
      path = os.path.normcase (path)
      try:
         ext = os.path.splitext (file)[1][1:]
      except:
         ext = ''
      stat = os.stat(path)
      size = stat[ST_SIZE]

      # Nie traktuj folder�w jak pliki.
      if S_ISDIR(stat[ST_MODE]): continue

      # Dokonaj filtracji na podstawie parametr�w z find().
      if not re.search (context['gdzie'], file): continue
      if context['rozszerzenie']:
         if ext != context['rozszerzenie']: continue
      if context['logika']:
         arg = {}
         arg['�cie�ka'] = path
         arg['rozszerzenie'] = ext
         arg['stat'] = stat
         arg['rozmiar'] = size
         arg['modyfikacja'] = stat[ST_MTIME]

         if not context['logika'](arg): continue

      # Filtracj� zawarto�ci wykonuj na ko�cu, bo jest najbardziej kosztowna.
      if context['zawarto��']:
         f = open (path, 'r')
         match = 0
         for l in f.readlines():
            if re.search(context['zawarto��'], l):
               match = 1
               break
         f.close()
         if not match: continue

      # Utw�rz zwracan� warto�� dla wszystkich plik�w spe�niaj�cych podane kryteria.
      file_return = (path, file, ext, size)
      context['zwr��'].append (file_return)
