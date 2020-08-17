# def max_sub_sum(A: list, T: int):
#     A_sorted = A.sort()
#     for i in range(len(A)):
#         for j in range(len(A) - 1):
#             track_1 = A[i]
#             track_2 = A[j]
#             if abs(track_1 + track_2) <= T:
#                 m = track_1 + track_2
#                 print(A[i], A[j])
#     return m
# Arr = [3, 3, 9, 9, 5]
# T = 8
# max_sub_sum(Arr, T)
# def test_max_sub_sum():
#     A1 = [3, 3, 9, 9, 5]
#     T = 7
#     m = max_sub_sum(A1, T)
#     if m == 6:
#         print("Tested")
#     else:
#         print(" Failed")


# test_max_sub_sum()

import math
import os
import random
import re
import sys


def maximumSum(a, m):
    arr_sorted = sorted(a)


    for i in range(len(arr_sorted) // 2):
        for j in range((len(arr_sorted) - 1) // 2, 1, -1):
            if m >= abs(arr_sorted[i] + arr_sorted[j]):
                word_1 = arr_sorted[i]
                word_2 = arr_sorted[j]


    return print()


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'test.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()
