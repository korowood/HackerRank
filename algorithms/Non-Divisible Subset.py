import os


def non_divisible_subset(k, s):
    """вход: два числа и строка
     n - количество элементов, k - делитель
     s - строка
     выход: количество элементов, сумма которых делится на делитель
     """
    array_of_sum = [0] * k
    for x in s:
        array_of_sum[x % k] += 1
    count = min(array_of_sum[0], 1)
    for i in range(1, k // 2 + 1):
        if i != k - i:
            count += max(array_of_sum[i], array_of_sum[k - i])
    if k % 2 == 0:
        count += 1

    print(count)
    return count

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'test.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = non_divisible_subset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
