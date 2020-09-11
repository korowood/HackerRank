def maxMin(k, arr):
    arr.sort()
    return min([arr[x+k-1]-arr[x] for x in range(n-k+1)])


if __name__ == '__main__':

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)
    print(result)
