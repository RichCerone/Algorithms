#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    finalGrades = []
    for grade in grades:
        if grade >= 38 and (5 - grade % 5) < 3:
            finalGrades.append(grade + ( 5 - grade % 5))
        else:
            finalGrades.append(grade)
            
    return finalGrades

if __name__ == '__main__':

    grades = [4, 73, 67, 38, 33]

    result = gradingStudents(grades)

    print(result)