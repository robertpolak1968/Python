import unittest

class ArithTestSuper (unittest.TestCase):
    def setUp (self):
        print "Inicjalizacja testu ArithTest"

    def tearDown (self):
        print "Czyszczenie testu ArithTest"

class ArithTest (ArithTestSuper):
    def runTest (self):
        """ Testowanie dodawania, brak b³êdów. """
        print "Wykonywanie ArithTest"
        self.failUnless (1+1==2, 'b³¹d dodawania jeden plus jeden!')
        self.failIf (1+1 != 2, 'kolejny b³¹d dodawania jeden plus jeden!')
        self.failUnlessEqual (1+1, 2, 'i jeszcze jeden b³¹d dla jeden plus jeden!')

class ArithTestFail (ArithTestSuper):
    def runTest (self):
        """ Testowanie dodawania, b³êdy. """
        print "Wykonywanie ArithTestFail"
        self.failUnless (1+1==2, 'b³¹d dodawania jeden plus jeden!')
        self.failIf (1+1 != 2, 'kolejny b³¹d dodawania jeden plus jeden!')
        self.failUnlessEqual (1+1, 2, 'i jeszcze jeden b³¹d dla jeden plus jeden!')
        self.failIfEqual (1+1, 2, 'spodziewany b³¹d')
        self.failIfEqual (1+1, 2, 'kolejny spodziewany b³¹d')


class ArithTest2 (unittest.TestCase):
    def setUp (self):
        print "Inicjalizacja testu ArithTest2"

    def tearDown (self):
        print "Czyszczenie testu ArithTest2"

    def runArithTest (self):
        """ Testowanie dodawania, brak b³êdów, jedna klasa. """
        print "Wykonywanie ArithTest w ArithTest2"
        self.failUnless (1+1==2, 'b³¹d dodawania jeden plus jeden!')
        self.failIf (1+1 != 2, 'kolejny b³¹d dodawania jeden plus jeden!')
        self.failUnlessEqual (1+1, 2, 'i jeszcze jeden b³¹d dla jeden plus jeden!')

    def runArithTestFail (self):
        """ Testowanie dodawania, b³êdy, jedna klasa. """
        print "Wykonywanie ArithTestFail w ArithTest2"
        self.failUnless (1+1==2, 'b³¹d dodawania jeden plus jeden!')
        self.failIf (1+1 != 2, 'kolejny b³¹d dodawania jeden plus jeden!')
        self.failUnlessEqual (1+1, 2, 'i jeszcze jeden b³¹d dla jeden plus jeden!')
        self.failIfEqual (1+1, 2, 'spodziewany b³¹d')
        self.failIfEqual (1+1, 2, 'kolejny spodziewany b³¹d')


def suite():
    suite = unittest.TestSuite()

    # Pierwsze podejœcie:
    suite.addTest (ArithTest())
    suite.addTest (ArithTestFail())

    # Drugie podejœcie:
    suite.addTest (ArithTest2("runArithTest"))
    suite.addTest (ArithTest2("runArithTestFail"))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run (test_suite)
