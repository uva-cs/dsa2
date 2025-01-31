# CS3100 - Fall 2024 - Programming Assignment 1
#################################
# Collaboration Policy: You may discuss the problem and the overall
# strategy with up to 4 other students, but you MUST list those people
# in your submission under collaborators.  You may NOT share code,
# look at others' code, or help others debug their code.  Please read
# the syllabus carefully around coding.  Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################

import sys
import time
from FedUps import FedUps

fp = open("example.txt", 'r')
lines = fp.readlines()

# Parse the input
numCities = int(lines[0])
start = int(lines[1])
end = int(lines[2])
capacities = []
loads = []
capacitiesDone = False

for i in range(3, len(lines)):
    line = lines[i].strip()
    if line == "---":
        capacitiesDone = True
    elif not capacitiesDone:
        capacities.append(line)
    else:
        loads.append(line)
        
# Call method and print the result
startT = time.time()
f = FedUps()
output = f.compute(numCities, capacities, loads, start, end)
endT = time.time()
for city in output:
    print(city)
print("time: "+ str(endT-startT))
