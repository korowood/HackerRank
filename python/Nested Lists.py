if __name__ == '__main__':
    N = int(input())
    name = [0] * N
    score = [0] * N
    for i in range(N):
        name[i] = input()
        score[i] = float(input())
    # print(name)

    # name = ['govno40', 'loh30', 'pidr50', 'chelik40']
    # score = [40, 30, 50, 40]
    name_score = [0] * N
    for i in range(N):  # создаем кортеж
        name_score[i] = [name[i], score[i]]
    # print(name_score)

    minimum_score = 0
    index_min_score = 0
    for i in range(N-1):  # находим мин значение и индекс
        if name_score[i][1] < name_score[i + 1][1]:
            minimum_score = name_score[i][1]
            index_min_score = i
    # print(minimum_score, index_min_score)

    sorted_name_score = sorted(name_score, key=lambda student: student[1])  # сортируем по балу
    # print(sorted(name_score, key=lambda student: student[1]))

    i = 0
    while minimum_score == sorted_name_score[0][1]:
        sorted_name_score.pop([i][i])
        i += 1
    # print(sorted_name_score)

    minimum_score = sorted_name_score[0][1]
    # print(minimum_score)

    sorted_name_score = sorted(sorted_name_score, key=lambda student: student[0])  # сортируем по алфавиту
    # print(sorted_name_score)

    for i in range(len(sorted_name_score)):
        if sorted_name_score[i][1] == minimum_score:
            print(sorted_name_score[i][0])


# плохо работает. Ниже все работает

# marksheet = []
# for _ in range(0, int(input())):
#     marksheet.append([input(), float(input())])
#
# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print('\n'.join([a for a, b in sorted(marksheet) if b == second_highest]))