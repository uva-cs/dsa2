---
title: "DSA2: PA1: FedUps"
---

### Description

Package delivery isn't what it used to be.  With a rise in premium package delivery services, FedEx and UPS have now created a new tier in their delivery service options: FedUps sub-premium delivery subscription service.  Subscribers to FedUps will receive a small discount on their shipping costs, but they must agree to receive only the worst customer treatment and delivery times for all packages. One example of this intentionally poor treatment is that FedUps will now send your packages to you via routes that are not guaranteed to be the most efficient. Instead, FedEx and UPS will try to use FedUps orders to do their best to minimize the excess capacity of all of their vehicles.

Your algorithm will receive two weighted graphs (lists of edges) as input. The first graph will represent the total transportation capacities of their vehicles. The nodes represent cities, edges represent trucks traveling between cities, and the weight of the edge represents the maximum weight that can be carried by each truck.  The second graph will represent the remaining available capacities on all vehicles. The same nodes and edges will be present as for the first graph, but now the edges represent how much more cargo each truck can carry.

Your goal will be to write an algorithm which finds the path from a given start city to a destination city which *minimizes the sum of load percentages* across the nodes in the graph. Note that the number of trucks is irrelevant, we only care to *minimizes the sum of load percentages*. At-capacity trucks may not be used, since FedUps could not add a package to that truck.

### Changelog

- Tue, 9/24: To make this assignment more feasible, we are changing the goal: instead of "maximizes the percentage of available capacity" we are "minimizes the sum of load percentages".  Note that what you have to minimize is the load percentage (how much space is taken), but what is given to you in the problem is the available space (how much space is left).  Also, another example test cases was added.
- Sun, 9/15: The original graph had an error: the edge from 0->3 should be "0/60" (as now shown below); the example.txt and the I/O output below was fixed the next day

### Input

Your input will be 5 parameters containing the following information:

- `numCitites` - the number of total cities; the cities are integers from 0 to $numCities-1$.
- `start` - the start city.
- `end` - the destination city.
- `capacities` - a list of the total capacities of each of the trucks, given as a list of strings.  Each string in the list contains a comma-separated list of integer values: the truck's starting city, the truck's destination city, and the truck's total carrying capacity.
- `available` - a list of available capacity of each of the trucks, given as a list of strings.  Each string in the list contains a comma-separated list of integer values: the truck's starting city, the truck's destination city, and the truck's available capacity.

The provided skeleton code, below, already reads in the input from an `example.txt` file.

### Output

Your output will be a list of integers indicating the sequence of cities which starts in the start city and ends in the destination city, that also *minimizes the sum of load percentages*.  The main method provided will print this list one city per line.  An example output is given below.

### Running Time Requirements

The worst-case asymptotic running time of your program should belong to $O(c \cdot t)$, where $c$ is the number of cities and $t$ is the number of trucks.


### Example

![](pa1-graph.jpg){style="float:right"}

Consider the graph to the right.  The start is at node 0, and the end is at node 3.


In this example, there are three paths from the start node to the end node.  The correct path your algorithm should return would be [0,2,3]. 

- The edge [0,3] is at capacity (has 0 available space), so it cannot be used.
- The path [0,1,4,3] has available capacity 16/40 (40%) on each of the three segments, or 40%.  The sum of these is 120%/
- The path [0,2,3] has available capacity 60/100 (60%) for the path from 0-2, and 40/100 (40%) for the path from 2-3.  This sums to 100%.

As the third path *minimizes the sum of load percentages*, it would be the output path.

The actual output would be:

```
0
2
3
```

If we made one graph change -- changing the available capacity of the (0,3) edge to 60 (so there is a lot of available space on that truck), then the output would be:

```
0
3
```


<br clear='all'>


### Example Input

- `numCities = 5`
    - The nodes are all integers, indexed from 0
- `start = 0`
- `end = 3`
- `capacities` the list:
```
0,1,40
0,2,100
0,3,60
1,4,40
2,3,100
4,3,40
```
- `available` the list:
```
0,1,16
0,2,60
0,3,0
1,4,16
2,3,40
```

The exact input would be the following; this is available in the [example.txt](example.txt) file.

```
5
0
3
0,1,40
0,2,100
0,3,60
1,4,40
2,3,100
4,3,40
---
0,1,16
0,2,60
0,3,0
1,4,16
2,3,40
4,3,16
```


### Example Output

The exact output would be:


```
0
2
3
```

### Submission Requirements

-   Your algorithm must be written in Python 3.10.12 or Java 21.0.4 (OpenJDK)
-   You must download the appropriate wrapper code based on the language you choose: `Main.py`, `FedUps.py`, and `Graph.py` for Python; `Main.java`, `FedUps.java`, and `Graph.java` for Java.
    - Java files: [FedUps.java](FedUps.java.html) ([src](FedUps.java)), [Graph.java](Graph.java.html) ([src](Graph.java)), and [Main.java](Main.java.html) ([src](Main.java))
    - Python files: [FedUps.py](FedUps.py.html) ([src](FedUps.py)), [Graph.py](Graph.py.html) ([src](Graph.py)), and [Main.py](Main.py.html) ([src](Main.py))
    - For both: [example.txt](example.txt)
-   Implement the `compute()` method in the `FedUps` class. The `compute()` method should execute the entirety of your algorithm and return the list of cities in the path.
-   Implement the `Graph` class using an Adjacency List graph implementation.  You should then use this in your `FedUps` class.
-   You *may* modify the `Main.java` or `main.py` files to test your algorithm, but they **will not** be used during grading.
-   You must submit your {`FedUps.java` and `Graph.java`} or {`FedUps.py` and `Graph.py`} files on Gradescope. Do **not** submit `Main.java`, `main.py`, or any test files.
-   A few other notes:
    -   Your code will be run as:  
        - `python Main.py` or `python3 Main.py` for Python
        - `javac *.java && java Main` for Java
    -   Any and all source code must be in the two files that you submit (FedUps.py/java and Graph.py/java)
    -   You may **not** use any graph packages for this assignment.
    -   Please note that you are responsible for analyzing the running time of any algorithm you use and ensuring that they satisfy the runtime requirements for this assignment.

### Rules on Collaboration and Outside Sources

You must follow the rules about Collaboration and Outside Sources [in the syllabus](https://uva-cs.github.io/dsa2/syllabus.html#honesty-and-collaboration).

### Use of Generative AI

For PA1, you are not allowed to use generative AI tools to help you solve this problem.

