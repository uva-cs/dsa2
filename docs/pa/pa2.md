---
layout: default 
title: PA2 - Snow Plows
nav_order: 2
parent: Programming Assignments
---


<img src="https://thumb.wikimedia.org/wikipedia/commons/thumb/3/39/Icy_morning_encounter.jpg/960px-Icy_morning_encounter.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail" style="float:right;max-width:40vw;border-radius:40px;padding-left:10px">

### Introduction

It's snowing in Charlottesville!  It's looking pretty bad out, and it is going to get much worse.  VDOT (Virginia Department of Transportation) is overloaded, and does not have the resources to help keep the entire state's highways an interstates plowed.  They have come to you to help keep the local stretch of interstate I-64 clear.

You are taking the role of the plowing shift manager, and as such are in charge of a number of snow plows; each of which are identical.  You are assigned a stretch of I-64 to clear -- to make this problem viable, we'll assume you have a integer number of *miles*, and a snow plow will plow a whole (i.e., positive integer) number of miles; we'll assume the mile counts start from 0.

Each snow plow must be assigned a *contiguous* section of the interstate.  For example, it might plow miles 5-10, but it would not be assigned to plow 5-8 and then 10-13 -- since it would have to travel from 8-10, it would plow the area between.

Not all miles are equal in difficulty.  Some areas of the interstate are very windy due to the local geography, so they have less snow accumulation and are thus quicker to clear.  Others may be hilly, or have much larger snow drifts to have to be plowed, and will take longer to clear.  More difficult areas require more time to plow.  Thus, each mile will have a *time* needed to clear it, which is a positive integer.

Lastly, you want to reduce the amount of time taken to plow the interstate.  This means balancing the work load among the plows as best you can.

Given a mile range on the interstate, with each mile having a plow clearing time, and a number of plows, your task is to write a **divide-and-conquer** algorithm to determine what is the highest *total time* any one plow has in an optimal solution.  Here, "optimal solution" means that the total time (or, specifically, the time of the plow that takes the longest) is as low as possible.


### Changelog

Any changes to this page will be put here for easy reference.  Typo fixes and minor clarifications are not listed here.  So far there aren't any significant changes to report.


### Example


<div style="float:left;padding-right:10px">
<table>
	<tr><th>Mile #</th><th>Time</th></tr>
	<tr><td>0</td><td>8</td></tr>
	<tr><td>1</td><td>12</td></tr>
	<tr><td>2</td><td>31</td></tr>
	<tr><td>3</td><td>19</td></tr>
	<tr><td>4</td><td>15</td></tr>
</table>
</div>

Consider the case shown in the table, which is plowing 5 mile segments, 0 through 4.  You have 3 plows.

The optimal solution is to schedule these miles is to give the first plow miles 0 and 1 (the plow's *total time* is 20), the second plow gets mile 2 (the plow's *total time* is 31), and the third plow gets miles 3 and 4 (the plow's *total time* is 34).

In this example, the plow with the highest total time has total time of 34, which would be the answer to this test case.

If we had 5 plows, then we would assign one mile to each plow, and the highest total time of any plow would be 31 (the plow clearing mile 2).  In any example, having as many plows as there are miles will yield the minimum possible time to plow the road.  Likewise, having only one plow will yield the maximum time, as that plow has to handle all of the miles.

### Input

**Note: for this homework, we are providing you with skeleton code that handles reading in of the input.  HOWEVER, this will not be provided in future homeworks, so you should ensure that you understand how it works.**

All input is read in from standard input (not a file).

The first line of the file will contain the single positive integer $1 \le c \le 10^5$, the number of test cases in the file.

Each test case will consist of two lines.

The first line will consist of two integers, $2 \le m \le 10^9$, the number of miles, and $2 \le p \le 10^9$, the number of plows.  Furthermore, $m \ge p$ (there will never be more plows than miles).  To simplify mile marker notation, each mile marker will have a number starting from 0.  This, if there are $m$ miles to plow, they are referred to by the consecutive integers 0 to $m-1$.  Likewise, each plow is assigned a consecutive number from 0 to $p-1$.

The second line lists the *times* of each mile to be plowed, space separated.  All times are positive integers $1 \le t \le 10^{15}$.  These values will require being stored in a `long`, not an `int`!  The mile times are listed in order from mile 0 to mile $m-1$.

The skeleton code, which just reads in the input and prints it out, is provided in [pa2.py](files/pa2.py.html) ([src](files/pa2.py)) and [PA2.java](files/PA2.java.html) ([src](files/PA2.java)).

### Output

All output is to be printed to standard output (not a file).

The only output for each test case is the maximum total time of the plows.  Each test case has its output printed on a separate line.  This total time value will fit in a signed `long` variable, but may not fit in an `int`.

### Example input


This file is available as [example.in](files/pa2-example.in).  The first test case in this file corresponds to the example above.

```
4
5 3
8 12 31 19 15
10 4
4 1 3 5 3 7 8 6 5 9
16 5
11 12 25 46 26 43 29 2 19 11 26 18 29 31 35 21
10 2
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
```

There is another example test case described below, in the Requirements section.

### Example output

This file is available as [example.in](files/pa2-example.out).  This output of the above input is shown below.  The last test case is to ensure that you are using `long` variables rather than `int` variables.

```
34
14
93
5000000000
```


### Algorithm

There are two parts to this algorithm: selecting a time to have the road plowed in (which is what we want to optimize), and determining if your $p$ plows can plow the road in that amount of time.  The first part is through a binary search -- rather than searching through an array, you search through the possible times from the minimum time (there are as many plows as there are miles) and the maximum time (only one plow).  For the second part, we start with one plow at the beginning of the mile range, and just keep adding consecutive mile clearing times until the next one would cause us to go over, and then we proceed onto the next plow; this may result in learning that one cannot clear the road with your $p$ plows in a given time.


### Requirements

***This must be a divide-and-conquer solution!***  To ensure this, we have a few test cases that will cause all other potential solutions to either time out or cause a stack overflow due to recursion depth.  One such test case has one thousand plows and one million miles, and is available in Canvas's files (named `pa2-example-1M.in`, but stored in a .zip file named `pa2-example-1M.in.zip`).  The output from that test case is 500,507.

There are some assumptions that you may and may not make:

- All mile times are positive integer (`long`) values
- The input provided will always be valid
- The values in the array, as well as the answer, may not fit in a `int` variable, but will fit into a signed `long` variable
- There will be at least 2 miles and at least 2 plows
- There will never be more plows than miles


### Execution

We will run your program as follows:

```
cat example.in | python3 pa2.py
```

or:

```
cat example.in | java PA2
```

This takes the output of what is on the left (`cat example.in`, whose output is the contents of the example.in file) and uses it as the input to what is on the right.  This version should work in all platforms (Windows, MacOS, and Linux).

### Submission

You will submit your completed `pa2.py` or `PA2.java` file to Gradescope.  There will be a *small set* of acceptance tests that are *NOT COMPREHENSIVE*.  These acceptance tests are the test cases in [example.in](files/pa2-example.in) file.  It's up to you to comprehensively test your code.  The acceptance tests just verify that you are reading the input correctly and providing the expected output.
