# Problem Description
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. In the diagram below, the red region denotes his house, where <i><b>s</b></i> is the start point, and <i><b>t</b></i> is the endpoint. The apple tree is to the left of his house, and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point <i><b>a</b></i>, and the orange tree is at point <i><b>b</b></i>.

<img src="https://s3.amazonaws.com/hr-challenge-images/25220/1474218925-f2a791d52c-Appleandorange2.png" alt="NOT FOUND">

When a fruit falls from its tree, it lands <i><b>d</b></i> units of distance from its tree of origin along the <i><b>x</b></i>-axis. A negative value of <i><b>d</b></i> means the fruit fell <i><b>d</b></i> units to the tree's left, and a positive value of <i></b>d</b></i> means it falls <i><b>d</b></i> units to the tree's right.

Given the value of <i><b>d</b></i> for <i><b>m</b></i> apples and <i><b>n</b></i> oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range [<i><b>s</b></i>, <i><b>t</b></i>])?

For example, Sam's house is between <i><b>s = 7</b></i> and <i><b>t = 10</i></b>. The apple tree is located at <i><b>a = 4</b></i> and the orange at <i><b>b = 12</b></i>. There are <i><b>m = 3</b></i> apples and <i><b>n = 3</b></i> oranges. Apples are thrown <i><b>apples</i></b> = [<b>2,3,-4</b>] units distance from <i><b>a</b></i>, and <i><b>oranges</i></b> = [<b>3,-2,-4</b>] units distance. Adding each apple distance to the position of the tree, they land at [<b>4</b> + <b>2</b>, <b>4</b> + <b>3</b>, <b>4</b> + -<b>4</b>] = [<b>6,7,0</b>]. Oranges land at [<b>12 + 3</b>, <b>12 + -2</b>, <b>12 + -4</b>] = [<b>15,10,8</b>]. One apple and two oranges land in the inclusive range <b>7 - 10</b> so we print

    1
    2

<b>Function Description</b>

Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges that land on Sam's house, each on a separate line.

countApplesAndOranges has the following parameter(s):

- s: integer, starting point of Sam's house location.
- t: integer, ending location of Sam's house location.
- a: integer, location of the Apple tree.
- b: integer, location of the Orange tree.
- apples: integer array, distances at which each apple falls from the tree.
- oranges: integer array, distances at which each orange falls from the tree.

<b>Input Format</b>

The first line contains two space-separated integers denoting the respective values of <b><i>s</i></b>
and <i><b>t</b></i>.
The second line contains two space-separated integers denoting the respective values of <i><b>a</b></i> and <i><b>b</b></i>.
The third line contains two space-separated integers denoting the respective values of <i><b>m</b></i> and <i><b>n</b></i>.
The fourth line contains space-separated integers denoting the respective distances that each apple falls from point <i><b>a</b></i>.
The fifth line contains space-separated integers denoting the respective distances that each orange falls from point <i><b>b</b></i>.

<b>Constraints</b>
- <b>1</b> &le; <i><b>s,t,a,b,m,n</b></i> &le; <b>10<sup>5</sup></b>
- <b>-10<sup>5</sup></b> &le; <i><b>d</b></i> &le; <b>10<sup>5</sup></b>
- <i><b>a</b></i> &lt; <i><b>s</b></i> &lt; <i><b>t</b></i> &lt; <i><b>b</b></i>

<b>Output Format</b>

Print two integers on two different lines:

1. The first integer: the number of apples that fall on Sam's house.
2. The second integer: the number of oranges that fall on Sam's house.

<b>Sample Input 0</b>

    7 11
    5 15
    3 2
    -2 2 1
    5 -6

<b>Sample Output 0</b>

    1
    1

# How To Solve This Problem
This problem isn't hard to solve, but it does try to trick you by giving you a lot of information at once. I personally think this is a good problem to help demonstrate whether you can follow directions and pick out the useful informaton from the useless.

Let's break down this problem to what is actually important:
- The house coordinates are given as <i><b>s</b></i> and <i><b>t</b></i> to be a set [<i><b>s,t</b></i>]. 
- The apple and orange tree start at a single <i>x</i>-coordinate position on the <i>x</i>-axis given as <i><b>a</b></i> and <i><b>b</b></i>.
- The number of apples thrown are given as <i><b>m</b></i> and <i><b>n</b></i>.

All this question is really asking is that given the throwing distances of each apple and orange, do they land within [<i><b>s</b></i>, <i><b>t</b></i>] inclusive. 

The only other thing to note is that the original throw distance needs to be added by the <i><b>a</b></i> or <i><b>b</b></i> (depending on whether it is an apple or orange).

## Putting it all Together
We can assert the following:

A house coordinates is defined as <i><b>s</b></i> and <i><b>t</b></i> such that <i><b>s</b></i> is the starting poistion of the house and <i><b>t</b></i> is the ending postion of the house given as [<i><b>s</b></i>, <i><b>t</b></i>] on the <i>x</i>-axis. Let the single <i>x</i>-coordinate of the apple tree be represented as <i><b>a</b></i> and the single <i>x</i>-coordinate of the orange tree be represented as <i><b>b</b></i>. Let the number of apples thrown be represented as <i><b>m</b></i> and the number of oranges be represented as <i><b>n</b></i>. The <i>x</i>-coordinate of each apple thrown is represented as a set <i><b>a<sub>c</sub></b></i> and the <i>x</i>-coordinate of each orange thrown is represented as a set <i><b>b<sub>c</sub></b></i>. Let <i><b>a<sub>i</sub></b></i> &isin; <i><b>a<sub>c</sub></b></i> be added with the <i>x</i>-coordinate of the apple tree <i><b>a</b></i> and let <i><b>b<sub>i</sub></b></i> &isin; <i><b>b<sub>c</sub></b></i> be added with the <i>x</i>-coordinate of the orange tree <i><b>b</b></i>. If <i><b>a<sub>i</sub></b></i> &isin; [<i><b>s</b></i>, <i><b>t</b></i>] or <b><i>b<sub>i</sub></b></i> &isin; [<i><b>s</b></i>, <i><b>t</b></i>] inclusive, then count that apple or orange as landing within the house.  