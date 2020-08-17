def pangrams(s):
    temp_set = set()
    s = ''.join(s.lower().split())
    for word in s:
        temp_set.add(word)
    if len(temp_set) == 26:
        return print('pangram')
    else:
        return print("not pangram")


if __name__ == '__main__':
    st = input()
    pangrams(st)

# We promptly judged antique ivory buckles for the next prize
