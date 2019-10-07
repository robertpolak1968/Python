import unittest

class ArithTest (unittest.TestCase):
    def runTest (self):
        """ Testowanie dodawania, brak b³êdów. """
        self.failUnless (1+1==2, 'b³¹d dodawania jeden plus jeden!')
        self.failIf (1+1 != 2, 'kolejny b³¹d dodawania jeden plus jeden!')
        self.failUnlessEqual (1+1, 2, 'i jeszcze jeden b³¹d dla jeden plus jeden!')

class ArithTestFail (unittest.TestCase):
    def runTest (self):
        """ Testowanie dodawania, b³êdy. """
        self.failUnless (1+1==2, 'b³¹d dodawania jeden plus jeden!')
        self.failIf (1+1 != 2, 'kolejny b³¹d dodawania jeden plus jeden!')
        self.failUnlessEqual (1+1, 2, 'i jeszcze jeden b³¹d dla jeden plus jeden!')
        self.failIfEqual (1+1, 2, 'spodziewany b³¹d')
        self.failIfEqual (1+1, 2, 'kolejny spodziewany b³¹d')

def suite_2():
    suite = unittest.TestSuite()
    suite.addTest (ArithTest())
    suite.addTest (ArithTestFail())
    return suite

def suite():
    suite = unittest.TestSuite()
    suite.addTest (ArithTest())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run (test_suite)
    test_suite = suite_2()
    runner.run (test_suite)
