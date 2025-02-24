def sort_students(n, order, students):
    # 如果 order 是 1，按成绩升序排序；否则按成绩降序排序
    if order == 1:
        sorted_students = sorted(students, key=lambda x: x[1])
    else:
        sorted_students = sorted(students, key=lambda x: -x[1])
    return sorted_students


# 输入处理
n = int(input())
order = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append((name, int(score)))

# 排序
sorted_students = sort_students(n, order, students)

# 输出结果
for student in sorted_students:
    print(student[0], student[1])
