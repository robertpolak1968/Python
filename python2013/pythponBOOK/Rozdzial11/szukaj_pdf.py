import os, os.path
import re

# Pierwsza implementacja
def print_pdf (arg, dir, files):
   for file in files:
      path = os.path.join (dir, file)
      path = os.path.normcase (path)
      if re.search (r".*\.pdf", path):
         print path


# Kolejna implementacja, która 
# pomija pliki ze spacjami w nazwach.
def print_pdf (arg, dir, files):
   for file in files:
      path = os.path.join (dir, file)
      path = os.path.normcase (path)
      if not re.search (r".*\.pdf", path): continue
      if re.search (r" ", path): continue

      print path


# Trzecia implementacja wyœwietla pliki, które
# w swojej œcie¿ce zawieraj¹ tekst \mgr.
def print_pdf (arg, dir, files):
   for file in files:
      path = os.path.join (dir, file)
      path = os.path.normcase (path)
      if not re.search (r".*\.pdf", path): continue
      if not re.search (r"\\mgr", path): continue

      print path

os.path.walk ('.', print_pdf, 0)

# Spowoduje wywo³anie ostatniej definicji funkcji.
os.path.walk ('.', print_pdf, 0)

