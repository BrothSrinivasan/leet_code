import unittest
from solution import findMissing

class PublicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        self.assertEqual(3, findMissing([1,2,4], 0, 2))

    def test2(self):
        self.assertEqual(4, findMissing([1,2,3,5], 0, 3))

    def test3(self):
        self.assertEqual(2, findMissing([1,3], 0 , 1))

    def test4(self):
        self.assertEqual(1, findMissing([2,3,4], 0, 2))

if __name__ == "__main__":
    unittest.main()
