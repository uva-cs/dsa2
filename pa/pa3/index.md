---
title: "PA3: Zombie Containment"
---

<a href="..."><img src="https://upload.wikimedia.org/wikipedia/en/c/c6/The_Night_King_at_Hardhome.jpg" style="float:right;max-width:40vw;border-radius:40px;margin-left:10px;width:500px"></a>

The situation has gotten a little out of hand.

After a mysterious outbreak, the city has been overrun with zombies. Emergency containment teams have managed to isolate the infected within a large quarantine zone, but there are still far too many roaming around. For research purposes, the scientists studying the outbreak need a small number of zombies to remain intact, but the rest must be eliminated as quickly and cheaply as possible.

Several containment companies have offered their services. Each company provides two methods for dealing with zombies:

- They can neutralize a single zombie using standard equipment.
- They can deploy a containment gas device that spreads through the area and eliminates about half of the zombies at once. For simplicity, we will assume it always rounds in favor of eliminating more zombies.  For example, if there are 9 zombies, the device will remove 5.

You currently have $x$ zombies trapped in the containment zone, and researchers require exactly $y$ zombies to remain for study. Your task is to determine the minimum cost each company would charge to reduce the zombie population from $x$ down to $y$, using any sequence of the two available operations.

Once you determine the cost for each company, you must list them in order of increasing cost so the city council can choose the most economical containment strategy.

This ***MUST*** be a greedy algorithm.  It must not be a brute-force algorithm (i.e., try all possibilities).



### Example

Consider a situation where you have 75 zombies roaming around, and you must leave exactly 10 for the researchers.  There are 6 elimination companies.  Thus, $x=75$, $y=10$, and $z=6$.

| Company name | remove<br>1 ($c$) | remove<br>half ($d$) | Lowest<br>cost |
|----|----|----|----|
| Afterlife Cleanup Systems | 5 | 3 | 46 |
| Biohazard Consulting | 3 | 5 | 34 |
| Global Undead Solutions | 3 | 2 | 28 |
| Omniexterminate | 1 | 2 | 12 |
| Undead Management Corp | 9 | 9 | 90 |
| Zombie Remediation Group | 1 | 20 | 30 |

For most of these, the best option is to cut in half twice (75 -> 37 -> 18) to start.  We can't cut in half a third time, as we would be less than the 10 that we need to save.  Then we have to do 8 separate individual removals.

However, that is not the case for the Zombie Remediation Group.  It's best to cut in half once to start (75 -> 37) for $20.  But then cutting in half a second time, which would reduce the zombies from 37 -> 18, is more expensive than 19 individual elimination costs of $1 each.


### Input

The first line of the input will contain a single number which is the number of test cases in the input. 

The first line in each test case will contain three numbers: the number of zombies there are, how many you must must leave for the researchers, and the number of available zombie elimination companies, in that order.  We will designate these numbers as $x$,
$y$, and $z$.

Each of the following $z$ lines in the test case will contain the information for one of the zombie elimination companies.  Each line will contain, space separated, the following values: the company name (alphanumeric -- no spaces, but underscores and dashes are allowed), their charge $c$ for the first service (eliminating one zombie), and their charge $d$ for the second service (eliminating half of the zombies).  

All numeric values will be non-negative integers, and all will be less than $2^{31}$.



### Output

For each test case, your output should start with the line `Case #`, where `#` is the case number, starting from 1.

Each case will contain $z$ additional output lines, one for each agency.  Each line should list the agency name, a single space, and the *minimum* cost of using that company.  The list should be sorted by cost (increasing); ties are resolved by the normal alphabetical sorting of the company names.

All numeric output values will be less than $2^{31}$.

### Sample Input

This input is available as [example.in](example.in).

```
2
75 10 6
Afterlife_Cleanup_Systems 5 3
Undead_Management_Corp 9 9
Global_Undead_Solutions 3 2
Biohazard_Consulting 3 5
Zombie_Remediation_Group 2 7
Omniexterminate 1 2
2246 2245 5
Apocalypse_Control 100 600
Skullcrack_Command 2 2000
The_Zombie_Terminators 20 20
Brain_Blast_Industries 2 100
Chainsaw_Response_Team 0 0
```


### Sample Output

This output is available as [example.out](example.out).


```
Case 1
Omniexterminate 12
Global_Undead_Solutions 28
Biohazard_Consulting 34
Afterlife_Cleanup_Systems 46
Zombie_Remediation_Group 47
Undead_Management_Corp 90
Case 2
Chainsaw_Response_Team 0
Brain_Blast_Industries 2
Skullcrack_Command 2
The_Zombie_Terminators 20
Apocalypse_Control 100
```

### Requirements

This ***MUST*** be a greedy algorithm.  It must not be a brute-force algorithm (i.e., try all possibilities).

### Submission

The submission system can handle four different programming languages.  For each programming language, the name of the submitted file is listed below -- you have to have it named that exact name, else it will not compile properly.  If you want to program in a different language, email the course email at least three days before it is due, as we have to reconfigure the submission system to handle that language.

- Python 3: pa3.py
- Java: PA3.java
- C: pa3.c
- C++: pa3.cpp

You will submit your completed source code file to Gradescope.  There will be a *small set* of acceptance tests that are ***NOT COMPREHENSIVE***.  These acceptance tests are the test cases in the [example.in](example.in) file.  It's up to you to comprehensively test your code.  The acceptance tests just verify that you are reading the input correctly and providing the expected output.

Note that when you submit, Gradescope will report your grade as "-/10" or "0/10" -- that's a quirk of Gradescope, and is because the grading tests have not been run (and won't be run until after all submissions are in).  YOu can look at the results of the individual test cases to see how your program worked.
