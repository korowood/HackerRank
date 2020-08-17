from itertools import product
from itertools import combinations_with_replacement
from itertools import combinations
from itertools import groupby
from itertools import permutations


def direct_product():
    """ прямое произведение А на В"""
    A = [int(x) for x in input().split()]
    B = [int(y) for y in input().split()]
    return print(*product(A, B))


# direct_product()

def two_combination_word():
    """ввод: слово и через пробел число - количество комбинаций букв в числе"""
    s, k = input().split()
    for c in combinations_with_replacement(sorted(s), int(k)):
        print("".join(c))


# two_combination_word()


def two_combination_letter():
    """ВВод: слово и цифра через пробел. Вывод: буквы и комбинации букв в слове"""
    s, k = input().split()
    for i in range(1, int(k) + 1):
        for j in combinations(sorted(s), i):
            print(''.join(j))


# two_combination_letter()

def group_by_symbol():
    """Ввод: строка чисел. Вывод: количество каждой цифры"""
    return print(*[(len(list(c)), int(k)) for k, c in groupby(input())])


# group_by_symbol()


def letter_permutations():
    """перестановка всех букв в слове"""
    s, k = input().split()
    for c in permutations(sorted(s), int(k)):
        print("".join(c))


letter_permutations()
