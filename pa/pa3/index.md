---
title: "PA3: Office Hours Redux"
---

<img src="../pa2/office-hours-sign.jpg" style="float:right;max-width:40vw;border-radius:40px;padding-left:10px;border:3px solid black">

### Introduction

The TAs tried out the previous office hours scheduling idea (from [PA2: Office Hours](../pa2/index.html)), and ended up not liking it all that much.  So they have revolted again!  This time they want to create a new and different office hours schedule.

In the new version, each TA will hold one shift each, and will specify when they will start and when they will end.  Any given TA's shift may overlap with one (or more) other shifts, or they may be alone.  Given a series of such TA shift requests, they need to be combined into a single set of times when there are TAs in office hours.

For example:

- TA A wants to work from 1 pm to 3 pm
- TA B wants to work from 2 pm to 4 pm
- TA C wants to work from 8 pm to 10 pm

Given these, the shifts of TAs A and B would combine to form one longer streak of office hours from 1 pm to 4 pm.  Thus, the final office hours schedule would list from 1 pm to 4 pm and then from 8 pm to 10 pm.

To make life easier, we will present the times as numbers.  The above example would list TA A's request as 1-3, TA B's from 2-4, and TA C's from 8-10.  The final answer would be 1-4 and 8-10.  Times in this assignment can be any non-negative integer within the range described in the input section below.

Note that a shift from 1-3 and another shift from 3-5 overlaps, as there is a TA present from 1 pm to 5 pm.  But a shift from 1-3 and another from 4-6 do *not* overlap -- a TA is present from 1 pm to 3 pm and then from 4 pm to 6 pm, but not from 3 pm to 4 pm.

Given a set of requests of this form, create a *greedy* algorithm that can combine the TA shift requests into a single TA office hours schedule.

### Changelog

Any changes to this page will be put here for easy reference.  Typo fixes and minor clarifications are not listed here.  So far there aren't any significant changes to report.


### Input format

**For this homework, we are *NOT* providing you with skeleton code that handles reading in of the input.**  You should look at the previous two homeworks for examples how to do so: [PA1: Driving Directions](../pa1/index.html) ([md](../pa1/index.md)) and [PA2: Office Hours](../pa2/index.html) ([md](../pa2/index.md)).


All input is read in from standard input (not a file).

The first line of the file will contain the single positive integer $1 \le c \le 10^5$, the number of test cases in the file.

Each test case will start with a line containing a single positive integer $1 \le r \le 10^9$, which is the number of shift requests in the file.  The next $r$ lines will consist of a single ordered pair each, the start and end times of each shift request.  A shift request is two integers $(0 \le s \le 10^9, 0 \le t \le 10^9)$, with $t > s$, the start time ($s$) and end time ($t$) of the shift request.  These two values are space separated.

All input values will fit into a signed `int` variable.


### Output format

**The output format is very precise.  Extra spaces, extra lines, or different punctuation will cause the answer to be judged as incorrect.**

Each test case will output a single line that contains all of the combined shifts, in `x-y` form (a dash between the start and end times), with each range separated by a comma and a space.  The example above would have the output: `1-4, 8-10`.

All output values will fit into a signed `int` variable.

### Example input

This file is available as [example.in](example.in).

```
4
4
7 8
1 5
2 4
4 6
1
1 2
5
1 2
3 4
5 6
7 8
9 10
5
8 22
48 50
16 22
31 43
30 45
```

### Example output

This file is available as [example.out](example.out).

```
1-6, 7-8
1-2
1-2, 3-4, 5-6, 7-8, 9-10
8-22, 30-45, 48-50
```

### Notes

This assignment must be a *greedy solution*.  Specifically, it needs to be a $\Theta(n \log n)$ solution -- a $\Theta(n^2)$ solution will time out with our larger test cases.  To ensure this, we have a few test cases that will cause all other potential solutions to time out.  Some of those test cases are given below.

There are some assumptions that you may and may not make:

- All values, both input and output, are non-negative integer values that will fit into a signed `int` variable
- The input provided will always be valid
- There will be at least one shift request in each test case
- The end time for a shift request will always be strictly greater than the start time of that shift request


There are two large test cases available in Canvas' Files.  They are contained in a zip file named `pa3-examples.zip`.  The files therein are:

- `pa3-example-1M.in`: this has 1 million randomly generated shifts.  The solution for this problem is: `20-4317505, 4317530-53367411, 53367771-67213730, 67213768-89410658, 89410677-100000000`
- `pa3-example-1M-exclusive.in`: this has 1 million shifts are are all mutually exclusive (there is no overlap).  The solution will be 1 million ranges, that will start with: `0-1, 2-3, 4-5, 6-7, 8-9, 10-11, ...`

If your program does not implement a greedy algorithm, at least one of those cases will time out when we run it.

### Execution

We will run your program as follows:

```
cat example.in | python3 pa3.py
```

or:

```
cat example.in | java PA3
```

This takes the output of what is on the left (`cat example.in`, whose output is the contents of the example.in file) and uses it as the input to what is on the right.  This version should work in all platforms (Windows, MacOS, and Linux).

### Submission

You will submit your completed `pa3.py` or `PA3.java` file to Gradescope.  There will be a *small set* of acceptance tests that are *NOT COMPREHENSIVE*.  These acceptance tests are the test cases in [example.in](example.in) file.  It's up to you to comprehensively test your code.  The acceptance tests just verify that you are reading the input correctly and providing the expected output.
