import os

#КАКОГО ХУФ НЕ РАБОТАЕТ
# def angry_professor(k, a):
#     count_student = 0
#     answer = 'NO'
#     for i in range(len(a)):
#         if a[i] > 0:
#             count_student += 1
#     if k > count_student:
#         answer = 'YES'
#
#     return answer


def angry_professor(k, a):
    return "NO" if len([1 for x in a if x <= 0]) >= k else "YES"


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'test.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angry_professor(k, a)

        fptr.write(result + '\n')

    fptr.close()
