# Author: Barath Srinivasan

# Given a rod of length n and a dictionary mapping the length
# of a rod to the price you can get for it, determine the max
# value you can obtain by cutting the rod into smaller pieces.
# You may cut the rod into as many pieces as necessary to obtain the max value.

# Explanation of Code
"""
The code could have structured such that I explore all possible subsets to find the subset that produces the max value. However, the problem is this is an inefficient algorithm as we will end up recalculating a lot of similar value. So, we can improve on this by realizing we need the max of the price of the current length plus the optimal cost of the length less than our current size. This way allows us to store previously calculated answers since we solve the smaller subproblems first.
"""

# Analysis of Code
"""
The time complexity of the code is O(n^2). This is because we have two for-loops in our algorithm whose summation solves to O(k^2). Also, our space complexity is O(n) because we use an additional n space array to store previously calculated answers.
"""

def rod_cutter(length, prices):
	if length is 0 or prices is None: # edge case check
		return 0;
	
	memo = [0] * (length+1); # creating space to save old subproblems
	
	c1 = 1; # counter for subproblem
	while c1 <= length:
		optValue = -1; # optimal value
		priceToUse = 0; # our price var
		
		c2 = 1; # counter for current price
		while c2 <= c1:
			if c2 in prices: # extracts info from dictionary or returns a 0
				priceToUse = prices[c2];
			else:
				priceToUse = 0;
			
			optValue = max(optValue, (priceToUse + memo[c1 - c2])); # optimization
			c2 += 1;
		
		memo[c1] = optValue; # save optimal solution
		c1 += 1;
	
	return memo[length]; # return the most optimal solution
