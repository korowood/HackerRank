import numpy
import numpy as np


def arrays(arr):
    # revrser array first, convert to float array with numpy
    return (numpy.array(arr[::-1], float))


# arr = input().strip().split(' ')
# result = arrays(arr)
# print(result)


def summ_two_array():
    """
    Input:
    The first line contains space separated integers M, N and P.
    The next N lines contains the space separated elements of the P columns.
    After that, the next M lines contains the space separated elements of the P columns.
    Output:
    Print the concatenated array of size (N+P)xM.
    """
    a, b, c = map(int, input().split())
    arrA = np.array([input().split() for _ in range(a)], int)
    arrB = np.array([input().split() for _ in range(b)], int)

    return print(np.concatenate((arrA, arrB), axis=0))


# summ_two_array()

def shape_and_reshape():
    """можно задавать таким образом матрицы"""
    arr = numpy.array(list(map(int, input().split())))
    return print(arr.reshape(3, 3))
