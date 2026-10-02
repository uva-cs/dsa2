# PA2 Skeleton Code
# DSA2, fall 2026



# YOUR CODE HERE



# This reads in the input from stdin -- you can always assume that the input is valid
test_cases = int(input())
for _ in range(test_cases):
    [m, p] = [int(x) for x in input().split(" ")]
    times = [int(x) for x in input().split(" ")]
    
    # print out the values read in -- this has to be deleted prior to submission!
    print(m,p)
    print(" ".join([str(x) for x in times]))

    # call your function here
