---
title: "DSA2: PA3: Weighing Children"
---

![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/HK_%E8%A5%BF%E7%87%9F%E7%9B%A4_Sai_Ying_Pun_Dr_doctor_clinic_shop_January_2021_SS2_03.jpg/1024px-HK_%E8%A5%BF%E7%87%9F%E7%9B%A4_Sai_Ying_Pun_Dr_doctor_clinic_shop_January_2021_SS2_03.jpg){style="width:33%;float:right;margin-left:20px;border-radius:10px"}

Professor Pettit is bringing his children to their annual pediatrician's appointment.  As always, they are weighted and measured to check their growth.  Normally a scale like the one to the right is used -- a weigh-beam scale, it's called.  However, the scale at Pediatrics Incorporated is broken, and they have to use a different means to weigh each of his children.

The only tools available are an old-fashioned [balance scale](https://commons.wikimedia.org/wiki/File:Balance_scale_IMGP9722.jpg) and a number of boxes of standard kilogram weights, which are all in powers of 10.  We'll assume that Professor Pettit knows the weight of each child, and the physician just has to go through the motions to verify it.

Thus, the pediatrician needs to weigh a child weighing $m$ kilograms by balancing the child on a balance scale with weights of standard masses on the other side that are all powers of 10 (1 kg weights, 10 kg weights, 100 kg weights, etc.). Thus, the pediatrician has to choose a set of standard weights with total sum equal to $m$ kg.

Standard weights come in $b$ sealed boxes. A given box contains some number of identical mass weights of $10^{x}$ kg. The pediatrician wants to open the minimal number of boxes to take a set of weights with the sum of their weights of $m$ kg.

The goal is to minimize the number of (sealed) boxes that need to be opened.

Consider the following example, where the pediatrician wants to measure out 176 kg (no, none of Professor Pettit's children weigh 176 kg, which is 387 lbs).  There are five boxes of weights available:

<br clear='all'>

![](pa3.svg)

There are a few possible solutions.  In both solutions discussed here, the box of 100 kg weights and the box of 1 kg weights have to be opened.  In the first solution, the box of 8 x 10 kg weights is opened, leading to a result of 3 boxes (box numbers 1, 3, and 5).  The second solution is to open both the 5 x 10 kg weights box and the 3 x 10 kg weights box, leading to 4 boxes being opened.  (There are technically other solutions where you open the 8 x 10 kg box and one or both of the others, but we'll ignore those).  The first solution is the optimal one, as it opens the fewest number of boxes.  The greyed boxes are the ones that have to be opened, and the greyed weights are the ones that sum to 176 kg.

Note: you may not use a weight of a given power of 10 if there is a zero value in that digit's position.  For example, if the weight is 201 kg, you cannot use any 10 kg weights, since there is a 0 digit in the 10's place.  (The reason is that otherwise this becomes a dynamic programming problem without a greedy solution).

### Input

The first line of the input contains $1 \le c \le 10^3$, the number of test cases.

The first line of each test case contains two positive integers: $1 \le m \le 10^{18}$, the number of kg to measure out, and $1 \le b \le 10^5$, the number of sealed boxes. The next $b$ lines contain pairs of positive integers $0 \le k_i \le 18$, the weight of the masses in that box as an exponent of 10, and $q_i$, the number of such weights in the box.  Note that $1 \le q_i \cdot 10^{k_i} \le 10^{18}$.  The boxes may be listed in any order.  Not all exponent values of 10 may be present.

### Output

On the first line output the minimal number of boxes that should be opened. On the second line output the numbers of these boxes in *ascending sorted* order. Boxes are numbered in the order they appear in the input file starting from 1 (not 0!). If there are multiple possible optimal solutions, any one will suffice.  

If it is impossible to measure exactly $m$ kg with the provided boxes of weights, output a single line with -1.

### Sample input

The first test case corresponds to the diagram above.  The blank lines are only present to separate test cases for easy viewing; they will not be present in the actual input, and are not present in the [sample.in](sample.in) file.

```
5

176 5
2 4
1 5
1 8
1 3
0 25

40 3
2 3
1 6
0 30

5550 3
3 5
2 5
1 99999

5500 3
3 5
2 5
1 99999

87 1
1 9
```

Note that the third and fourth test cases are rather tricky, so focus on getting the others to work first.

Your program will be run as follows (if in Python):

```
$ python pa3.py < sample.in
```

Or, if Java:

```
$ java PA3 < sample.in
```

The `<` will provide the contents of the [sample.in](sample.in) file as standard input to your program.

### Sample output

There should NOT be blank lines between test cases -- that is only to help illustrate which values are the output for which test cases.  The blank lines are not present in the [sample.out](sample.out) file.

```
3
1 3 5

1
2

1
3

2
1 2

-1
```

### Requirements

This needs to be a greedy solution.  Brute force solutions will time out with the test cases we are going to provide.

There is no skeleton code being provided for this (or future) programming assignments.  You can look at [PA2](../pa2/index.html) for how to read in the input from standard input (but note that the input for this assignment is quite different than for PA2).

Your source code file must be named either `pa3.py` or `PA3.java`.
