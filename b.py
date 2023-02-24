#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'newPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def newPassword(a:str, b:str):
    res = ""
    if len(a) >= len(b):
        for i in range(len(a)):
            if i >= len(b):
                res+= a[i]
            else:
                res+= (a[i] + b[i])
    else:
        for i in range(len(b)):
            if i >= len(a):
                res+= b[i]
            else:
                res+= (a[i] + b[i])            
    return res

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    result = newPassword(a, b)

    fptr.write(result + '\n')

    fptr.close()
