---
layout: default 
title: Syllabus
nav_order: 2
---

# Syllabus
{: .no_toc }

Page Last Updated: {{ site.time | date: '%A, %B %d, %Y' }}

## TL;DR (Too Long; Didn't Read)

We realize not everybody will read through this entire document.  So here are the highlights:

- If you have concerns, please email [cs3100@cshelpdesk.atlassian.net](mailto:cs3100@cshelpdesk.atlassian.net) rather than the instructors (it's a quicker response time).  Please do not emails the TAs directly.
- There will be five modules taught in the course: graphs, divide and conquer, greedy algorithms, dynamic programming, and reductions.
- There will be five quizzes, one per module, and will be in a dedicated Computer Based Testing Facility (CBTF) -- more information about this is below, and will be discussed when we get to that point.  There will also be a practice quiz in the CBTF.  It's the same CBTF that was used in DSA1 last semester.
- There will be one programming assignment (PA) per module; any language is fine, but if it's not a currently supported language (Java, Python, C, C++, and Rust), you have to let us know in time to configure the submission system.
- There will be two problem sets (PS) per module -- these have to be typeset using LaTeX, which assignment PS0 will cover.  You can collaborate with up to five other students on the problem sets, but you need to list who you collaborated with in your assignment.
- Grades will be 60% quizzes, 20% programming assignments, and 20% written (typed) problem sets
- Late PAs and PSs will receive 25% off per day for each day (or fraction thereof, including 1 second) it is late
- You have eight extensions that you can use throughout the semester -- these can be added or removed up to 4 days after the original due date using an automated system.  Each extension will delay the onset of the late penalty by 4 days (96 hours).
- We have a textbook, but it's available online for free through the UVA library: [Introduction to Algorithms](https://ebookcentral-proquest-com.proxy1.library.virginia.edu/lib/UVA/detail.action?docID=6925615), called "CLRS" after the intials of the authors.
- If we mess up the grading on anything, there will be an opportunity to submit a regrade; this is typically limited to 7 days after the assignment or quiz was returned.
- Generative AI usage: you may not use it to generate solutions for the problem sets or programming assignments, but you are encouraged to use it to help study and prepare; you may not use it at all for the quizzes. <!--you can use it for the problem sets, in limited circumstances for the programming assignments, and not at all for the quizzes.-->
    - That being said, the material in this course is the primary content used in job interviews.  If you just use generative AI, then you are not going to learn the material, which will tank you in your interviews.  There is a reason that companies fly you out to their location for a full day interview -- it's to see what you really know.  And they aren't going to let you use generative AI during those interviews.

## Logistics

### Getting Connected

#### Course Contact Information

**Course Email: [cs3100@cshelpdesk.atlassian.net](mailto:cs3100@cshelpdesk.atlassian.net)**

Please use our course email for the fastest response time with course staff.  This email is monitored by our TAs and professors in a help-desk ticketing system and will allow us to more quickly resolve any issues.

#### Professor Contact Information

Aaron Bloomfield
- Email: aaron_at_virginia.edu
- Office: Rice 402
- Office Hours: TBD

Robbie Hott
- Email: jrhott_at_virginia.edu
- Office: Rice 401
- Office Hours: TBD

If you email a professor, include "DSA2" at the beginning of the subject line to help us prioritize your email.


#### Teaching Assistants

Our TAs are students too, with duties and work outside of their TAing. Please do not ask them to act as your TA except at the scheduled on-the-clock times they have listed as their office hours. They are also kind people; please don't put them in the position of having to say no or (worse) being nice to you at the expense of their own schooling.

TA office hours and location will be posted on the Canvas landing page.

### Class Meetings

Most often CS3100 class meetings will follow a lecture format, but we may use some part of class time for collaborative learning, which will benefit from students being present.

Lectures **will not** be recorded this semester.  You are strongly encouraged to come and participate in the discussion and learning activities.


### Practicing and Measuring Learning

As always, there will be tasks for students to carry out to support learning and help us assess your learning. 
Some tasks are designed to help you learn and practice what you learned enough that the concepts solidify in your mind.
Others are designed to measure what you have learned.
The primary kinds of tasks are:  Quizzes, Programming Assignments (PAs), Problem Sets (PSs). 



#### Quizzes 

There will be five quizzes (exams) this semester, each on a separate module.  The fifth quiz will be during finals week.  There will also be a practice quiz before the other quizzes.  There will also be a practice quiz, which will be worth less of the overall quiz grade than the regular quizzes.

All quizzes will be taken in a dedicated Computer-Based Testing Facility (CBTF), which is located in Gilmer Hall, room 490A.  Each quiz will be 50 minutes long, and can be taken at any time over the 3 day period specified in the course schedule.  While everybody will get similar questions, the questions themselves will be randomized, so that one person's quiz will not be the same as another person's quiz.  That room has a limited capacity (40 seats), and you will need to schedule a time based on your availability.  If you wait until the last minute to schedule an quiz, then you will be stuck with whatever spots are still left.  We will provide scheduling details as the semester progresses.

The practice quiz, "Quiz 0", will be a practice quiz to familiarize you with the CBTF, the quiz taking procedure, and the types of questions you may see.  The answers to this quiz are either obvious or are provided to you -- the goal on this practice quiz is to learn the system, not test your knowledge.

We will make it clear what each quiz entails, and what questions are on each quiz.  The goal is to ensure that those who take it early are not at a disadvantage versus those who took it later and spoke to those who took it early.  We were able to achieve that last semester, and we will achieve that this semester.

If you have a valid reason to miss a quiz, then we will allow a make-up.  Unless it is an emergency, you need to let us know ahead of time.  Missing a quiz due to not realizing that you were supposed to take it will not allow a make-up.

***GRADING WARNING:*** This is the first semester we are using the CBTF for the *entire* semester (we used for half a semester in the past).  Some of the questions will be a choose-1-of-many -- meaning you will be given one randomly chosen algorithm to solve on from a set of four or so.  Each of the questions in this set will have a different grading scheme, since it is a different question, and some algorithms may be harder than others.  As a result, there will be ***GRADING MODIFICATIONS*** to the grade you receive.  The intent is to ensure that those who get a harder algorithm to solve are not at a disadvantage versus those who received an easier algorithm to solve.  These modifications may be positive or they may be negative -- again, the goal is to ensure it is fair across the entire class.  The grading modifications will be based on the mean score for each of the questions, and we will present this math to the entire course.


#### Programming Assignments (PAs)

The goal of Programming assignments (PAs) is to explore one or more topics from a unit by applying an algorithm to a problem, implementing it in code, and showing it works correctly by passing a set of test-cases.  Grading will be primarily based on passing test-cases on GradeScope.  Some PAs may require a short write-up. Submissions must include information about sources, collaborators, etc.   For more information, see sections below on "Collaboration and Outside Sources" for PAs.

Generative AI can generally not be used for programming assignments, but see our full [Honesty and Collaboration](#honesty-and-collaboration) and [Generative AI policy](#honesty-and-collaboration) below.

When you submit a PA, the submission system will run a small set of tests on your code to ensure it interacts properly with the grading system (compiles, handles I/O correctly, etc.).  These test cases will be the ones provided in the assignment.  There will be a *separate* set of test cases that your grade will be based on, which will not appear until the assignment's grade is returned to you.  We do it this way because if we revealed the grading test cases at the start, then one could get full credit by just using `print()` statements.

You may write code in any programming language that you would like.  Students most often use Java and Python, and our system handles C, C++, and Rust.  If you want to use a different language, you need to contact us, at least three days before the due date, so that we can reconfigure the submission system to handle that other language.



#### Problem Sets (PSs)

Each Problem Set (PS) will include some written and thought-provoking questions on the content that we're discussing. Some may be simple questions on concepts or details of what's be taught, but most will require students to design an algorithm, analyze it's complexity, make proofs or other logical arguments about its complexity, correctness, etc.  For information on collaboration on PSs, see the section below on "Collaboration and Outside Sources" for PSs.

Generative AI can generally not be used for problem sets, but see our full [Honesty and Collaboration](#honesty-and-collaboration) and [Generative AI policy](#honesty-and-collaboration) below.


#### LaTeX Warm-up

PS0 will be designed to help learn how to use the LaTeX typesetting system, which will be used for all PSs in this course.


### Textbook and Readings

We will assign readings from the "CLRS" textbook:  Introduction to Algorithms, by Cormen, Leiserson, Rivest and Stein, 4th Edition. (3rd edition is OK, but is missing some new material.) The book is available for free for UVA users in an online format through the UVA Library at [this link](https://ebookcentral-proquest-com.proxy1.library.virginia.edu/lib/UVA/detail.action?docID=6925615).  There may be additional readings from online sources.  The readings for each chapter are shown on the [schedule page](schedule.html).


### Coding

> "If you really want to understand something, the best way is to try and explain it to someone else. That forces you to sort it out in your own mind. And the more slow and dim-witted your pupil, the more you have to break things down into more and more simple ideas. And that’s really the essence of programming. By the time you’ve sorted out a complicated idea into little steps that even a stupid machine can deal with, you’ve certainly learned something about it yourself."
> <div class="text-right">-Douglas Adams</div>

In this course, you are welcome to use Python, Java, C/C++, or Rust to complete your PAs.  We will provide starter code for both languages.  Please choose an IDE that you are comfortable working with (Eclipse, IntelliJ, PyCharm, VSCode, vim (if you're like Prof Hott), etc).  For each PA, you should thoroughly test your algorithms; we will provide some example test cases in the assignment descriptions, but you should devise your own tests to check edge and corner cases.

You will be asked to submit your code to Gradescope.  It is important to use a version of a language that is compatible with our grading system.  Therefore, we **strongly suggest** using either:
- Python 3.10
- Java 21 (OpenJDK)
- C/C++
- Rust

*If you choose to use a different version, please be sure that any classes, methods, language features you use are available in these versions.*

Estimating how long it will take someone to complete a coding assignment is always difficult.
The target difficulty is 5–10 hours of focused effort each week.

## Grading

### Grading Scale

We will use the standard grading scheme for this course.

|  Grade    |  Lower Bound    |
| :-------: | :-------------: |
| A+        | 98.0*           |
| A         | 93.0            |
| A-        | 90.0            |
| B+        | 87.0            |
| B         | 83.0            |
| B-        | 80.0            |
| C+        | 77.0            |
| C         | 73.0            |
| C-        | 70.0            |
| D+        | 67.0            |
| D         | 63.0            |
| D-        | 60.0            |
| F         | 0               |

* Note that the A+ range is a percentage of students in the course, so the actual cut-off may vary.

### Points per Activity Type

Points are awarded per task.
Different tasks and different task types are given different weight, as outlined below.

| Task        | Weight    |
|:------------|:---------:|
| Quizzes     |   60%     |
| PAs         |   20%     |
| PSs         |   20%     |


### Extensions and late submissions

Submissions for the programming assignments will generally open one week (7 days) before the due date/time.  Submissions for problem sets will generally open up 3 days (72 hours) before the due date/time.

Assignments turned in after the due date are penalized 25% per day (or fraction thereof) late; this means a maximum of just under 4 days (i.e. just under 96 hours) late.  For example, anywhere from 1 second late to 24 hours late receives 25% percent off.  Due to how the different grading systems work, that ends up being 2.5 points off for each late day for each problem set, and 25% off per each late day for the programming assignments.

You may request an extension on any assignment (PA or PS) for any reason -- there is an automated system, linked to from the Canvas landing page, for this.  That extension is 4 days.  **HOWEVER**, you only have 8 such "free late passes" during the semester -- once they are used up, there will not be any more.  An extension will delay the onset of the late penalty by 4 days -- so if you get an extension, then the late penalty does not kick in until the 5th day after the due date.

This extension rule does not apply to quizzes, exams, or any in-class activities.  It only applies to programming assignments (PAs) and written assignments (PSs).

However, there are a few specifics to this extension rule:

- As mentioned above, you only have 8 such free late passes to use throughout the semester
- The extension request must be submitted no later than 4 days after the (regular) due date.  We will not allow anybody to submit it after this date (it actually should be in before the due date itself, but we are giving you 4 days to submit after the original due date).
- You may add an extension as early as you would like -- even on class day 1, for example.  You may remove an extension, up to 4 days after the original due date.  After 4 days post the due date, you may not make any modifications to that extension.
- This extension time covers any and all situations: travel, holidays, being busy, family emergencies, SDAC (generally), dog ate your homework, religious observances, interviews, thunderstorms, power outages, temporal dislocation, etc.
- We are not expecting to allow any further extensions beyond this 4 days, unless there are considerable extenuating circumstances -- essentially, something that would have granted an extension for more than 4 days in the first place.  If you get busy or sick at the end of your 4 day extension request, then that's your tough luck.
- After you extension ends, the late penalty (above) kicks in for the next four days.
- This policy *already includes* SDAC accommodations less than 4 days (we are just extending these accommodations to everybody).  Likewise, religious accommodations of a short time (a few days) are handled by this policy as well.  It also covers short-term (less than 4 days) athletic extensions.
- If there is a valid need for an extended accommodation -- SDAC, religious, health, athletic, etc. -- please chat with one of the instructors, and we'd be happy to discuss it with you.
- Be aware that TA and instructor office hours are optimized for the actual due date -- if you file for an extension, there may not be sufficient office hours available for when you plan to submit it.  Also, the next week's office hours will have to focus on the assignment due that week.


### Grading Mistakes

Much of the grading in this course is done by hand with the help of teaching assistants. Some of the grading is done directly by hand by the instructors. The course staff occasionally also use tools to help with initial clustering of student answers in to similarity groups. In all of these cases, we realize that sometimes the grading of a problem ends up being incorrect. If you think a grading mistake on a PS has been made, but it is in your favor, you are not required to communicate that with the course staff. If you think there is a grading mistake on a PS that scores your answer with fewer points than it should have been scored, you may submit a regrade request through Gradescope.  

**Problem Sets**: Regrade requests for problem set (PS) assignments will be accepted for 7 days after the graded assignment is released to the student. For PS assignments, within Gradescope, you will see the option to make a regrade request for an individual problem. If the regrade request time period is past (it's more than 7 days since the assignment was graded and released to the student), you will not have an opportunity to request a regrade and you will see that Gradescope will not provide a regrade request button. When you request a regrade, our primary goal is to make sure that the grading was accurate, and change the grading if it wasn't. In the course of regrading a problem, we usually need to look at the entire problem, not just a small piece of it. If we notice grading mistakes other than the one you describe, we will fix all of the ones that we notice. This includes any grading mistake we happen to notice in other problems. We don't go out of our way to find more mistakes, but if we happen to see one, we will fix it. After the regrade is completed, your corrected grade may be higher, lower, or the same as your previous grade. Before making a regrade request, make sure that you understand what the question was asking and reassess your answer. Please be specific in what rubric(s) you think were mis-graded. Regrade requests of the type, "I only got 10 out of 25 points and I think I should have received more" aren't as helpful to us as a more specific statement such as, "I didn't receive points for the first rubric, but I think I did address that issue in the second sentence of my explanation".     

**Programming Assignments**: Programming Assignments (PAs) are auto-graded, and regrades are handled differently.  We will strictly follow the auto-grader's result in each and every case.  However, there are times when the auto-grader has bugs, doesn't handle certain cases, etc.  For each PA, a Piazza post will be created where one can put comments and suggestions for how to modify the auto-grader.  Those comments need to be submitted within a reasonable period (one week after the post is made). Addressing these auto-grader issues takes time, but will occur via that one Piazza post thread.

If this regrade policy is abused during the semester (many students are submitting frivolous regrades), then we reserve the right to start applying a frivolous regrade penalty.  We will clearly communicate this if it is to occur.


## Professionalism

In this course, there will be a focus on working well together and learning. Students and staff are all expected to treat each other with respect. This includes, but certainly is not limited to:

- Misuse of class platforms (Discord, Piazza, YouTube comments, etc.)
- Disrespectful language or actions to course staff or other students
- Promptness for all deadlines and class meetings
- Quality work
- Excessive frivolous regrade requests
- Not following University regulations or being mindful of others

Behave professionally.

Never abuse anyone, including the emotional abuse of blaming others for your mistakes.
Kindness is more important than correctness.

Let our TAs be students when they are not on the clock as TAs.

**Consequences of Unprofessional Behavior**: Unprofessional behavior, such as misbehavior towards instructors, classmates, or TAs, or causing distractions for other students, can be held against a student when final grades are calculated.  The penalty is up to 20% of the final course grade.

## Honesty, Collaboration, and Generative AI Usage

We always hope everyone will behave honestly.
We know we all are tempted to do what we ought not;
if you do something you regret, the sooner you tell us the sooner (and more leniently) we can correct it.

Generative AI is the way of the future, especially in computing. While we encourage embracing it, as your instructors and as computer scientists, we believe that a firm foundation in computer science is necessary for efficient and accurate use of these emerging tools. This is a foundation course, so we want to help you build intuition outside of AI for programming so that you will have the background and expertise moving forward when you use generative AI.  **Namely, expert AI use requires expertise.**

### No plagiarism (nor anything like it)

You **must** cite any and every source you consult, other than those explicitly provided by the course itself.
Talked to a friend, saw an interesting video, consulted a website, had a tutor?
Tell us!
Put it in a comment in your code or asssignment.

#### Understand what you submit

Your understanding is the primary deliverable of our assignments, not the code itself.
As such, we may ask you to explain aspects of a solution you turn in,
and may dock points if it appears you simply copied someone else's ideas (or just guessed a lot of things until one worked) without understanding them.

### Programming Assignments

#### Collaboration and Outside Sources

You may discuss the problem and the overall strategy with up to 4 other students, but you **must** list those people in your submission under collaborators.  You may **not** share code, post your code publicly online, look at others' code, or help others debug their code. You must write your own code.
Not just type it (though you need to do that too): **compose it yourself**, as your own original work. Please read the sections following this one for more details and clarifications. 

Do not seek published or online solutions for any assignments. If you use any published or (which may not include solutions) when completing this assignment, you must cite them by giving a complete citation of each source as a comment at the top of your the program file you submit. Do not submit a solution that you are unable to explain orally to a member of the course staff. Failure to cite a source is a serious violation of academic integrity and may result in a grade penalty (perhaps a severe one).

You must write your own code. Not just type it (though you need to do that too): **compose it yourself**, as your own original work.

#### Generative AI Usage

The PAs are intended to help you practice and learn the content, so you are **not** allowed to use generative AI to write the code.  Why?  The process of problem solving and programming will help you build mental models and strategies for solving problems.  Could generative AI write this code for you?  Yes!  But then you're missing out on gaining the experience and knowledge gain of trying it yourself -- you can't replace that with AI.  So you may **NOT** use AI to write these for you.

You may use generative AI to look up a ***SMALL*** snippet of code, such as how to use a particular function.  That snippet of code can be no more than two lines in length.

That being said, the material in this course is the primary content used in job interviews. If you just use generative AI, then you are not going to learn the material, which will tank you in your interviews. There is a reason that companies fly you out to their location for a full day interview – it's to see what you really know. And they are not going to let you use generative AI during those interviews.

You must write your own code. Not just type it (though you need to do that too): **compose it yourself**, as your own original work.

You must cite all generative AI uses, such as code snippet generation, as described [below](#citing-generative-ai-use).


### Problem Sets

#### Collaboration and Outside Sources

On Problem Sets you are allowed (and encouraged) to collaborate with up to 4 other students, but all work submitted must be your own **independently** written solution. List the computing ids of all of your collaborators in the __collabs__ command at the top of the .tex file you submit. 

Our intention is that collaborators can discuss the problems and possible solutions in a way that helps each member of the group to learn more effectively. We do not allow collaborative activities that make it easier for each individual to write-up a solution for submission. To avoid this, you are not allowed to share written notes, documents (including Google docs, Overleaf docs, discussion notes, PDFs), or code. Talk to increase your understanding of the problem and how to solve it, then take what you've learned from that collaboration and write-up your own solution.

Do not seek published or online solutions for any assignments. If you use any published or online resources (which may not include solutions) when completing this assignment, you must cite them by giving a complete citation of each source in the __sources__ command at the top of the .tex file you submit. Failure to cite a source is a serious violation of academic integrity and may result in a grade penalty (perhaps a severe one).


#### Generative AI Usage

The problem sets are intended to help you practice and learn the content, and they'll include some questions that will help prepare you for the quizzes (and even future job interviews!).  Therefore, like PAs, you may **not** use generative AI to solve and write them.  Why?  The process of solving these problems and converting those solutions into coherent and cohesive algorithms, arguments, and/or proofs will help you build strategies for future problems.  **We want to build your mind, NOT just get the answers.**  Generative AI may be able to provide good enough answers, but it won't give you an intuition.  And... how do you know it gave you the right answer?  Or if it's right, is it good?

That being said, once you have solved (or fully attempted to solve) the PS problems on your own (or with your group), you may use generative AI to check your answers.  This only applies to PS assignments, not to PA assignments!  Discussing the problems and strategies with the course staff during office hours is typically much better than using generative AI to verify your answers.

You must cite all generative AI uses, including that you checked your answers, as described [below](#citing-generative-ai-use).

### Quizzes

It would probably go without saying if we didn't say it, but no assistance may be given or received on any supervised evaluation or quiz unless specifically announced otherwise by the professor (or another proctor of the evaluation).


### Allowed Uses of Generative AI


You may use generative AI to:

1. Verify the answers to the problem sets once you have made a sincere effort to solve them yourself first
2. Look up small code snippets (no more than 2 lines) in lieu of using a programing language reference
3. Summarize course material
4. Help you study the course content
5. Provide context around the material we're discussing
6. Generate practice problems to help study and prepare, 
7. Check the work of any practice problems you generate

**Note:** _if you use generative AI in connection with any assignment in the course, you **must cite that usage** as noted below._

**If you are ever in doubt as to whether a use of generative AI is acceptable or not, please post on Piazza or send an email to the course ticketing system.**  We'll respond as quickly as possible as well as update this section of the syllabus with more details.

#### Available Models

Three different Generative AI models are available for you to use during this course (within the restrictions above).

1. Our [Office Hour queuing system (ASCI)](https://kytos02.cs.virginia.edu/asci) has a built-in local LLM model.  It has access to our course material, including slides when available, so it will be able to provide direct answers with references to specific course documents.  Please note that it takes a few seconds to respond as it is running on a server in the basement of Rice Hall.
2. [Microsoft Copilot](https://copilot.cloud.microsoft/) through Office 365.  With UVA's license agreement, your interactions are not used to train the model, providing some privacy guarantees over other paid models.
3. [Google Gemini](https://gemini.google.com).  With UVA's license agreement, your interactions are not used to train the model, providing some privacy guarantees over other paid models.  *You must [request access from ITS](https://virginia.service-now.com/esc?id=sc_cat_item&sys_id=322248a91bd37254f9b86575624bcb82) before you can use Gemini.

#### Risks of Generative AI

Generative AI tools can be powerful learning aids, but they also come with important limitations and risks. Remember that generative AI can only generate content from their training data, which is out of date, and they may provide incorrect or false information. Therefore, please keep the following in mind:

1. **Outdated or inaccurate content:** AI systems are trained on past data, so their knowledge may be out of date. They may also produce responses that sound confident but are factually incorrect.
2. **Plagiarism and copyright concerns:** AI models are trained on pre-existing material, which may include copyrighted content. Using AI output without proper citation may lead to plagiarism or copyright violations.
3. **Not designed for accuracy:** The goal of these tools is to generate human-like text, not necessarily reliable or correct information. Submissions based solely on AI output may therefore be inaccurate or incorrect.

Ultimately, **you are responsible**--not the AI--for ensuring that your work is accurate, original, and consistent with the standards of this course. Please carefully evaluate AI responses against course material and, **whenever in doubt, don't hesitate to visit a TA or instructor during office hours**. _We **enjoy** discussing the material with you!_

#### Citing Generative AI Use

**You must properly document and credit the generative AI tools** themselves when your use is connected with any assignment in the course. Cite each tool you used, in the form shown below for Copilot.  **Note:** you must include the **name of the tool**, the **URL for the tool**, and a **brief description of how you used it in relation to the assignment**.

{: .aside-title}
> Example Generative AI Citation
>
> Microsoft Copilot (UVA licensed version). Accessed from https://copilot.microsoft.com.  Generated practice problems similar to the homework assignment to get extra experience before starting on the actual problems.  Used Copilot to check my work on the practice problems and provide feedback.

Failure to cite the use of the tool as a source is a serious violation of academic integrity.  If you use generative AI tools to complete assignments in this course, in ways that we have not explicitly authorized, **we will apply the course's policies on academic integrity** appropriate to your specific case. In addition, you must be wary of unintentional plagiarism or fabrication of data. Please act with integrity, for the sake of both your personal character and your academic record.


## Consequences of Dishonesty

If we believe you have acted dishonestly, including sharing or receiving code, we will communicate this fact to you and propose a penalty.
If you have information we lack, please share that with us; we may thereafter change our belief and/or proposed penalty.
Penalties can include modification of the grade on the assignment, modification of the grade in the course, and may be up to and including a failing grade (F) in the course. *This is independent of and in addition to the operations of the Honor Code*.

If the case is particularly egregious and beyond our comfort level handling in-course, we will refer the case to the University Honor System.

## Life

Bad things happen.
People forget things and make mistakes.
Bad days coincide with due dates.
etc.

If you believe that circumstances warrant an change in deadline, a second chance, or some other accommodation in order to more accurately synchronize grade with knowledge, come talk to your professor and we'll resolve the situation as best we can. *Out of fairness, we can't promise we'll make extensions or accommodations.*


### Special Circumstances 

It is our goal to create a learning experience that is as accessible as possible. If you anticipate any issues related to the format, materials, or requirements of this course, please meet with me outside of class so we can explore potential options. Students with disabilities may also wish to work with the Student Disability Access Center (SDAC) to discuss a range of options to removing barriers in this course, including official accommodations. We are fortunate to have an SDAC advisor, Courtney MacMasters, physically located in Engineering. You may email her at [cmacmasters@virginia.edu](mailto:cmacmasters@virginia.edu) to schedule an appointment. For general questions please visit the SDAC website: [sdac.studenthealth.virginia.edu](http://sdac.studenthealth.virginia.edu/). If you have already been approved for accommodations through SDAC, please send me your accommodation letter and meet with me so we can develop an implementation plan together.

Since we are a large course, we ask that students with special circumstances let us know as soon as possible, preferably during the **first week of class**.

### Religious Accommodations 
It is the University's long-standing policy and practice to reasonably accommodate students so that they do not experience an adverse academic consequence when sincerely held religious beliefs or observances conflict with academic requirements.

Students who wish to request academic accommodation for a religious observance should submit their request in writing to me as far in advance as possible. If you have questions or concerns about academic accommodations for religious observance or religious beliefs may contact the [University's Office for Equal Opportunity and Civil Rights](https://eocr.virginia.edu/)  (EOCR) at [UVAEOCR@virginia.edu](mailto:UVAEOCR@virginia.edu) or 434-924-3200.  Accommodations do not relieve you of the responsibility for completion of any part of the coursework missed as the result of a religious observance.

### Safe Environment
The University of Virginia is dedicated to providing a safe and equitable learning environment for all students. 
If you or someone you know has been affected by power-based personal violence, more information can be found on the UVA Sexual Violence website that describes reporting options and resources available -- [www.virginia.edu/sexualviolence](https://www.virginia.edu/sexualviolence). 

The same resources and options for individuals who experience sexual misconduct are available for discrimination, harassment, and retaliation.  [UVA prohibits discrimination and harassment](https://uvapolicy.virginia.edu/policy/HRM-009) based on age, color, disability, family medical or genetic information, gender identity or expression, marital status, military status, national or ethnic origin, political affiliation, pregnancy (including childbirth and related conditions), race, religion, sex, sexual orientation, veteran status. [UVA policy](https://uvapolicy.virginia.edu/policy/HRM-010) also prohibits retaliation for reporting such behavior. 

If you witness or are aware of someone who has experienced prohibited conduct, you are encouraged to submit a report to [Just Report It](https://justreportit.virginia.edu) (justreportit.virginia.edu) or contact [EOCR](mailto:UVAEOCR@virginia.edu), the office of Equal Opportunity and Civil Rights.

If you would prefer to disclose such conduct to a confidential resource where what you share is not reported to the University, you can turn to [Counseling & Psychological Services](https://mentalhealthservices.studenthealth.virginia.edu/) (CAPS) and [Women's Center Counseling Staff and Confidential Advocates](https://womenscenter.virginia.edu/counseling/our-counseling-services) (for students of all genders). 

As your professor and as a person, know that we care about you and your well-being and stand ready to provide support and resources as we can. As a faculty member, we are responsible employees, which means that we are required by University policy and federal law to report certain kinds of conduct that you report to me to the University's Title IX Coordinator. The Title IX Coordinator's job is to ensure that the reporting student receives the resources and support that they need, while also determining whether further action is necessary to ensure survivor safety and the safety of the University community. 

### Well-being 
If you are feeling overwhelmed, stressed, or isolated, there are many individuals here who are ready and wanting to help. The Student Health Center offers Counseling and Psychological Services (CAPS) for all UVA students. Call 434-243-5150 (or 434-972-7004 for after hours and weekend crisis assistance) to get started and schedule an appointment. If you prefer to speak anonymously and confidentially over the phone, Madison House provides a HELP Line at any hour of any day: 434-295-8255.

### Support for Your Career Development 

Engaging in your career development is an important part of your student experience. For example, presenting at a research conference, attending an interview for a job or internship, or participating in an extern/shadowing experience are not only necessary steps on your path but are also invaluable lessons in and of themselves. We wish to encourage and support you in activities related to your career development. To that end, please notify us as far in advance as possible (at least one-week in advance of such an event) to arrange for appropriate accommodations.


## Student Support Team 


At UVA, you have many resources available to you when you experience academic or personal stress, and we understand that it's hard to know where to go, especially for CS students as our undergraduates span both the College of Arts and Sciences (BACS) and SEAS (BSCS).

In addition to your professor, the Computer Science department has staff members located in Rice Hall who you can contact to help talk through your academic or personal challenges and get you connected to the right resources. You may reach out directly to either SJ Jimènez-Calhoun ([smj4z@virginia.edu](mailto:smj4z@virginia.edu)) or Sheri Grimes ([prk2zq@virginia.edu](mailto:prk2zq@virginia.edu)), or visit during walk-in advising hours posted on the [CS Advising Site](https://uvacsadvising.org/).
Please do not wait until the end of the semester to ask for help!

#### Learning
- Lisa Lampe, Assistant Dean for Undergraduate Affairs, ll4uu@virginia.edu
- Georgina Nembhard, Director of Student Success, gnembhard@virginia.edu
- Courtney MacMasters, Accessibility Specialist, cmacmasters@virginia.edu
- [Free tutoring](https://engineering.virginia.edu/undergraduate-study/student-support/tutoring) is available for many CS and Engineering classes
- More [academic support programs around Grounds](https://academicsupport.virginia.edu/) for a wide variety of other courses, too


#### Health and Wellbeing

You may schedule time with the CAPS counselors through [Student Health](https://sites.studenthealth.virginia.edu/mental-health/getting-started-scheduling).  You are also urged to use [TimelyCare](https://sites.studenthealth.virginia.edu/mental-health/our-services/timelycare) for either scheduled or on-demand 24/7 mental health care.  If you need immediate assistance, call (434) 243-5150 to speak with an on-call clinician.

#### Accommodations

[Learn abou thte process of applying for Student Disability Access Center (SDAC) services](https://disabilityservices.studenthealth.virginia.edu/application-process), completing an online application, submitting documentation, undergoing a review, and attending an appointment to establish accommodations.

#### Community and Identity

The Center for Connection (The Connect) is a dedicated student space within UVA Engineering that fosters academic success and personal growth. Through its programs and initiatives, The Connect helps students strengthen their engineering identity while providing resources to help them thrive during their studies and beyond. Our work centers on three key areas: student belonging and development, academic support, and community programming grounded in intentional, data-driven strategies.

The Connect features an open study area, a flexible event space, and on-site staff who provide direct support and advising to students. It is part of the [Office of Community, Opportunity, and Engagement](https://engineering.virginia.edu/offices-programs/office-community-opportunity-and-engagement). 

## Additional Notes

**Syllabus Note**: This syllabus is to be considered a reference document that may be adjusted throughout the course of the semester to address necessary changes. This syllabus can be changed at any time, and the class will be notified if that is the case. Small changes, such as office hour times or grammatical corrections, will not have a notification issued.  Final authority on any decision in this course rests with the professor, not with this document.

**Research**: Your class work and related data might be used for research purposes in an anonymized form. For example, we may use anonymized scores from student assignments to compare to other student performance data. Any student who wishes to opt out can contact the instructor or TA to do so *after* final grades have been issued. This has no impact on your grade in any manner.
