# Author: Barath Srinivasan

# Implement a function to check whether a given linked list contains a cycle.
# Return true if it has a cycle and return false if it does not have a cycle.

# Notes:
# function will be called on the head of the linked list.
# Node has `.val` and `.next` properties.

# Explanation of Code
"""
Basically, I follow a fast i, slow j structure. I create a pointer that goes through each node of my linked list; this is my slow j. I also create a pointer that skips to every other node; this is my fast i. I keep iterating through my list and if my i and j pointer ever intersect, then I know there is a cycle. However, if I hit a null either with my slow or fast pointer, then I know there is no cycle. 
"""

# Analysis of Code
"""
The time complexity of this algorithm is O(n). This is because the worst case is that you visit all the nodes, n, with the slow pointer before reaching the end of the linked list to find no cycle. The space complexity is O(1) because we don't use any additional memory to solve the problem.   
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def hasCycle(head: Node) -> bool:
    if head is not None and head.next is not None and head.next.next is not None: # checks if slow and fast pointers can be set
        slow = head.next # moves through each node
        fast = head.next.next # moves through every other node
        
        while slow.next is not None and fast.next is not None and fast.next.next is not None: # checks if pointers can move foward
            if slow == fast: # checks if slow and fast pointers are equals
                return True # means cycle exists
            
            slow = slow.next # moves the slow pointer by 1
            fast = fast.next.next; # moves the fast pointer to succ's successor
    
    return False # means no cycle exists

