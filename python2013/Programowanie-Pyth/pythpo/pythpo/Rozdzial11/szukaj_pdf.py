import os, os.path
import re

# Pierwsza implementacja
def print_pdf (arg, dir, files):
   for file in files:
      path = os.path.join (dir, file)
      path = os.path.normcase (path)
      if re.search (r".*\.pdf", path):
         print path


# Kolejna implementacja, kt�ra 
# pomija pliki ze spacjami w nazwach.
def print_pdf (arg, dir, files):
   for file in files:
      path = os.path.join (dir, file)
      path = os.path.normcase (path)
      if not re.search (r".*\.pdf", path): continue
      if re.search (r" ", path): continue

      print path


# Trzecia implementacja wy�wietla pliki, kt�re
# w swojej �cie�ce zawieraj� tekst \mgr.
def print_pdf (arg, dir, files):
   for file in files:
      path = os.path.join (dir, file)
      path = os.path.normcase (path)
      if not re.search (r".*\.pdf", path): continue
      if not re.search (r"\\mgr", path): continue

      print path

os.path.walk ('.', print_pdf, 0)

# Spowoduje wywo�anie ostatniej definicji funkcji.
os.path.walk ('.', print_pdf, 0)

