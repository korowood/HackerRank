#!/bin/python3

import math
import os
import random
import re
import sys


def maximumPerimeterTriangle(sticks):
    A = sorted(sticks)

    i = n - 3
    while i >= 0 and (A[i] + A[i + 1] <= A[i + 2]):
        i -= 1

    if i >= 0:
        return (A[i], A[i + 1], A[i + 2])
    else:
        return (-1)



if __name__ == '__main__':


    n = int(input())

    sticks = list(map(int, input().rstrip().split()))
    result = maximumPerimeterTriangle(sticks)

    print(result)

