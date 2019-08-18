#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    if d == len(a):
        return a
    
    rotatedArray = []
    
    after = d
    while after < len(a):
        rotatedArray.append(a[after])
        after += 1

    before = 0
    while before < d:
        rotatedArray.append(a[before])
        before += 1

    return rotatedArray

if __name__ == '__main__':

    d = 4

    a = [1,2,3,4,5]

    result = rotLeft(a, d)
    print(result)