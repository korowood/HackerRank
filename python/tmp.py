
N = int(input())

arr_x = [0] * N
arr_y = [0] * N
if N % 4 == 1:
    x, y = -1, 0
    for i in range(0, N, 4):
        arr_x[i] = x
        arr_y[i] = y
        x -= 1
        y -= 1
if N % 4 == 2:
    x, y = -1, 1
    for i in range(1, N, 4):
        arr_x[i] = x
        arr_y[i] = y
        x -= 1
        y += 1
if N % 4 == 3:
    x, y = 1, 1
    for i in range(2, N, 4):
        arr_x[i] = x
        arr_y[i] = y
        x += 1
        y += 1
if N % 4 == 0:
    x, y = 1, -1
    for i in range(3, N, 4):
        arr_x[i] = x
        arr_y[i] = y
        x += 1
        y -= 1
print(arr_x[N - 1])
print(arr_y[N - 1])
