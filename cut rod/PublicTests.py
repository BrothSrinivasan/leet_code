import unittest
from solution import rod_cutter

class PublicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        prices = {1:5}
        self.assertEquals(15, rod_cutter(3, prices))

    def test2(self):
        prices = {1:1, 2:3, 4:1, 8:20}
        self.assertEquals(7, rod_cutter(5, prices))

    def test3(self):
        prices = {1:1, 2:1, 3:2, 4:2, 5:20}
        self.assertEquals(40, rod_cutter(10, prices))

    def test4(self):
        prices = {1:1, 2:2, 3:3, 4:4}
        self.assertEquals(0, rod_cutter(0, prices))


if __name__ == "__main__":
    unittest.main()
