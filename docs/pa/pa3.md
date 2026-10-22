---
layout: default 
title: "PA3: PHP2Shell Intrusion Monitoring"
nav_order: 3
parent: Programming Assignments
---

### Introduction

<img src="https://thumb.wikimedia.org/wikipedia/commons/thumb/3/32/Wikimedia_Phabricator_PHP2Shell.png/960px-Wikimedia_Phabricator_PHP2Shell.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail" style="float:right;max-width:40vw;border-radius:40px;padding-left:10px;border:3px solid black">

The cybersecurity world is in a panic! A new vulnerability, known as [PHP2Shell](https://en.wikipedia.org/wiki/PHP2Shell), has just been discovered in PHP, the programming language used by a large percentage of websites worldwide. This vulnerability can allow attackers to remotely execute malicious code on vulnerable web servers, potentially stealing sensitive information, taking control of servers, or causing widespread disruptions.

Naturally, hackers around the world have wasted no time attempting to exploit this vulnerability.

You are part of a cybersecurity team responsible for monitoring a large network of web servers. Your team has deployed several intrusion detection systems (IDS), each of which monitors network traffic for suspicious activity. Whenever one of these systems detects a possible attack, it records the time when the suspicious activity began and the time when it ended.

Unfortunately, your intrusion detection systems are a bit overzealous. Different systems may detect the same attack, or they may detect different attacks occurring simultaneously. As a result, their reports frequently contain overlapping time intervals.

Your team needs to combine these reports into a single timeline showing all periods during which at least one intrusion detection system observed suspicious activity.

For example, suppose three intrusion detection systems report the following:

- IDS A detects suspicious activity from time 6 to time 9.
- IDS B detects suspicious activity from time 8 to time 12.
- IDS C detects suspicious activity from time 15 to time 20.

Because the first two reports overlap, they can be combined into a single period of suspicious activity from time 6 to time 12. The third report remains separate.

Thus, the final timeline would contain two intervals: 6-12 and 15-20.

To simplify the problem, we will represent all times as non-negative integers. Each intrusion detection report consists of two integers representing the start and end times of the suspicious activity.  Note that two intervals that share an endpoint are considered overlapping. For example, reports covering times 1–3 and 3–5 combine into a single interval of 1–5, since suspicious activity was detected continuously throughout that period.  However, reports covering times 1–3 and 4–6 do not overlap, since there was a period between times 3 and 4 when no suspicious activity was detected.

Your task is to develop a **greedy algorithm** that combines all intrusion detection reports into a minimal set of non-overlapping intervals representing the periods during which suspicious activity was observed.

Your algorithm must run in $\Theta(n \log n)$ time, where n is the number of intrusion detection reports.

The cybersecurity team is counting on you. The hackers certainly aren't going to wait for your algorithm to finish!

### Changelog

Any changes to this page will be put here for easy reference.  Typo fixes and minor clarifications are not listed here.  So far there aren't any significant changes to report.


### Input format

**For this homework, we are *NOT* providing you with skeleton code that handles reading in of the input.**  You should look at the previous two homeworks for examples how to do so: [PA1: Aircraft Loading](pa1.html) and [PA2: Snow Plows](pa2.html).


All input is read in from standard input (not a file).

The first line of the file will contain the single positive integer $1 \le c \le 10^5$, the number of test cases in the file.

Each test case will start with a line containing a single positive integer $1 \le r \le 10^9$, which is the number of shift requests in the file.  The next $r$ lines will consist of a single ordered pair each, the start and end times of each shift request.  A shift request is two integers $(0 \le s \le 10^9, 0 \le t \le 10^9)$, with $t > s$, the start time ($s$) and end (terminating) time ($t$) of the shift request.  These two values are space separated.

All input values will fit into a signed `int` variable.


### Output format

**The output format is very precise.  Extra spaces, extra lines, or different punctuation will cause the answer to be judged as incorrect.**

Each test case will output a single line that contains all of the combined shifts, in `x-y` form (a dash between the start and end times), with each range separated by a comma and a space.  The example above would have the output: `1-4, 8-10`.

All output values will fit into a signed `int` variable.

### Example input

This file is available as [pa3-example.in](pa3-example.in).

```
4
3
1 3
2 4
8 10
5
1 3
3 5
7 9
8 12
15 18
6
10 20
12 15
2 5
4 8
25 30
28 35
4
1 2
4 5
7 8
10 11
```

### Example output

This file is available as [pa3-example.out](pa3-example.out).

```
1-4, 8-10
1-5, 7-12, 15-18
2-8, 10-20, 25-35
1-2, 4-5, 7-8, 10-11
```

### Notes

This assignment must be a *greedy solution*.  Specifically, it needs to be a $\Theta(n \log n)$ solution.  A $\Theta(n^2)$ solution will time out with larger test cases.  To ensure this, we have a few test cases that will cause all $\omega(n \log n)$ solutions to time out.  Some of those test cases are given below.

There are some assumptions that you may and may not make:

- All values, both input and output, are non-negative integer values that will fit into a signed `int` variable
- The input provided will always be valid
- There will be at least one shift request in each test case
- The end time for a shift request will always be strictly greater than the start time of that shift request


There are two large test cases available in Canvas' Files.  They are contained in a zip file named `pa3-large-test-cases.zip`.  The files therein are:

- `pa3-example-1M.in`: this has 1 million randomly generated shifts.  The solution for this problem is: `203-2749560, 2749679-28174283, 28174585-55062652, 55062880-67614733, 67614807-78848447, 78848508-100000000`
- `pa3-example-1M-exclusive.in`: this has 1 million shifts are are all mutually exclusive (there is no overlap).  The solution will be 1 million ranges, that will start with: `0-1, 2-3, 4-5, 6-7, 8-9, 10-11, ..., 1999994-1999995, 1999996-1999997, 1999998-1999999`

If your program does not implement a greedy algorithm, at least one of those cases will time out when we run it.

### Execution

We will run your program as follows:

```
cat pa3-example.in | python3 pa3.py
```

or:

```
cat pa3-example.in | java PA3
```

This takes the output of what is on the left (`cat pa3-example.in`, whose output is the contents of the pa3-example.in file) and uses it as the input to what is on the right.  This version should work in all platforms (Windows, MacOS, and Linux).

### Submission

You will submit your completed `pa3.py` or `PA3.java` file to Gradescope.  There will be a *small set* of acceptance tests that are *NOT COMPREHENSIVE*.  These acceptance tests are the test cases in [pa3-example.in](pa3-example.in) file.  It's up to you to comprehensively test your code.  The acceptance tests just verify that you are reading the input correctly and providing the expected output.
