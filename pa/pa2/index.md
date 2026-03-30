---
title: "PA2: Sorting Train Cars"
---

<a href="..."><img src="http://images.fineartamerica.com/images-medium-large-5/corwith-intermodal-rail-yard-chicago-steve-gadomski.jpg" style="float:right;max-width:40vw;border-radius:40px;margin-left:10px"></a>


You have been hired by a train yard to help get their train cars in order.  Delivery freight trains leave the train yard for a route with a number of destination factories.  At each stop the train detaches the appropriate cars -- dropping them off -- so that the train does not have to wait while the destination factory unpacks the cars.  On the return trip, the train picks up all the cars to return to the train yard.  

To make this work efficiently, the first destination must have their trains at the end, so they can quickly be detached and the train can then move onward.  Similarly, the second destination must have their trains just in front of those.  The last destination must have their cars right behind the locomotive.

The problem is that when the train comes into the yard, the cars are not in the proper order.  The task of the yard is to re-arrange the train cars so that they are in the necessary order for delivery.  The train yard gets to bill for how out of order a car is on the incoming train.

Your task is to help the train yard figure this out.  Given a list of train cars, and a required order, determine how out of order the train cars are.  To make this problem easier, each of the $n$ trains car will have a unique integer that indicates its order -- car 0 is right behind the locomotive, and car $n-1$ is at the very back.  Here, "out of order" means one or more higher numbered cars are in front of a lowered number car.


This ***MUST*** be a divde-and-conquer algorithm.  It must run in $\Theta(n \log n)$ time, else it will timeout with some of the grading execution runs.


### Example

Consider a train with 4 cars numbered 0 through 3 (the locomotive is in front of car 0).  The expected order, of course, is:

| 0 | 1 | 2 | 3 |
|---|---|---|---|

The locomotive is to the left of car 0, and the rear of the train is to the right in that diagram.  In this correct ordering, no car has a higher-numbered car to its left -- all the higher numbered cars are to its right.

But the order they arrive is:

| 0 | 3 | 2 | 1 |
|---|---|---|---|

And "out of order" car means that one or more higher numbered cars are in front of (to the left of) a lowered number car.  To determine how many cars are out of order:

- Car 0 has no higher-numbered cars to its left
- Car 1 has two higher-numbered cars to its left
- Car 2 has one higher-numbered car to its left
- Car 3 has no higher numbered cars (and thus no higher-numbered cars to its left)

This case would have three mis-orderings.

### Input

An input file will start with a line containing a single integer $1 \le t \le 10^5$, which is the number of test cases in the file.

Each of the $t$ test cases will be on exactly one line.  The first value on the line will have $n$, the number of cars in that train.  The next $1 \le n \le 2**31$ values will be the order of the train cars; these are all unique integers from $0$ to $n-1$.  All values on this line will be space separated

All input is provided via standard input.  All values will fit into a 32-bit singed integer (i.e., a standard `int` variable).



### Output

Each test case will output a single integer variable, on its own line, which is the number of mis-orderings of the incoming train.

All output is to be printed to standard output.

### Sample Input

This input is available as [example.in](example.in).  The first test case is the example shown above.

```
4
4 0 3 2 1
5 4 0 3 1 2
10 5 2 7 1 8 4 3 6 0 9
40 35 8 9 26 6 3 39 28 32 23 22 14 24 33 18 19 12 21 4 34 37 11 7 38 10 15 16 1 5 25 20 17 31 29 13 0 30 27 2 36
```


### Sample Output

This output is available as [example.out](example.out).


```
3
6
21
407
```

### Requirements

This can be done via two nested for loops, but that yields a $\Theta(n^2)$ algorithm.  Your algorithm must be a **divide and conquer** algorithm, as discussed in class -- we are going to check this.  You cannot use parallelization -- your program will be limited to one thread/process.

Your algorithm must run in $\Theta(n\ \log n)$ time.  We are going to check this with a *very* large test case provided via standard input.  If your algorithm is not $O(n\ \log n)$, Gradescope will time out on your submission.

**You will need to name your recursive function `solve()` (not `Solve()`, not `solver()`, not anything else).**

We are NOT providing skeleton code to read in the input.  You can look at the skeleton code from [PA1](../pa1/index.html), if that would help.

### Submission

The submission system can handle four different programming languages.  For each programming language, the name of the submitted file is listed below -- you have to have it named that exact name, else it will not compile properly.  If you want to program in a different language, email the course email at least three days before it is due, as we have to reconfigure the submission system to handle that language.

- Python 3: pa2.py
- Java: PA2.java
- C: pa2.c
- C++: pa2.cpp

You will submit your completed source code file to Gradescope.  There will be a *small set* of acceptance tests that are ***NOT COMPREHENSIVE***.  These acceptance tests are the test cases in the [example.in](example.in) file.  It's up to you to comprehensively test your code.  The acceptance tests just verify that you are reading the input correctly and providing the expected output.

Note that when you submit, Gradescope will report your grade as "-/10" or "0/10" -- that's a quirk of Gradescope, and is because the grading tests have not been run (and won't be run until after all submissions are in).  YOu can look at the results of the individual test cases to see how your program worked.
