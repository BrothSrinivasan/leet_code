# Author: Barath Srinivasan

# Write a method to merge k Sorted Linked Lists.

# Explanation of Code
"""
I take a list from the top and bottom. I merge them together by using pointers to guide me to the next smallest value. Then after merging, I store the new array at the where the top array was pointing to. Then I decrement the top and increment the bottom and repeat the proccess. Once the top and bottom pointers meet, I continue again to merge the previously merged list together. I continue this until all the lists have been fully merged
"""

# Analysis of Code
"""
The time complexity of this algorithm takes O(nlgn). This is because this code works much like mergesort. In that it takes two lists and merges them together. Then continues to merge the merged lists and so on and so forth. Because it acts like mergesort, we know the time complexity should be O(nlgn). Space complexity for this algorithm is O(1) because while we create a temp list of size 2n, we replace it the two lists that were used for the merging process. So, 2n - n - n, should give us back a net of 0. This means we effectively use constant space for this algorithm.
"""

# Node class with value and pointer to next Node
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def mergeK(heads):
	if heads is None: # checks if array is null
		return []
	
	size = len(heads) - 1 # last indexable index
	
	while size != 0: # continue until all we proccess all arrays
		start = 0 # pointer to start
		end = size # pointer to end
		
		while start < end: # continue until start crosses end
			tempStart = Node(None) # temp header node
			tempPointer = tempStart # temp list
			pointer1 = heads[start]
			pointer2 = heads[end]
			
			while(pointer1 is not None and pointer2 is not None): # check to see if we can compare two lists
				if pointer1.val <= pointer2.val: # adds lower value to temp list and increments pointers
					tempPointer.next = Node(pointer1.val)
					pointer1 = pointer1.next
					tempPointer = tempPointer.next
				else: # if second list has greater value
					tempPointer.next = Node(pointer2.val)
					pointer2 = pointer2.next
					tempPointer = tempPointer.next
			
			# if one list goes empty, we can directly add all of other list to temp list
			if pointer1 is None:
				tempPointer.next = pointer2
			elif pointer2 is None:
				tempPointer.next = pointer1
			
	    # stores temp list and increments pointers
			heads[start] = tempStart.next
			start += 1
			end -= 1
		
		size = end # new size of array
	
	return heads[0] # returns merged list
