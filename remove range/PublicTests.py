import unittest
from solution import removeOutsideRange

class TreeNode:  
    def __init__(self, data):  
        self.val = data  
        self.left = None
        self.right = None

def insert(tree, data):
    if not tree:
        return TreeNode(data)
    elif data < tree.val:
        tree.left = insert(tree.left, data)
    else:
        tree.right = insert(tree.right, data)
    return tree

def inorder(tree):
    sol = []
    def helper(curr):
        if curr:
            helper(curr.left)
            sol.append(curr.val)
            helper(curr.right)
    helper(tree)
    return sol





class PublicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        tree = TreeNode(6)
        for num in [-13, -8, 14, 15, 13, 7]:
            insert(tree, num)
        new_tree = removeOutsideRange(tree, -10, 13)

        self.assertEqual(inorder(new_tree), [-8, 6, 7, 13])

    def test2(self):
        tree = TreeNode(10)
        for num in [7, 5, 11, 13, 12]:
            insert(tree, num)
        new_tree = removeOutsideRange(tree, -100, 100)
        self.assertEqual(inorder(new_tree), [5, 7, 10, 11, 12, 13])

    def test3(self):
        tree = TreeNode(10)
        for num in [7, 5, 11, 13, 12]:
            insert(tree, num)
        new_tree = removeOutsideRange(tree, 100, 101)
        self.assertEqual(inorder(new_tree), [])

    def test4(self):
        tree = TreeNode(18)
        for num in [1, 2, 11, 13, 12, 3, 6, 16, 7, 8, 9, 14, 10, 15, 17, 4, 5]:
            insert(tree, num)
        new_tree = removeOutsideRange(tree, 3, 13)
        self.assertEqual(inorder(new_tree), [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])



if __name__ == "__main__":
    unittest.main()
