---
title: "PA2: Office Hours"
---

<img src="office-hours-sign.jpg" style="float:right;max-width:40vw;border-radius:40px;padding-left:10px;border:3px solid black">

### Introduction

The TAs have revolted, and want a new office hours schedule!  Rather than having a fixed time in the evenings, they want to start holding office hours 24/7.  They have a few demands for their new office hours shifts.  

1. Some office hours are busier than others, some are less busy.  So each office hour shift has a positive integer *weight* indicating how busy it is.  The sum of the shift weights should be split, as evenly as possible, among the TAs, so that each TA is carrying a (roughly equal) load of shift weights (called the *total weight* for that TA).
2. The TAs do not want to keep having to come back to Rice Hall for their different shifts.  Thus, any one TA's shifts must be *consecutive*.
3. There is only one TA per shift.

Given a set of shift weights, and a number of TAs, your task is to determine what is the highest *total weight* any one TA has using a divide-and-conquer algorithm.


### Changelog

Any changes to this page will be put here for easy reference.  Typo fixes and minor clarifications are not listed here.  So far there aren't any significant changes to report.


### Example


<div style="float:left;padding-right:10px">

| Shift # | Weight |
|---------|--------|
| 0 | 8 |
| 1 | 12 |
| 2 | 31 |
| 3 | 19 |
| 4 | 15 |

</div>

While a real office hours shift would have 168 separate shifts (24 hours in a day times 7 days in a week), the example given here is much smaller so that it is more easily understandable.  Consider the case where there are 3 TAs, and the weights of the shifts are shown in the table to the left.

The most optimal way to schedule these shifts is to give the first TA shifts 0 and 1 (the TA's *total weight* is 20), the second TA gets shift 2 (the TA's *total weight* is 31), and the third TA gets shifts 3 and 4 (the TA's *total weight* is 34).

In this example, the TA with the highest total weight has total weight of 34.

If we had 5 TAs, then we would assign one shift to each TA, and the highest total weight of any TA would be 31 (the TA staffing shift 2).

<br clear='all'>

### Input

**Note: for this homework, we are providing you with skeleton code that handles reading in of the input.  HOWEVER, this will not be provided in future homeworks, so you should ensure that you understand how it works.**

All input is read in from standard input (not a file).

The first line of the file will contain the single positive integer $1 \le c \le 10^5$, the number of test cases in the file.

Each test case will consist of two lines.

The first line will consist of two integers, $2 \le s \le 10^9$, the number of shifts, and $2 \le t \le 10^9$, the number of TAs.  Furthermore, $s \ge t$ (there will never be more TAs than shifts).  To simplify shift notation, each shift will have a number starting from 0.  This, if there are $s$ shifts, they are referred to by the consecutive integers 0 to $s-1$.  Likewise, each TA is assigned a consecutive number from 0 to $t-1$.

The second line lists the *weights* of each shift, space separated.  All weights are positive integers $1 \le w \le 10^{15}$.  These values will require being stored in a `long`, not an `int`!  They are listed in order from shift 0 to shift $s-1$.

The skeleton code, which just reads in the input, is in [pa2.py](pa2.py.html) ([src](pa2.py)) and [PA2.java](PA2.java.html) ([src](PA2.java)).

### Output

All output is to be printed to standard output (not a file).

The only output for each test case is the maximum total weight of the TAs.  Each test case has its output printed on a separate line.  This total weight value will fit in a signed `long` variable, but may not fit in an `int`.

### Example input


This file is available as [example.in](example.in).  The first test case in this file corresponds to the example above.

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

This output of the above input is shown below.  The last test case is to ensure that you are using `long` variables rather than `int` variables.

```
34
14
93
5000000000
```


### Algorithm

The divide-and-conquer algorithm for this problem is based on that of a [binary search](https://en.wikipedia.org/wiki/Binary_search).  Make sure you understand how that works before reading further.

<div style="float:left;padding-right:10px">

| | | | | | |
|----------|----------|----------|----------|----------|----------|
| Shift: | 0 | 1 | 2 | 3 | 4 |
| Weight: | 8 | 12 | 31 | 19 | 15 |
| Sum of weights so far: | 8 | 20 | 51 | 70 | 85 |

</div>

The table to the left contains the five shifts from the example above, their individual shift weights, and the sum of the weights encountered as we move left-to-right in the list of shifts.  Note that the middle row -- the weights -- is what is read in from standard input.

If we had an as many TAs as shifts, then the minimum total weight for any one TA would be 31 -- we would have one TA on each shift, and the TA on shift 2 would have total weight 31.  If we had only one TA, then the total weight on any one TA would be 85 -- s/he would cover all five of those shifts, and the sum of those weights is 85.  Thus, the answer is between 31 (the maximum weight of any one shift) and 85 (the sum of the weights of all the shifts).  These values will be referred to as `low` and `high`, respectively: $low=31$ and $high=85$.

A binary search takes a sorted array, and looks at the middle value to see how it compares to the value being searched for.  Assuming it isn't that value, the algorithm either looks in the upper half or the lower half, depending on the result of that comparison.

The algorithm for this problem is going to do a binary search on the *allowed total weight* until we find the minimum allowed total weight that allows $k$ TAs (here, $k=3$) to staff those shifts.  We already know, from above, that the answer to this example is 34.  We know that the minimum total weight is 31 and the maximum is 85, so those are the initial bounds of our binary search.  The middle of those two values, then, is $(31+85)/2=58$, which is our first take at the allowed total weight.  The first iteration will determine if 3 TAs can staff those shifts when the allowed total weight of any TA is 58 (see below for how).  

- If 3 TAs *can* staff those shifts when the allowed total weight is 58 or less, then that value (of 58) is a potential answer for the allowed total weight, but it could be lower -- in this example, we know the final answer is 34, so the value is actually lower in this case.  Thus, we would search in the lower half of the results (31-58), and we would include the current value (of 58) in that search.
- If 3 TAs can *NOT* staff those shifts -- we would need 4 or more TAs, for example -- then the current allowed total weight is too low, and we have to search for a higher allowed total weight.  We would then search in the upper half (59-85).

Thus, we are binary searching on the *allowed total weight*, not on an array of values.

The last problem is how to count how many TAs can staff a given shift.  If we know the allowed total weight that we are considering, we just keep adding consecutive shifts until the next one would cause us to go over, and then we proceed onto the next TA.  For the shifts above, if the allowed total weight being considered is 58, then we would add up $8+12+31=51$ (as adding the next shift, with weight 19, would go over 58) for the first TA, and $19+15=34$ for the second TA.  Thus, with an allowed total weight of 58, we only need 2 TAs.


### Requirements

***This must be a divide-and-conquer solution!***  To ensure this, we have a few test cases that will cause all other potential solutions to either time out or cause a stack overflow due to recursion depth.  One such test case has one thousand TAs and one million shifts, and is available in Canvas's files (named `pa2-example-1M.in`, but stored in a .zip file named `pa2-example-1M.in.zip`).  The output from that test case is 500,814.

There are some assumptions that you may and may not make:

- All shift weights are positive integer (`long`) values
- The input provided will always be valid
- The values in the array, as well as the answer, may not fit in a `int` variable, but will fit into a signed `long` variable
- There will be at least 2 shifts and at least 2 TAs
- There will never be more TAs than shifts


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

You will submit your completed `pa2.py` or `PA2.java` file to Gradescope.  There will be a *small set* of acceptance tests that are *NOT COMPREHENSIVE*.  These acceptance tests are the test cases in [example.in](example.in) file.  It's up to you to comprehensively test your code.  The acceptance tests just verify that you are reading the input correctly and providing the expected output.
