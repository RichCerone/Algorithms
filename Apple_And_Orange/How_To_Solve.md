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
