#!/bin/python3

import math
import os
import random
import re
import sys

def minimumBribes(q):
    for i in range(len(q)):
        q[i] = q[i] - 1

    bribes = 0
    for i in range(len(q)):
        if q[i] - i > 2:
            print("Too chaotic")
            return
        
        for j in range(max(q[i] - 1, 0), i):
            if(q[j] > q[i]):
                bribes += 1
        
    print(bribes)

if __name__ == '__main__':

    q = [2,1,5,3,4]

    minimumBribes(q)
