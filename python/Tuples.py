"""создать кортеж и использовать хэш на него"""

n = int(input())
integer_list = map(int, input().split())

print(tuple(integer_list).__hash__())
