
def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    ans = 0
    for i in range(len(calorie)):
        ans += calorie[i] * 2 ** i
    return ans


if __name__ == '__main__':
    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)
    print(result)
