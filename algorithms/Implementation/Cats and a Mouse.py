def catAndMouse(x, y, z):
    return "Cat A" if abs(x - z) < abs(y - z) else "Cat B" if abs(y - z) < abs(x - z) else "Mouse C"


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)
