import math
import os
import random
import re
import sys


def insertionSort1(n, arr):
    for i in range(len(arr) - 1):
        x = arr[i]
        j = i
        while j > 0 and arr[j - 1] > x:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = x
    print(arr)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    # for _ in range(n - 1):
    #     if arr[_] > arr[_ + 1]:
    #         tmp = arr[_ + 1]
    #         indx_tmp = _ + 1
    #
    # for __ in range(indx_tmp, -1, -1):
    #     if tmp <= arr[__ - 1]:
    #         arr[__] = arr[__ - 1]
    #         print(*arr)
    #         ss = __ - 1
    #     else:
    #         arr[ss] = tmp
    #         break
    # arr[ss] = tmp
    # print(*arr)
