# PA1 Skeleton Code
# DSA2, spring 2026

# This code will read in the input, and put the values into lists.  It is up
# to you to properly represent this as a graph -- this code only reads in the
# input properly.

test_cases = int(input())
for t in range(test_cases):
	[n,e,q] = [int(_) for _ in input().split(" ")] # number of nodes, edges, and queries
	nodes = ['n'+str(_) for _ in range(n)]
	# read in the edges, all on one line
	tmp = input().split(" ")
	edges = []
	while len(tmp) > 0:
		edges.append((tmp.pop(0),tmp.pop(0)))
	# read in the queries, all on one line
	tmp = input().split(" ")
	queries = []
	while len(tmp) > 0:
		queries.append((tmp.pop(0),tmp.pop(0)))

	print(f"test case {t}:")
	print(f"there are {n} nodes, {e} edges, and {q} queries")
	print("the nodes are:",nodes)
	print("the edges are:",edges)
	print("the queries are:",queries)
	print("")
