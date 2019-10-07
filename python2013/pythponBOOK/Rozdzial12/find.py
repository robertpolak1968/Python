import os, os.path
import re
from stat import *

# To pierwsza wersja. U¿yj jej przy pierwszym wywo³aniu
# testu test_find.py
def find (where='.*', content=None, start='.', ext=None, logic=None):
    return ([])

# To druga wersja. Dodaje niektóre funkcje, ale nie
# oblewa niektóre teksty.
def find (where='.*', content=None, start='.', ext=None, logic=None):
   context = {}
   context['gdzie'] = where
   context['zawartoœæ'] = content
   context['zwróæ'] = []

   os.path.walk (start, find_file, context)

   return context['zwróæ']

def find_file (context, dir, files):
   for file in files:
      # Wydob¹dŸ informacje na temat pliku.
      path = os.path.join (dir, file)
      path = os.path.normcase (path)
      try:
         ext = os.path.splitext (file)[1][1:]
      except:
         ext = ''
      stat = os.stat(path)
      size = stat[ST_SIZE]

      # Nie traktuj filderów jak pliki.
      if S_ISDIR(stat[ST_MODE]): continue

      # Dokonaj filtracji na podstawie oryginalnych parametrów find()
      if not re.search (context['gdzie'], file): continue

      # Filtracjê zawartoœci wykonuj jako ostatni¹, by zminimalizowaæ
      # koszt wyszukiwania.
      if context['zawartoœæ']:
         f = open (path, 'r')
         match = 0
         for l in f.readlines():
            if re.search(context['zawartoœæ'], l):
               match = 1
               break
         f.close()
         if not match: continue

      # Utwórz zwracan¹ wartoœæ dla wszystkich plików spe³niaj¹cych podane kryteria.
      file_return = (path, file, ext, size)
      context['zwróæ'].append (file_return)


# To trzecia, najbardziej rozbudowana wersja. Udaje jej siê
# sprostaæ wszystkim testom z test_find.py.

def find (where='.*', content=None, start='.', ext=None, logic=None):
   context = {}
   context['gdzie'] = where
   context['zawartoœæ'] = content
   context['zwróæ'] = []
   context['rozszerzenie'] = ext
   context['logika'] = logic

   os.path.walk (start, find_file, context)

   return context['zwróæ']

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

      # Nie traktuj folderów jak pliki.
      if S_ISDIR(stat[ST_MODE]): continue

      # Dokonaj filtracji na podstawie parametrów z find().
      if not re.search (context['gdzie'], file): continue
      if context['rozszerzenie']:
         if ext != context['rozszerzenie']: continue
      if context['logika']:
         arg = {}
         arg['œcie¿ka'] = path
         arg['rozszerzenie'] = ext
         arg['stat'] = stat
         arg['rozmiar'] = size
         arg['modyfikacja'] = stat[ST_MTIME]

         if not context['logika'](arg): continue

      # Filtracjê zawartoœci wykonuj na koñcu, bo jest najbardziej kosztowna.
      if context['zawartoœæ']:
         f = open (path, 'r')
         match = 0
         for l in f.readlines():
            if re.search(context['zawartoœæ'], l):
               match = 1
               break
         f.close()
         if not match: continue

      # Utwórz zwracan¹ wartoœæ dla wszystkich plików spe³niaj¹cych podane kryteria.
      file_return = (path, file, ext, size)
      context['zwróæ'].append (file_return)
