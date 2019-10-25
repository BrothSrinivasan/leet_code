import unittest
from solution import hasCycle

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


class PublicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        linkedlist1 = Node(1)
        linkedlist1.next = Node(2)
        linkedlist1.next.next = Node(3)
        self.assertFalse(hasCycle(linkedlist1))

    def test2(self):
        self.assertFalse(hasCycle(Node(42)))

    def test3(self):
        head = None
        self.assertFalse(hasCycle(head))

    def test4(self):
        a = Node(10)
        b = Node(11)
        c = Node(12)
        d = Node(13)
        a.next = b
        b.next = c
        c.next = d
        d.next = b
        self.assertTrue(hasCycle(a))

if __name__ == "__main__":
    unittest.main()
