import math

n, m = map(int, input().split()) # 读取要填充的数字个数n和矩阵的行数m
cols = math.ceil(n / m) # 计算矩阵的列数
matrix = [[0 for _ in range(cols)] for _ in range(m)] # 创建一个整型矩阵，默认初始化为0

num = 1 # 用于填充的数字从1开始
top, bottom, left, right = 0, m - 1, 0, cols - 1
while num <= n:
    for i in range(left, right + 1): # 从左到右填充上边界
        if num <= n:
            matrix[top][i] = num
            num += 1
    top += 1 # 上边界下移
    for i in range(top, bottom + 1): # 从上到下填充右边界
        if num <= n:
            matrix[i][right] = num
            num += 1
    right -= 1 # 右边界左移
    for i in range(right, left - 1, -1): # 从右到左填充下边界
        if num <= n:
            matrix[bottom][i] = num
            num += 1
    bottom -= 1 # 下边界上移
    for i in range(bottom, top - 1, -1): # 从下到上填充左边界
        if num <= n:
            matrix[i][left] = num
            num += 1
    left += 1 # 左边界右移

for row in matrix: # 遍历矩阵的每一行
    print(' '.join('*' if val == 0 else str(val) for val in row)) # 如果当前位置是0，则输出'*'，否则输出当前位置的数字