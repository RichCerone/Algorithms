# Problem Description
It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by 1 from 1 at the front of the line to <i><b>n</b></i> at the back.

Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if <i><b>n = 8</b></i> and <i><b>Person 5</b></i> bribes <i><b>Person 4</i></b>, the queue will look like this: <b>1, 2, 3, 5, 4, 6, 7, 8</b>.

Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!

<b>Function Description</b>

Complete the function minimumBribes in the editor below. It must print an integer representing the minimum number of bribes necessary, or Too chaotic if the line configuration is not possible.

minimumBribes has the following parameter(s):

- q: an array of integers

<b>Input Format</b>

The first line contains an integer <i></b>t</b></i>, the number of test cases.

Each of the next <i><b>t</b></i> pairs of lines are as follows:
- The first line contains an integer <i><b>t</b></i>, the number of people in the queue
- The second line has <i><b>n</b></i> space-separated integers describing the final state of the queue.

<b>Constraints</b>

- <b>1 &le; <i>t</i> &le; 10</b>
- <b>1 &le; <i>n</i> &le; 10<sup>5</sup></b>

<b>Subtasks</b>

- For <b>60%</b> score <b>1 &le; <i>n</i> &le; 10<sup>3</sup></b>
- For <b>100%</b> score <b> 1 &le; <i>n</i> &le; 10<sup>5</sup></b>

<b>Output Format</b>

Print an integer denoting the minimum number of bribes needed to get the queue into its final state. Print Too chaotic if the state is invalid, i.e. it requires a person to have bribed more than <b>2</b> people.

<b>Sample Input</b>

    2
    5
    2 1 5 3 4
    5
    2 5 1 3 4

<b>Sample Output</b>

    3
    Too chaotic


# How To Solve This Problem
This problem is extremely tricky. It throws a lot of useless information that doesn't help you solve the problem. To keep it simple, let's sift through what's above and break down what is most important:

1. Any person (number) that moves past more than 2 other people (numbers) is considered "Too chaotic" and we therefore print out that statement.
2. You can only bribe your way forward.
3. With a given array, we need to print the shortest numbers of bribes that have occurred, and whether it is "Too chaotic."

First, if we try to attempt figuring out when a person has moved, this problem will become too long to solve and we will write an uneccessary amount of code. To keep it simple, let's just worry about <i>if</i> a person was bribed when a person behind them moved forward. We can assert the following:

- We know that a queue starts in order; meaning that if we have 4 people we have an array of [1, 2, 3, 4, 5].
- Given that the queue is not 0 based, we can simplify our logic by making it 0 based, and subtract each element (person) in the line by 1.

For example:

    [2,5,1,3,4] 
    [1,4,0,2,3]

By reducing each element to 0 base we can simplify how we calculate and compare our values.

The next step is to calculate a bribe. We know that if we are given an index <i>i</i>, it will correspond with the position on the line. Therefore if we take the value of index <i>i</i> and subtract it by <i>i</i> itself, we can get the total number of bribes that number committed in order to get where it at the end state of the array:

Let each index in a given array <i>a</i> be defined as <i>i<sub>n</sub>. &forall; i<sub>n</sub> &isin; a</i>, let the value of each <i>i<sub>n</sub></i> be defined as <i>n<sub>i</sub></i>. To calculate the number of moves <i>n<sub>i</sub></i> has made we peform <i>n<sub>i</sub> - i<sub>n</sub></i>.

The above formula helps us determine if a chaotic line has been formed by only having to look at a single element and avoid iterating through the whole array.

If a chaotic line did not form, we still need to determine how many bribes occurred. To do this we can use our 0 based array and determine if the largest digit in range is greater than the digit being compared. If so, then we increment our bribe by 1. This is the equivalent of asking a person on line, if they were bribed by a person in front of them, and them saying "yes."

We can shows this by a step by step example:

    0. Take the standard array input: [2,1,5,3,4]
    1. Make it 0 based: [1,0,4,2,3]
    2. We need to subtract each index value by one so that we ensure we are starting with the first value.
    3. Was 1 bribed? No, because 1 is at the front of the line.
    4. Was 0 bribed? Yes, because 1 is greater than 0. 
    5. Was 4 bribed? No, 0 is not greater than 4. 
    6. Was 2 bribed? Yes, 4 is greater than 2.
    7. Was 3 bribed? Yes, 4 is greater than 3.

Essentially what is occuring is we are starting with the first index and slowly expanding our windows across the array and seeing if the current index is greater than the largest number in the current window.

## Putting it all Together
We can assert the following:

For a given array <i>a</i> where each index can be defined as <i>i<sub>n</sub>. &forall; i<sub>n</sub> &isin; a</i>, let the value of each <i>i<sub>n</sub></i> be defined as <i>n<sub>i</sub></i>. Let <i>a'</i> be defined as { n<sub>i</sub> - 1</i> | <i>n<sub>i</sub> &isin; a &gt; n<sub>i</sub> &isin; a' }</i>. If <i>n<sub>i</sub> - i<sub>n</sub> &isin; a' &gt; 2;</i> determine the array to be "too chaotic." Let the number of bribes be defined as <i>b = 0</i>. For each <i>i<sub>n</sub> &isin; a'</i>, let s  &sub; a' where <i>s = { n<sub>i</sub> - 1...i<sub>n</sub> }</i>. Let the max value in <i>s</i> be defined as <i>m</i>. If <i>m &gt; n<sub>i</sub> &isin; s; b = b+1.
