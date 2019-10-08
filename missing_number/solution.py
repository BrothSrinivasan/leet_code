# Author: Barath Srinivasan

# Given a sorted array A of size n (with n at least 1) where A is uniquely 
# filled with integers in the range 1 to n + 1 such that there is one “missing
# integer” (the “missing integer” is defined as the integer in the 
# range 1 to n + 1 that is not in A), return that “missing integer”.
# Return -1 if the input is None or an empty list.

# Notes:
# `nums` is a list of integers (e.g. [1,2,4])
# findMissing will initially be called with
# `start = 0` and `end = len(nums) - 1`
# e.g. findMissing([1,2,3,5], 0, 3)

# Explanation of Code
"""
Basically, I know the array is a sorted array with unique values from 1 to n+1. That means the sum of the entire array is the guassian sum. So, I first compute the guassian sum as the expected value the array should sum to if no integers were missing. Then I loop over my array to calculate the actual sum of the array. Then the difference of my expected and actual sum will be the missing integer for me to return.
"""

# Analysis of Code
"""
The time complexity is O(n). This is because I iterate over the array once to get its sum. All the other lines are constant calculations (i.e. calculating the guassian sum using the formula instead of an iteration). And my space complexity is O(1). This is because no matter how big or small my n value is, my space consists of a single use to hold the expected guassian and a single use of space to hold the actual sum. 
"""

def findMissing(nums, start, end) -> int:
	if nums is None or len(nums) < 1:
		return -1;
	else:
		guassian = (end + 2)*(end + 3)/2;
		totalArr = 0;
		
		for x in nums:
			totalArr += x;
		
		return guassian -  totalArr;
