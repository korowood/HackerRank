def gradingStudents(grades):
    return [elem + (5 - (elem % 5)) if (elem > 37 and elem % 5 != 0 and elem % 5 >= 3) else elem for elem in grades]


if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(*result)
