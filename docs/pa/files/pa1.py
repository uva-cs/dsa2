# PA1 (fall 2026) Python skeleton code
#
# This file shows how to read and parse the input, which is provided via
# standard input


edges = [] # will be a list of 4-tuples: source node (string), 
		   # dest node (string), available capacity, total capacity
nodes = [] # will be the string names of the nodes
start_node = end_node = None


def read_input():
	global edges, nodes, start_node, end_node
	parts = input().strip().split(" ")
	num_edges = int(parts[0])
	start_node, end_node = parts[1], parts[2]
	nodeset = set()
	for _ in range(num_edges):
		parts = input().split(" ")
		nodeset.add(parts[0])
		nodeset.add(parts[1])
		parts[2] = int(parts[2])
		parts[3] = int(parts[3])
		edges.append( tuple(parts) )
	nodes = list(nodeset)


# read the input from standard input
read_input()


# REMOVE THESE LINES BEFORE SUBMISSION
# any extra output will cause the program to be marked incorrect
print(f"Start node is {start_node}, end node is {end_node}")
print(f"The list of {len(nodes)} nodes:",nodes)
print(f"The list of {len(edges)} edges:",edges)
