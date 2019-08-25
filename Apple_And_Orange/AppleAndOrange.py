#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    numOfApples = 0
    numOfOranges = 0

    for i in range(len(apples)):
        landed = apples[i] + a
        if landed >= s and landed <= t:
            numOfApples += 1
    
    print(numOfApples)

    for i in range(len(oranges)):
        landed = oranges[i] + b
        if landed >= s and landed <= t:
            numOfOranges += 1

    print(numOfOranges)    
    

if __name__ == '__main__':

    s = 7
    t = 11
    a = 5
    b = 15
    apples = [-2, 2, 1]
    oranges = [5, -6]   

    countApplesAndOranges(s, t, a, b, apples, oranges)