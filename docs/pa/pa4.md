---
layout: default 
title: "DSA2: PA4: Compiler Instruction Optimization"
nav_order: 4
parent: Programming Assignments
---

### Introduction

<img src="https://thumb.wikimedia.org/wikipedia/commons/thumb/0/0d/2023_Intel_Core_i7_12700KF_%284%29.jpg/1280px-2023_Intel_Core_i7_12700KF_%284%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail&_=20230315192237" style="float:right;max-width:40vw;border-radius:40px;padding-left:10px;border:3px solid black">

While browsing job postings for summer internships, you come across an interesting opportunity at a startup developing a revolutionary new processor architecture. The company claims that its processors will be faster, more energy-efficient, and cheaper than anything currently on the market. The only problem is that nobody has written a compiler for them yet. Naturally, they have decided that this is the perfect job for an undergraduate intern.

You apply for the position, and somehow get hired. On your first day, you discover that the processor's instruction set was designed by a team of hardware engineers who apparently never consulted anyone who has actually written a compiler. The processor supports a rather unusual feature called instruction fusion, where two instructions can be combined into a single instruction. Your task is to optimize this process so that programs execute as efficiently as possible.

The processor supports $r$ unique instruction types, where $2 \le r \le 26$. We will represent these instruction types using lowercase letters `a` through `z`. You will be given an instruction string, such as `abc`, representing a sequence of three instructions that need to be executed.

The processor can fuse only two instructions together at a time. Thus, for the instruction string `abc`, you can either fuse the first two instructions and then fuse the result with the third, or fuse the last two instructions and then fuse the result with the first. Effectively, you can choose to perform either $(a + b) + c$ or $a + (b + c)$.

Fusing instructions requires computational resources, which we will represent as a cost. Each pair of instruction types has a separate fusion cost, and that cost depends on the order in which the instructions appear. Thus, fusing instruction $a$ with instruction $b$ (i.e., $a + b$) may have a different cost than fusing instruction $b$ with instruction $a$ (i.e., $b + a$).

Furthermore, fusing two instructions produces a new instruction, which will always be one of the $r$ instruction types supported by the processor. The resulting instruction type also depends on the order of the inputs. For example, $a + b$ might produce instruction $a$, while $b + a$ might produce instruction $c$. Apparently, the hardware engineers thought this was a perfectly reasonable design decision.

You will be provided with a table that specifies both the cost of fusing two instructions and the resulting instruction type:

| | a | b | c |
|----|----|----|----|
| a | c:10 | a:4 | a:4 |
| b | c:3 | a:4 | a:2 |
| c | b:4 | b:1 | b:8 |

This means that fusing instruction $b$ with instruction $c$ produces instruction $a$ at a cost of 2, while fusing instruction $c$ with instruction $b$ produces instruction $b$ at a cost of 1. In the table, the instruction in the left-hand column is the left operand of the fusion operation, and the instruction in the top row is the right operand.

There is, of course, one additional complication. The compiler must preserve the original order of instructions in the program. After all, executing instructions in a different order could cause the program to produce incorrect results, which the hardware engineers assure you would be a minor inconvenience. You may change the order in which adjacent instructions are fused, but you cannot rearrange the instructions themselves.

For example, given the instruction string `abc`, you must determine which of $(a + b) + c$ and $a + (b + c)$ has the lower total cost. You cannot choose $c + (b + a)$, because that would change the original instruction order.

Your task is to write the instruction fusion optimizer for this new compiler. Given a table of fusion costs and resulting instruction types, along with a sequence of instructions, determine the fusion order that minimizes the total cost. You must also determine the type of the final fused instruction.

The startup's investors are expecting a demonstration next week, and the hardware engineers have already promised that your compiler will be ready. No pressure!

### Input

The first line of the input contains an integer $1 \le t \le 10^3$, the number of test cases.

The first line of each test case contains an integer $2 \le r \le 26$, the number of instructions in this test case.  The instructions always start at lower-case `a` and proceed sequentially through the alphabet (in order).

The next $r$ lines will contain the table.  Each line will contain $r$ pairs; each pair contains the resulting reagent and the cost.  The values in a pair are colon-separated, and the pairs themselves are space separated.  If $r=3$, an example line would be `c:3 a:4 a:2` (the middle row in the table above).  All costs are integers $1 \le c \le 10$.  The resulting instructions will always be one of the $r$ instructions in this test case -- meaning if there are only 5 instructions in a test case, which would be `a` through `e`, you will not get a mixing that yields any instructions `f` through `z`.

After the table is an integer $1 \le m \le 10^3$, the number of mixings of instructions to determine the minimum cost for.  Each such mixing will use the same table, as it is in the same test case.  The next $m$ lines will contain one reagent string per line; each string will be up to $10^3$ reagent letters, and will only contain the letters corresponding to the $r$ instructions available in this test case.

All input is to be read from standard input.


### Output

For each mixing in each test case, there should be two values output on a single line (space separated): the resulting reagent and the minimal cost.  If there are multiple paths that lead to the same minimum cost, you may print out the resulting reagent from any of them.  These minimal costs -- and all partial costs computed in the process -- are guaranteed to fit into a 32-bit singed integer.

All input is to be written to standard output.


### Sample input

This input below is available in the [pa4-example.in](files/pa4-example.in) file.  The first test case therein corresponds to the example above.

```
2
3
c:10 a:4 a:4
c:3 a:4 c:2
b:4 b:1 b:8
3
abc
cab
abcabcabcabc
2
b:3 b:5
a:6 b:2
1
abba
```

### Sample output

This input below is available in the [pa4-example.out](files/pa4-example.out) file.  The first test case therein corresponds to the example above.

```
a 6
a 8
a 30
b 11
```

Note that the second test case (`cab`) could have also output `b 8`, as doing the two operations in either order yields a cost of 8.  In other words, $c+(a+b)=b$ and $(c+a)+b=a$ both have a cost 8, and either answer is acceptable. 

### Requirements

This needs to be a dynamic programming solution.  Brute force solutions will time out with the test cases we are going to provide.

There is no skeleton code being provided for this programming assignment.  You can look at [PA2](pa2.html) for how to read in the input from standard input (but note that the input for this assignment is quite different than that for PA2).

Your source code file must be named either `pa4.py` or `PA4.java`.

### Execution

We will run your program as follows:

```
cat pa4-example.in | python3 pa4.py
```

or:

```
cat pa4-example.in | java PA4
```

This takes the output of what is on the left (`cat pa4-example.in`, whose output is the contents of the [pa4-example.in](files/pa4-example.in) file) and uses it as the input to what is on the right.  This version should work in all platforms (Windows, MacOS, and Linux).

### Submission

You will submit your completed `pa4.py` or `PA3.java` file to Gradescope.  There will be a *small set* of acceptance tests that are *NOT COMPREHENSIVE*.  These acceptance tests are the test cases in [pa4-example.in](files/pa4-example.in) file.  It's up to you to comprehensively test your code.  The acceptance tests just verify that you are reading the input correctly and providing the expected output.
aaron@d
