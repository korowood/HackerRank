def countingSort(arr):
    massive = [0] * 100
    for _ in arr:
        massive[_] += 1
    arr.clear()
    for i in range(100):
        arr += [i] * massive[i]
    return arr


if __name__ == '__main__':
    n = int(input())

    input = list(map(int, input().rstrip().split()))

    print(countingSort(input))