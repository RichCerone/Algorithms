# Problem Description
HackerLand University has the following grading policy:

- Every student receives a <i><b>grade</b></i> in the inclusive range from <b>0</b> to <b>100</b>. Any grade less than <b>40</b> is a failing grade.

Sam is a professor at the university and likes to round each student's grade according to these rules:

- If the difference between the <i><b>grade</b></i> and the next multiple <b>5</b> of is less than <b>3</b>, round <i>grade</i> up to the next multiple of <b>5</b>.
- If the value of grade is less than <b>38</b>, no rounding occurs as the result will still be a failing grade.

For example, <i><b>grade = 84</b></i> will be rounded to <b>85</b> but <i><b>grade = 29</b></i> will not be rounded because the rounding would result in a number that is less than <b>40</b>.

Given the initial value of <i><b>grade</b></i> for each of Sam's <i><b>n</b></i> students, write code to automate the rounding process.

<b>Function Description</b>

Complete the function gradingStudents in the editor below. It should return an integer array consisting of rounded grades.

gradingStudents has the following parameter(s):

- grades: an array of integers representing grades before rounding

<b>Input Format</b>

The first line contains a single integer, <i><b>n</b></i>, the number of students.
Each line <i><b>i</b></i> of the subsequent lines contains a single integer, <b><i>grades[i]</i></b> , denoting student <i><b>i</b></i>'s grade.

<b>Constraints</b>
- <b>1 $\leq$</b> <i>n</i> <b>$\leq$ 60</b>
- <b>0 $\leq$</b> <i>grades[i]</i> <b>$\leq$ 100</b>

<b>Output Format</b>

For each <i>grades[i]</i>, print the rounded grade on a new line.

# How to Solve This Problem
The wording for this problem can be tricky. We can start by breaking it down as so:

1. Grades are between 0 and 100.
2. Grades less than 40 <i>(n $\lt$ 40)</i> are considered failing.
3. Grades are rounded to the nearest multiple of 5, if not considered failing <i>($\lt$ 40)</i>.
4. Grades less than 38 (37 or below) will not be rounded at all because they will never be 40 or greater.

The easiest way to solve this problem is start by figuring out when we want to round. If we let each grade be defined as g we can assert the following:

<i>g is rounded to the nearest multiple of 5 when g $\lt$ 3. Anything less than 38 can be skipped and we take the unaltered grading value.</i>

The next part of the problem is figuring out whether a value <i>should</i> be rounded even though it is 38 or greater. Modulo is our best friend here, because we can use remainders to determine whether a value should be rounded. Let's use this table as an example:

|Original Grade| Next Multiple of 5|
|--------------|-------------------|
|73            |75                 |
|67            |70                 |
|38            |40                 |

<i>75 - 73</i> gives a remainder of 2.
<i>70 - 67</i> gives a remainder of 3.
<i>40 - 38</i> gives a remainder of 2.

Based on this simple math we know that rows 1 and 3 would be rounded to the nearest multiple of 5.

To figure out how to know what the multiple of 5 is, we can simply subract 5 from the remainder of a modulo operation to get the proper remainder (or distance) from the next multiple of 5. For example:

<i>5 - (73 mod 5) = 2</i>
<i>5 - (67 mod 5) = 3</i>
<i>5 - (38 mod 5) = 2</i>

If <i>5 - (73 mod 5) = 2</i>, then we know that <i>73</i> needs to be added by <i>2</i> in order to get to the next multiple of <i>5</i>: <i>75</i>.

## Putting it all Together
We can assert the following:

For a given grade <i>g</i>, if <i>g $\geq$ 38</i> and <i>5 - (g mod 5) $\lt$ 3</i>, then <i>g</i> = g + (5 - (g mod 5)). Otherwise, take the value of <i>g</i> itself.

The above assertion gives us the solution needed to solve this problem.
