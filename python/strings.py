def string_validation_1():
    """
    In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
    In the second line, print True if S has any alphabetical characters. Otherwise, print False.
    In the third line, print True if S has any digits. Otherwise, print False.
    In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
    In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
    """
    S = input()
    print(any(c.isalnum() for c in S))
    print(any(c.isalpha() for c in S))
    print(any(c.isdigit() for c in S))
    print(any(c.islower() for c in S))
    print(any(c.isupper() for c in S))


def string_validation_2():
    """Тоже самое"""
    S = input()
    for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        print(any(eval("c." + test + "()") for c in S))


def string_validation_3():
    """Тоже самое"""
    S = input()
    t = type(S)
    for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
        print(any(method(c) for c in S))


def capitalize_1():
    """написать слова с большой буквы"""
    s = input()
    return print(s.title())  # тест - 1 w 2 r 3g - не работает


def capitalize_2():
    s = input()
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return print(s)

capitalize_2()