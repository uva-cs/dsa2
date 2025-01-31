# DSA2 PA2 skeleton code

# This code shows how to read in the input in the format described at:
# https://uva-cs.github.io/dsa2/pa/pa2/

cases = int(input()) # how many test cases are in the file
for _ in range(cases):
	result = 0 # to hold the final answer
	size = int(input()) # how many not-so-ordered books are in this particular test case
	shelf = [int(x) for x in input().split(" ")]

	# The shelf of not-so-ordered book numbers is in the `shelf` variable

	# Do something here.

	print(result) # the only output is one integer printed per test case
