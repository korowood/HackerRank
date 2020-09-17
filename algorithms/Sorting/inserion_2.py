import math
import os
import random
import re
import sys


# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for top in range(1, n):
        k = top
        while k > 0 and arr[k - 1] > arr[k]:
            arr[k], arr[k - 1] = arr[k - 1], arr[k]
            k -= 1
        print(arr)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
