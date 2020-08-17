import math
import os
import random
import re
import sys


# Complete the rotLeft function below.
def rotLeft(a, d):
    return a[d:] + a[:d]

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'test.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nd = input().split()
    #
    # n = int(nd[0])
    #
    # d = int(nd[1])
    #
    # a = list(map(int, input().rstrip().split()))

    d = 2
    a = [1, 2, 3, 4, 5]

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
