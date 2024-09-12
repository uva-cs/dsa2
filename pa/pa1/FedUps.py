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
# Your Computing ID: 
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen
#################################
from Graph import Graph 

class FedUps:

    def __init__(self):
        return

    # This is the method that should run the computation
    # of FedUps.  It takes as input the number of cities, 
    # a list of carrying capacities as strings in the form:
    #
    # 2,5,100
    #
    # which means that there is a truck from city 2 to city
    # 5 with a carrying capacity of 100, and lastly a list
    # of current loads as strings in the form:
    #
    # 2,5,40
    #
    # which means that the truck from city 2 to city 5 has
    # current load of 40, the starting city, and the
    # destination city.
    #
    # @return a list of integers indicating the sequence
    # of cities which starts in the start city and ends
    # in the destination city that also minimizes the
    # cumulative sum of percentages of the truck capacities
    # for the route.
    def compute(self, numCities, capacities, loads, start, end):
        return [] 
