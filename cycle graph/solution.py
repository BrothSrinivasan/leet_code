# Author: Barath Srinivasan

# Given an unweighted undirected graph, return true if it is a Cycle graph;
# else return false. A Cycle Graph is one that contains a single cycle and every
# node belongs to that cycle (it looks like a circle).

# Notes:
# a cycle is only defined on 3 or more nodes.
# adj_matrix is an n-by-n list of lists representing the adjacency matrix of a simple graph. adj_matrix[i][i] = 0 for all i from 0 to n-1 (inclusive).


# Explanation of Code
"""
My reasoning was that for the graph to be a single cycle is if each node has exactly two paths. For example consider this valid example: 4<-1<->2<->3<->4->1. Every node is surrounded by a path foward and a path backward. Using this reasoning, I just run through the matrix to see if row has two paths. 
"""

# Analysis of Code
"""
The time complexity of this code is O(E^2). This is because a single row has enough elements to correspond to every node in the graph, thus V equals E. Since we we do a count function for each row, the complexity is O(E^2). Space complexity is O(1) since I don't use any additional space for my computation.
"""

def is_cycle(adj_matrix):
	if adj_matrix is not None: # checks if we can param is null
		for c in range(0, len(adj_matrix)): # goes through all rows of the matrix
			if adj_matrix[c].count(1) is not 2: # checks the number of connections in the node
				return False; # is there is not exactly 2 connections, then the cycle doesn't exist
		
		return True; # exactly 2 connections for all Nodes
	return False; # param was null
