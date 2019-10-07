import unittest
import find
import os, os.path

def filename(ret):
   return ret[1]

class FindTest (unittest.TestCase):
   def setUp (self):
      os.mkdir ("_test")
      os.mkdir (os.path.join("_test", "podfolder"))
      f = open (os.path.join("_test", "plik1.txt"), "w")
      f.write ("""pierwszy wiersz
drugi wiersz
trzeci wiersz
czwarty wiersz""")
      f.close()

      f = open (os.path.join("_test", "plik2.py"), "w")
      f.write ("""To jest plik testowy.
Zawiera wiele wyrazów.
To jest ostatni wiersz.""")
      f.close()

   def tearDown (self):
      os.unlink (os.path.join ("_test", "plik1.txt"))
      os.unlink (os.path.join ("_test", "plik2.py"))
      os.rmdir (os.path.join ("_test", "podfolder"))
      os.rmdir ("_test")

   def test_01_SearchAll (self):
      """ 1: Poszukiwanie wszystkich plików. """
      res = find.find (r".*", start="_test")
      self.failUnless (map(filename,res) == ['plik1.txt', 'plik2.py'],
                       'niepoprawne wyniki')

   def test_02_SearchFileName (self):
      """ 2: Poszukiwanie pliku z u¿yciem wyra¿eñ regularnych. """
      res = find.find (r"file", start="_test")
      self.failUnless (map(filename,res) == ['plik1.txt', 'plik2.py'],
                       'niepoprawne wyniki')
      res = find.find (r"py$", start="_test")
      self.failUnless (map(filename,res) == ['plik2.py'],
                       'nieudane poszukiwanie pliku Pythona')

   def test_03_SearchByContent (self):
      """ 3: Poszukiwanie wed³ug zawartoœci. """
      res = find.find (start="_test", content="pierwszy")
      self.failUnless (map(filename,res) == ['plik1.txt'],
                       "nie znaleziono plik1.txt")
      res = find.find (where="py$", start="_test", content="wiersz")
      self.failUnless (map(filename,res) == ['plik2.py'],
                       "nie znaleziono plik2.py")
      res = find.find (where="py$", start="_test", content="drugi")
      self.failUnless (len(res) == 0,
                       "znaleziono coœ, co nie istnieje")

   def test_04_SearchByExtension (self):
      """ 4: Poszukiwanie z u¿yciem rozszerzenia pliku. """
      res = find.find (start="_test", ext='py')
      self.failUnless (map(filename,res) == ['plik2.py'],
                       "nie znaleziono plik2.py")
      res = find.find (start="_test", ext='txt')
      self.failUnless (map(filename,res) == ['plik1.txt'],
                       "nie znaleziono plik1.txt")

   def test_05_SearchByLogic (self):
      """ 5: Test wyszukiwania z zastosowanie funkcji zwrotnej. """
      res = find.find (start="_test", logic=lambda (x): (x['rozmiar'] < 50))
      self.failUnless (map(filename,res) == ['plik1.txt'],
                       "nieudane znalezienie po rozmiarze")

if __name__ == '__main__':
   unittest.main()
