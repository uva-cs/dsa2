---
title: "DSA2: PA5: Final Exam Scheduling"
---

<figure style="float:right;width:40%;margin-left:20px">
<a href="graph-before.svg"><img src="graph-before.svg"></a>
<figcaption style="text-align:center">The constructed graph to run max flow on.  The classes and rooms are sorted by size, with the smaller classes and rooms on the bottom.</figcaption>
</figure>

It's always difficult to schedule final exams for all the classes at UVA.  Instead of the current method of scheduling final exams -- based on the time the class meets -- UVA wants to see if they can create a schedule that, for a given number of rooms, exam times, and classes, one can find a schedule that makes this all work.

But there is a complication.  There needs to be faculty members present at each exam to proctor it.  Under this new method, it doesn't have to be the faculty member who teaches the class, just any faculty member.  But, in an effort to balance the workload, no faculty member can have too many exams to proctor.

**Part 1: Reduce to Max Flow:** You will be given the number of classes ($c$), a number of rooms ($r$), a number of times ($t$), and a number of proctors ($p$).  For the sake of this assignment, these entities are all 0-index integers (so if $c=7$, then the classes are just 0 through 6).  To solve this problem, you will have to construct a graph such as the upper image on the right.  In that image, there are five sets of bipartite "ranges".  With the exception of one of those sets, all edges have capacity set to 1.

1. From the start ($s'$) to each of the classes: this represents that there is only one exam per class (if a class had multiple exams, then the capacity would be set higher, but that is not part of this assignment).
2. From the classes to the rooms: any class can fit into any room that has a sufficient capacity.  Thus, the lines in this section only connect to rooms that can hold the number of students in the course.  In the diagram, both the courses and the rooms are sorted by size with the smaller courses / rooms on the bottom.  The course sizes will be provided in the input.
3. From the rooms to the times: any exam could potentially be at any time, so this is a complete sub-graph (every room connects to every time).
4. From the times to the proctors: this is based on the proctor's availability, which is provided.  
5. From the proctors to the terminus: to allow the max flow to complete.  Each proctor has some limit of exams they can cover, so the capacity on these edges is set to that limit (5, in this example, but the actual limit varies by the input case).

Once max flow is run on this updated graph, you might get something like the lower of the images to the right.  In that image, the red edges have flow 1, and the green edges more more flow (proctor 3 to the terminus has capacity 3, the other two green edges have capacity 2).  This graph was the result of an actual solution for this assignment.

<figure style="float:right;width:40%;margin-left:20px">
<a href="graph-after.svg"><img src="graph-after.svg"></a>
<figcaption style="text-align:center">The result of running max flow on the graph.  The classes and rooms are sorted by size, with the smaller classes and rooms on the bottom.</figcaption>
</figure>

You will need to print the max flow value (as an integer) from this part in your final output.  The max flow of the graph shown is 9.

**Part 2: Extract the schedule:**  Once we have run max flow, we need to extract the schedule from the graph.  This can be done by tracing the paths through the graph, following edges with flow -- you can pick any outbound path from a given node.

You will need to print those paths in your final output.  This part is worth fewer points than the previous part, and if you do not get to it, there is a modification of the output, and you will still get the majority of the credit for the assignment (assuming your answers are otherwise correct).


### Input

The first line of a file will contain $n$, the number of test cases in that file.  Each test case uses a different graph.

The first line of each test case will contain five positive integers: $c$, $r$, $t$, $p$, and $p_c$, space separated.  The first four are the number of classes, rooms, times, and proctors, respectively.  The last is the proctor capacity -- how many exams they can handle.  For the examples images shown here, $(c,r,t,p,p_c)=(9,5,4,7,5)$.  However, these values -- including $p_c$ -- will vary on the input used to test your program.

The next line will contain $c$ positive integers, which is the class sizes of the $c$ courses.  These will be sorted in non-descending order.

The next line will contain $r$ positive integers, which is the room capacity of the $r$ rooms.  These will be sorted in non-descending order.

The next $p$ lines will contain the scheduling information for the $p$ proctors.  Each of these lines will start with a positive integer $x$ which is how many times that proctor is available for, followed by the $x$ times the proctor is available for (space separated).

All values, both input and output, will fit in a 32-bit singed integer.  All of the "things" referenced (classes, rooms, times, and proctors) are represented as consecutive integers indexing from 0.

You may assume that the provided graph is valid.  You may not assume that the max flow will be equal to the number of classes.  In some test cases, there will be classes that cannot have a final exam scheduled.

### Output

The first line of the output per test case will be the (integer) max flow of the graph.

If you did not complete part 2, then you should print out a -1 on a second line for each test case.

If you did complete part 2, then the next $c$ lines will contain their path (aka their schedule.)  It will be of the form `1 - 2 - 3 - 0`, which indicates that class 1 will use room 2 at time 3 with proctor 0.  These lines can print out in any order.  Note that the separator between each is three characters: space, dash, space.  You may also print out a single letter prefix before each, such as `c1 - r2 - t3 - p0` to indicate course, room, time, and proctor; either format is acceptable, but the ONLY letters you can use on those lines are 'c', 'r', 't', and 'p' (upper case or lower case).

If a class is not assigned a room / time / proctor, then print the class number and -1: `4 -1` (or `c4 -1`).

There are likely going to be many max flow paths through the graph, and any correct one (meaning a valid flow of maximum value) is acceptable.

### Sample input

This input corresponds to the first graph shown above.  In that image, the classes and rooms are sorted by size, with the smaller classes and rooms on the bottom of their respective column.  This means that class $c_0$, the smallest class, is at the bottom of the classes column, and likewise with the room column.  The number in each node corresponds to its number in the input.  

This file is available as [sample.in](sample.in):

```
1
9 5 4 7 5
12 20 34 57 63 63 87 153 725
18 48 72 100 850
2 0 1
1 0
2 0 2
3 0 1 2
3 1 2 3
2 2 3
2 1 3
```


### Sample output

This output corresponds to the second graph shown above.

```
9
c8 - r4 - t1 - p4
c7 - r4 - t0 - p3
c6 - r3 - t0 - p2
c5 - r2 - t2 - p3
c4 - r2 - t1 - p3
c3 - r2 - t0 - p1
c2 - r1 - t1 - p0
c1 - r1 - t0 - p0
c0 - r0 - t2 - p2
```

Note that you could have eliminated the letters ('c', 'r', 't', and 'p') in the above output.

### Requirements

You are *required* to reduce this problem to a max-flow problem.  You should use the networkx package for Python or the JGraphT package for Java.

- Networkx: [https://networkx.org/](https://networkx.org/)
- JGraphT: [https://jgrapht.org/](https://jgrapht.org/)

Your final submission should be in a file named `pa5.py` or `PA5.java`.

