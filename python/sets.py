def add_set():
    """
    If we want to add a single element to an existing set, we can use the .add() operation.
    It adds the element to the set and returns 'None'.
    Input: The first line contains an integer N, the total number of country stamps.
    The next N lines contains the name of the country where the stamp is from.
    Output: Output the total number of distinct country stamps on a single line.
    """
    s = set()
    for _ in range(int(input())):
        s.add(input())

    return print(len(s))


def average(array):
    """
    среднее значение массива
    """
    return sum(set(array)) / len(set(array))


def test_average():
    arr = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
    n = 10
    average(arr)
    print(average(arr))


test_average()


# без теста
# n = int(input())
# arr = list(map(int, input().split()))
# result = average(arr)
# print(result)

def union():
    """обьеденить множество А и В"""
    _, n, _, b = (set(input().split()) for _ in range(4))
    return print(len(n | b))


# union()

def check_subset():
    """ Проверить является ли А подмассивом В
    1 строка - количество тестов
    2 строка - размерность А
    3 строка - массив А
    4 строка - размерность В
    5 строка - массив В
    """
    T = int(input())
    for _ in range(T):
        _, a, _, b = input(), set(input().split()), input(), set(input().split())
        print(a.issubset(b))


# check_subset()

def discard_pop_remove():
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())
    a = set()
    for i in range(N):
        command = list(map(str, input().split()))
        if command[0] == ['remove']:
            a = s.remove(int(command[1]))
    print(list(a))


# discard_pop_remove()
s = set(map(int, input().split()))
s = s.remove(4)
print()