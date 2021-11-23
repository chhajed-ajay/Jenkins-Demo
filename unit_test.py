import unittest
from main import fact

class testFact(unittest.TestCase):
    def testfact(self):
        self.assertEqual(fact(3), 6)

if __name__ == '__main__':
    unittest.main()
