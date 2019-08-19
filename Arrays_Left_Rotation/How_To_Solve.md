# Problem Description
A left rotation operation on an array shifts each of the array's elements 1 unit to the left. For example, if <b>2</b> left rotations are performed on array [<b>1,2,3,4,5</b>], then the array would become [<b>3,4,5,1,2</b>].

Given an array <i><b>a</b></i> of <i><b>n</b></i> integers and a number, <i><b>d</b></i>, perform <i><b>d</b></i> left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

<b>Function Description</b>

Complete the function rotLeft. It should return the resulting array of integers.

rotLeft has the following parameter(s):

- An array of integers <i><b>a</b></i>.
- An integer <i><b>d</b></i>, the number of rotations.

<b>Input Format</b>

The first line contains two space-separated integers <i><b>n</b></i> and <i><b>d</b></i>, the size of <i><b>a</b></i> and the number of left rotations you must perform. The second line contains <i><b>n</b></i> space-separated integers <i><b>a[i]</b></i>.

<b>Constraints</b>

- 1 &leq; <i>n</i> &leq; 10<sup>5</sup>
- 1 &leq; <i>d</i> &leq; <i>n</i>
- 1 &leq; <i>a[i]</i> &leq; 10<sup>6</sup>

<b>Output Format</b>

Print a single line of <i><b>n</b></i> space-separated integers denoting the final state of the array after performing <i><b>d</b></i> left rotations.

<b>Sample Input</b>

    5 4
    1 2 3 4 5

<b>Sample Output</b>

    5 1 2 3 4

# How To Solve This Problem
This problem can be visually confusing looking at the examples. However, the best way to solve this problem is with laziness in mind. Looking at this problem, I don't want to actually shift anything. Instead, I want to just figure out where the element in the array should start and then where to insert the elements before and after that element.

Let's break it down to much more simpler terms. First we want to find a pattern with how everything shifts. If <i>d</i>, the value that determines how many left shifts to perform, is <i>d = 2</i>, and our array is [1, 2, 3, 4, 5], then we observe the following:

    Step 0: [1,2,3,4,5]
    Step 1: [2,3,4,5,1]
    Step 2: [3,4,5,1,2]

And if <i>d = 3</i> on the same array [1,2,3,4,5], we also observe the following:

    Step 0: [1,2,3,4,5]
    Step 1: [2,3,4,5,1]
    Step 2: [3,4,5,1,2]
    Step 3: [4,5,1,2,3]

Do you see a pattern? Notice how the value of <i>d</i> dictates where the rest of the elements are placed? When <i>d = 2</i>, everything before index <i>2</i> in the array comes <i>after</i> the <i>5</i>, and everything inlcuding index <i>2</i> comes <i>before</i>. In fact, we can define a formula for how the last element in the array (in this case <i>5</i>) will be placed at what index:

    Let the length of the array be defined as <i>l</i> and <i>d</i> define the number of left rotations. 
    <i>(l - d) - 1</i> defines the index where the last element in the array will be inserted at the end of the rotation.

The above formula is initially helpful because it shows that as long as we know where the last element in the array sits, we can determine what comes before and after it. It also helps us identify an edge case:

    If <i>d = l</i> then we return the array unaltered.

This is because, we know that the array will simply shift enough times where all the elements will end in the same position as they started.

## Putting it all Together
We can assert the following:

For a given array <i>a</i> with a set length <i>l</i>, we must peform a given number of left rotations defined by <i>d</i>. To determine where all elements in the array will be shifted based on <i>d</i> we must assert the following:

- If <i>d = l</i> return <i>a</i>.
- For <i>d</i> &gt; <i>l</i>, let the set of all elements in <i>a</i> including and after index <i>d</i> be denoted as <i>a</i><sub>before</sub> be inserted into <i>a</i> first.
- For <i>d</i> &gt; <i>l</i>, let the set of all the elements in <i>a</i> before index <i>d - 1</i> come after index <i>d</i> be denoted as <i>a<sub>after</sub></i> be inserted into <i>a</i> last.

As long as <i>d &ne; l</i>, then our new array will consist of the set {<i>a<sub>before</sub>, a<sub>after</sub>}.
