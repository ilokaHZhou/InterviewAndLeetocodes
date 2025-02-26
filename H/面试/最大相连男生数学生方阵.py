def get_max_connected(students, row, column, res):
    length = 1  # 初始化连续的M的个数为1
    a, b = 0, 0  # 初始化行和列的索引
    m, n = len(students), len(students[0])  # 获取方阵的行数和列数

    if column < n:  # 从左往右搜索
        a = row
        b = column
        while b < n - 1 and students[a][b + 1] == "M":  # 不越界且下一个元素为M
            b += 1
            length += 1  # 连续的M的个数加1
        res.append(length)  # 把连续的M的个数加入结果数组
        length = 1  # 重新初始化连续的M的个数为1

    if row < m:  # 从上往下搜索
        a = row
        b = column
        while a < m - 1 and students[a + 1][b] == "M":  # 不越界且下一个元素为M
            a += 1
            length += 1  # 连续的M的个数加1
        res.append(length)  # 把连续的M的个数加入结果数组
        length = 1  # 重新初始化连续的M的个数为1

    if row < m and column < n:  # 对角线搜索
        a = row
        b = column
        while a < m - 1 and b < n - 1 and students[a + 1][b + 1] == "M":  # 不越界且下一个元素为M
            a += 1
            b += 1
            length += 1  # 连续的M的个数加1
        res.append(length)  # 把连续的M的个数加入结果数组
        length = 1  # 重新初始化连续的M的个数为1

    if row >= 0 and column < n:  # 从右往左搜索
        a = row
        b = column
        while a > 0 and b < n - 1 and students[a - 1][b + 1] == "M":  # 不越界且下一个元素为M
            a -= 1
            b += 1
            length += 1  # 连续的M的个数加1
        res.append(length)  # 把连续的M的个数加入结果数组


if __name__ == "__main__":
    input_str = input().strip()
    row, column = map(int, input_str.split(","))

    # 初始化方阵
    students = []
    for _ in range(row):
        student_str = input().strip()
        students.append(student_str.split(","))

    max_res = []  # 初始化结果数组
    for i in range(row):
        for j in range(column):
            if students[i][j] == "M":
                get_max_connected(students, i, j, max_res)  # 在四个方向上搜索连续的M

    max_res.sort(reverse=True)  # 对结果数组排序
    print(max_res[0])  # 输出最大的连续的M的个数



import sys

# 定义四个方向的增量，分别表示：水平、垂直、对角线、反对角线
DIRECTIONS = [
    (0, 1), (1, 0), (1, 1), (-1, 1)
]

def getMaxConnected(students, row, column, res):
    m = len(students)
    n = len(students[0])

    for dir in DIRECTIONS:
        len_m = 1  # 初始化连续的M的个数为1
        a, b = row, column

        # 按当前方向搜索
        while (0 <= a + dir[0] < m) and (0 <= b + dir[1] < n) and students[a + dir[0]][b + dir[1]] == "M":
            a += dir[0]  # 更新行索引
            b += dir[1]  # 更新列索引
            len_m += 1  # 连续的M的个数加1

        res.append(len_m)  # 把连续的M的个数加入结果数组

if __name__ == "__main__":
    input_str = input().strip()
    row, column = map(int, input_str.split(","))

    # 初始化方阵
    students = []
    for _ in range(row):
        student_str = input().strip()
        students.append(student_str.split(","))

    max_res = []  # 初始化结果数组
    for i in range(row):
        for j in range(column):
            if students[i][j] == "M":
                getMaxConnected(students, i, j, max_res)  # 在四个方向上搜索连续的M

    max_res.sort(reverse=True)  # 对结果数组排序
    print(max_res[0])  # 输出最大的连续的M的个数