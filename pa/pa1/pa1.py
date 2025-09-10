# PA1 Skeleton Code
# DSA2, fall 2025

# This code will read in the input, and put the values into lists.  It is up
# to you to properly represent this as a graph -- this code only reads in the
# input properly.

# How many input cases are there?
n = int(input())

for _ in range(n):
	# read in the weights into wt, wf, wb, wc (wegiths for the edges of type tree, forward, backward, and cross, respectively)
	[wt,wf,wb,wc] = [int(x) for x in input().split(" ")]

	# read in the number of vertices and edges, respectively
	[v,e] = [int(x) for x in input().split(" ")]

	# all the edges in the graph -- the result is a list of tuples, such as: [('A', 'B'), ('B', 'C'), ... ]
	l = list(reversed(input().split(" ")))
	edges = [(l.pop(),l.pop()) for _ in range(len(l)//2)]

	# the start node and the node to print the pathogen load for
	(start,node) = input().split(" ")


	# YOUR CODE HERE (or above the for loop)
