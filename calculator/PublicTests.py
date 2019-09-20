import unittest
from solution import calculate

class PublicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        self.assertEqual(2, calculate("1+1"))

    def test2(self):
        self.assertEqual(0, calculate(""))

    def test3(self):
        self.assertEqual(10, calculate("2*1+8"))

    def test4(self):
        self.assertEqual(10, calculate("4/2+8"))

if __name__ == "__main__":
    unittest.main()
