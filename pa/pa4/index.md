---
title: "PA4: Water Drainage"
---

<a href="..."><img src="https://upload.wikimedia.org/wikipedia/commons/e/e3/A_stream_on_a_track_between_Sabine_Hut_and_Speargrass_Hut%2C_Nelson_Lakes_National_Park%2C_New_Zealand.jpg" style="float:right;max-width:40vw;border-radius:40px;margin-left:10px;width:500px"></a>

You decide to give up computer science, and instead pursue a career in environmental engineering. Fortunately, your algorithmic skills still prove useful! Your first assignment is to model water runoff — or *drainage* — across a terrain. The terrain is represented as a two-dimensional grid of elevations. Water flows across this landscape according to strict physical rules, and your task is to determine how far it can travel.

You are given:

- A set of terrain grids, each with a unique title
- Each grid has $r$ rows and $c$ columns
- Each cell contains an integer elevation

Water flows according to the following rules:

- Water flows only from **higher elevation to lower elevation**
- Water **cannot** flow to equal elevation
- Water **cannot** flow uphill
- Water can only move to **adjacent cells** (up, down, left, right (no diagonals))

Your goal is to determine the **length of the longest possible drainage path** in each grid.

---

### Example

Consider the following $5 \times 5$ grid:

```
66 78 41 3 77
4 90 41 8 68
12 11 29 24 53
0 51 58 9 28
97 99 96 58 92
```

There are many valid drainage paths. For example:

- One path starts at 90 and flows: `90 - 78 - 41 - 3`
- Note that `90 - 41 - 41 - 3` is **invalid**, since water cannot flow between equal elevations

The **longest drainage path** in this grid has length **7**:

```
99 - 96 - 58 - 29 - 24 - 8 - 3
```

---

### Theory

This problem ***MUST*** be solved using **dynamic programming**. A brute-force solution (recursive or otherwise) will not complete in time for large inputs.

---

### Input

The input begins with a single integer:

- $1 \le t \le 100$: the number of test cases

Each test case consists of:

- A single line containing:
	- A title string (no spaces or punctuation)
 	- Two integers $r$ and $c$ ($1 \le r, c \le 100$)

- Followed by $r$ lines, each containing $c$ integers:
	- Each integer represents a height between $0$ and $100$

---

### Output

For each test case, output a single line:

```
<city>: <length>
```

Where:

* `<city>` is the name of the test case
* `<length>` is the length of the longest drainage path

---

### Sample Input

```
4
Charlottesville 5 5
66 78 41 3 77
4 90 41 8 68
12 11 29 24 53
0 51 58 9 28
97 99 96 58 92
Richmond 3 3
1 1 1
1 1 1
1 1 1
WashingtonDC 5 5
10 81 28 2 49
64 59 61 85 82
77 14 81 6 76
37 86 99 11 92
85 95 78 13 57
Wintergreen 5 5
1 2 3 4 5
10 9 8 7 6
11 12 13 14 15
20 19 18 17 16
21 22 23 24 25
```

---

### Sample Output

```
Charlottesville: 7
Richmond: 1
WashingtonDC: 5
Wintergreen: 25
```

---

### Hints

- Think about defining a subproblem for each grid cell:
	- What is the longest path starting (or ending) at this cell?
- Use memoization (top-down) or tabulation (bottom-up)
- Each cell depends on its neighbors in some way

---

### Submission

The submission system can handle four different programming languages.  For each programming language, the name of the submitted file is listed below -- you have to have it named that exact name, else it will not compile properly.  If you want to program in a different language, email the course email at least three days before it is due, as we have to reconfigure the submission system to handle that language.

- Python 3: pa4.py
- Java: PA4.java
- C: pa4.c
- C++: pa4.cpp

You will submit your completed source code file to Gradescope.  There will be a *small set* of acceptance tests that are ***NOT COMPREHENSIVE***.  These acceptance tests are the test cases in the [example.in](example.in) file.  It's up to you to comprehensively test your code.  The acceptance tests just verify that you are reading the input correctly and providing the expected output.

Note that when you submit, Gradescope will report your grade as "-/10" or "0/10" -- that's a quirk of Gradescope, and is because the grading tests have not been run (and won't be run until after all submissions are in).  YOu can look at the results of the individual test cases to see how your program worked.
