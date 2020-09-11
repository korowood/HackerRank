def maximumToys(prices, k):
    """Complete the function maximumToys in the editor below.
    It should return an integer representing the maximum number of toys Mark can purchase."""
    ans, i = 0, 0
    prices.sort()
    while ans <= k:
        ans += prices[i]
        i += 1
    return i - 1


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)
    print(result)
