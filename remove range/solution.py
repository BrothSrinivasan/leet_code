# Author: Barath Srinivasan

# Write a function that takes a binary search tree, and two integers, Min and Max,
# and returns a binary search tree with elements outside of the 
# range [Min, Max] (inclusive) removed.

# Explanation of Code
"""
I first recursively call the remove function on both my left and right children. This is ensure that the tree I am currently working with has no numbers that fall outside of the given range. Once I ensure this, I check the current Node value to see if it falls within the range. If it does, I return that Node; however, if it doesn't fall in range, then I return the left or right child which is dependent on which side of the range the Node falls out.
"""

# Analysis of Code
"""
The time complexity of algorithm is O(n) because I visit Node once to determine whether it falls in range. Also, the space complexity is also O(n) because I visit each Node using a recursive call, which gets added to the Stack. So, I require an additional O(n) space in order to compute my answer. 
"""

#Tree class
class TreeNode:  
    def __init__(self, data):  
        self.val = data  
        self.left = None
        self.right = None

def removeOutsideRange(root, Min, Max): 
	if root is None: # checks if root is null (base case)
		return None # returns null if this is the case
	
	root.left = removeOutsideRange(root.left, Min, Max) # removes valid nodes on left child
	root.right = removeOutsideRange(root.right, Min, Max) # removes valid nodes on right child
	
	if root.val < Min: # checks if Node is less than Min
		return root.right # returns right child, which is bigger than curr Node
	elif root.val > Max: # checks if Node is greater than Max
		return root.left # returns left child, which is less than curr Node
	else: # Node falls in range
		return root # return the Node

