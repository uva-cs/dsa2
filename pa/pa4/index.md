---
title: "DSA2: PA4: Mixing Magical Reagents"
---

![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Arthur-Pyle_The_Enchanter_Merlin.JPG/892px-Arthur-Pyle_The_Enchanter_Merlin.JPG){style="width:25%;float:right;margin-left:20px;border-radius:10px"}

It's course registration time!  While choosing electives, you came across a rather interesting one -- *Mixing Magical Reagents (and Computing)*, taught by "Staff" -- meaning someone yet to be hired.  Somehow this course counts as a computing elective.  Curious to learn more, you sign up for the course.  Like all CS electives, the wait list size is already larger than the number of people enrolled -- many times larger, in fact.  But somehow you end up in the course, and quickly find out that it is more similar to a chemistry mixing free-for-all than an actual computing elective.  The first assignment in that class is how to optimize the mixing of magical reagents -- the physical components needed to cast spells.

You find that you have $r$ unique reagents that are available to be used for the mixings, where $2 \le r \le 26$.  We will represent these reagents here as lower-case letters 'a' through 'z'.  You will be given a *reagent string* such as `abc`, which might mean to mix **A**shes of mistletoe with **B**one dust with a caterpillar **C**ocoon.  Reagent strings can be as long as $10^3$ characters, but will only use the $r$ unique reagents (letters) available.  You can mix only two reagents together at a time, so you can either mix the first two and add the third, or mix the second two, and then add that to the first.  Effectively, you can choose to perform either $(a+b)+c$ or $a+(b+c)$.

Mixing reagents uses some magical energy -- a cost, if you will.  Each pair of reagents has a separate cost, and that cost varies depending on the order that you mix them together.  So the cost adding $b$ to $a$ (i.e., $a+b$) can have a different cost than the cost of adding $a$ to $b$ (i.e., $b+a$).  Furthermore, mixing two reagents yields a third reagent -- this is magic, after all.  That third reagent will always be one of the $r$ unique reagents available.  Like with the energy cost, the resulting reagent will vary depending on the order.  So $a+b=a$, but $b+a=c$, for example.

You will be provided with a table that lists both the cost of mixing two reagents, as well as the resulting reagent:

| | a | b | c |
|----|----|----|----|
| a | c:10 | a:4 | a:4 |
| b | c:3 | a:4 | a:2 |
| c | b:4 | b:1 | b:8 |

This means that mixing b+c will yield reagent a, and cost 2 energy.  Mixing c+b will yield reagent b, and cost 1 energy.  Thus, the mixing of reagents is not commutative: $c+b \ne b+c$.  In that table, the letter in the left-hand column is the left hand side of the '+' operation, and the letter in the top top row is the right-hand side of the operation.  Thus, $a+b=a$ and $b+a=c$.

Given a table in a format similar to what is above, and a list of reagents to mix, you have to determine the mixing order that minimizes the cost, as well as the resulting reagent.  You cannot change the order of the reagents in the reagent string, only change the order of which ones you mix first.  In other words, given the reagent string `abc` as your mixing string, you have to determine which is the minimum cost between $(a+b)+c$ and $a+(b+c)$, but you cannot choose $c+(b+a)$, as that changes the order of the reagent string.


### Input

The first line of the input contains an integer $1 \le t \le 10^3$, the number of test cases.

The first line of each test case contains an integer $2 \le r \le 26$, the number of reagents in this test case.  The reagents always start at lower-case 'a' and proceed sequentially through the alphabet (in order).

The next $r$ lines will contain the table.  Each line will contain $r$ pairs; each pair contains the resulting reagent and the cost.  The values in a pair are colon-separated, and the pairs themselves are space separated.  If $r=3$, an example line would be `c:3 a:4 a:2` (the middle row in the table above).  All costs are integers $1 \le c \le 10$.  The resulting reagents will always be one of the $r$ reagents in this test case -- meaning if there are only 5 reagents in a test case, which would be 'a' through 'e', you will not get a mixing that yields any reagents 'f' through 'z'.

After the table is an integer $1 \le m \le 10^3$, the number of mixings of reagents to determine the minimum cost for.  Each such mixing will use the same table, as it is in the same test case.  The next $m$ lines will contain one reagent string per line; each string will be up to $10^3$ reagent letters, and will only contain the letters corresponding to the $r$ reagents available in this test case.

All input is to be read from standard input.


### Output

For each mixing in each test case, there should be two values output on a single line (space separated): the resulting reagent and the minimal cost.  If there are multiple paths that lead to the same minimum cost, you may print out the resulting reagent from any of them.  These minimal costs -- and all partial costs computed in the process -- are guaranteed to fit into a 32-bit singed integer.

All input is to be written to standard output.


### Sample input

This input below is available in the [sample.in](sample.in) file.  The first test case therein corresponds to the example above.

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

Your program will be run as follows, if in Python:

```
$ python pa4.py < sample.in
```

Or, if in Java:

```
$ java PA4 < sample.in
```

The `<` will provide the contents of the [sample.in](sample.in) file as standard input to your program.

### Sample output


```
a 6
a 8
a 30
b 11
```

### Requirements

This needs to be a dynamic programming solution.  Brute force solutions will time out with the test cases we are going to provide.

There is no skeleton code being provided for this programming assignment.  You can look at [PA2](../pa2/index.html) for how to read in the input from standard input (but note that the input for this assignment is quite different than that for PA2).

Your source code file must be named either `pa4.py` or `PA4.java`.
