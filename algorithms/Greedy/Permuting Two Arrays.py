def twoArrays(k, A, B):
    """Complete the twoArrays function in the editor below. It should return a string, either YES or NO"""
    A.sort()
    B.sort(reverse=True)
    print(zip(A, B))
    if any(a + b < k for a, b in zip(A, B)):
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)
        print(result)
