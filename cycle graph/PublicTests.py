import unittest
from solution import is_cycle

class PublicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        adj_matrix = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
        self.assertTrue(is_cycle(adj_matrix))
    
    def test2(self):
        adj_matrix = [[0, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertFalse(is_cycle(adj_matrix))
    
    def test3(self):
        adj_matrix = [[0, 1, 0, 1], [1,0,1,0], [0, 1, 0, 1], [1,0,1,0]]
        self.assertTrue(is_cycle(adj_matrix))
    
    def test4(self):
        adj_matrix = None
        self.assertFalse(is_cycle(adj_matrix))
        

if __name__ == "__main__":
    unittest.main()
