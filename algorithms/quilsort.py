def quickSort(arr):
    if len(arr) <= 1:
        return arr
    barrier = arr[0]
    L = []
    M = []
    R = []
    for x in arr:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)

    k = 0

    for x in L + M + R:
        arr[k] = x

        k += 1


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    quickSort(arr)
    print(arr)

# badbadbad!!!!