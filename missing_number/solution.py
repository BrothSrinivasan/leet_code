# Given a sorted array A of size n (with n at least 1) where A is uniquely 
# filled with integers in the range 1 to n + 1 such that there is one “missing
# integer” (the “missing integer” is defined as the integer in the 
# range 1 to n + 1 that is not in A), return that “missing integer”.
# Return -1 if the input is None or an empty list.

# Notes:
# * `nums` is a list of integers (e.g. [1,2,4])
# * findMissing will initially be called with
#   `start = 0` and `end = len(nums) - 1`
#   e.g. findMissing([1,2,3,5], 0, 3)

def findMissing(nums, start, end) -> int:
	if nums is None or len(nums) < 1:
		return -1;
	else:
		guassian = (end + 2)*(end + 3)/2;
		totalArr = 0;
		
		for x in nums:
			totalArr += x;
		
		return guassian -  totalArr;
