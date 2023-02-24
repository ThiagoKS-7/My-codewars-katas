#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fourthBit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER number as parameter.
#

def fourthBit(number:int) -> int:
    res = ""
    while number  >0:
        res+=str(number % 2)
        number =number // 2
    return res[::-1][-4]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    number = int(input().strip())

    result = fourthBit(number)

    fptr.write(str(result) + '\n')

    fptr.close()
