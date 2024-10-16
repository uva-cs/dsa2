---
title: "DSA2: PA2: Messy Bookshelves"
---

![](https://webstockreview.net/images/bookshelf-clipart-messy-6.jpg){style="height:400px;float:right;margin-left:20px;margin-bottom:20px"}

Professor Pettit's children have to help clean the house once a week.  One of their jobs is to neatly put the books back on the bookshelf.  But, alas, being children, they often just throw them on the bookshelf in any order.  This makes the bookshelf look quite messy.  And that type of messiness is not allowed in the house!

In an effort to determine just *how* messy the book's ordering is, Professor Pettit has numbered each book.  The books should be in (ascending) sorted order.  To see how messy the bookshelf is, one has to count how many, of all possible pairings of books, are out of order (meaning a higher numbered book is before (to the left of) a lower numbered book).

Your job is to write a program to help Professor Pettit determine just how messy his bookshelf is.



### Input

The first line of the input will contain an integer $n$, will be the number of test cases in the input.  Each test case consists of exactly two lines.  The first line contains the integer number of books, $b$.  The second line of each test case will contain $b$ integers, space separated, which is the order the books appear on the shelf.  The $b$ book numbers will always be 1 to $b$, with no duplicates of the same book number for a given test case.

All input is provided via standard input.


### Output

The output is a single integer per test case, which is how many book pairs are out of ascending sorted order.  For any positions $i$ and $j$, such that $i < j$, let $b_i$ and $b_j$ represent the books at positions $i$ and $j$.  If $b_i > b_j$, then that book pair is out of order.  Recall that you are guaranteed that $b_i \ne b_j$ as long as $i \ne j$.  

The output, per test case, is the total number of book pairs that are out of order.

All output is to be printed to standard output.

### Requirements

This can be done via two nested for loops, but that yields a $\Theta(n^2)$ algorithm.  Your algorithm must be a **divide and conquer** algorithm, as discussed in class -- we are going to check this.  You cannot use parallelization -- your program will be limited to one thread/process.

Your algorithm must run in $\Theta(n\ \log n)$ time.  We are going to check this with a *very* large test case provided via standard input.  If your algorithm is not $O(n\ \log n)$, Gradescope will time out on your submission.

**You will need to name your recursive function `solve()` (not `Solve()`, not `solver()`, not anything else).**

**You will need to use a `long` counter for this program if using Java, as there may be more than 2^32 (the number of values in a 32-bit integer) book pairs that are out-of-order.**

### Example Input

```
2
4
4 3 2 1
3
1 3 2
```

This input can be found in the [sample.in](sample.in) file.

### Example Output

```
6
1
```

### Skeleton Code

We have provided skeleton code for this assignment.  This code only shows how to read in the input; you have to add the rest.

- [pa2-skeleton.py](pa2-skeleton.py.html) ([src](pa2-skeleton.py))
- [PA2Skeleton.java](PA2Skeleton.java.html) ([src](PA2Skeleton.java))

You will have to rename them to pa2.py or PA2.java prior to submission.  You can run your program as such:

```
$ python3 pa2.py < sample.in
6
1
$ javac PA2.java
$ java PA2 < sample.in
6
1
$
```




