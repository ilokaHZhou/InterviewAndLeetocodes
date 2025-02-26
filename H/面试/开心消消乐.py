def dfs(matrix, x, y):
    matrix[x][y] = 0 # 将当前位置的值设为0，表示已经遍历过
    rows, cols = len(matrix), len(matrix[0]) # 矩阵的行数和列数
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)] # 定义8个方向的偏移量
    for dir in directions: # 遍历8个方向
        nextX, nextY = x + dir[0], y + dir[1] # 计算下一个位置的行坐标和列坐标
        if 0 <= nextX < rows and 0 <= nextY < cols and matrix[nextX][nextY] == 1: # 如果下一个位置在矩阵范围内且值为1
            dfs(matrix, nextX, nextY) # 对下一个位置进行深度优先遍历
rows, cols = map(int, input().split()) # 输入矩阵的行数和列数
matrix = [] # 定义一个空列表存放矩阵
for i in range(rows): # 遍历矩阵的每一行
    row = list(map(int, input().split())) # 读入矩阵的每一行
    matrix.append(row) # 将每一行添加到矩阵中

result = 0 # 定义结果变量，表示矩阵中1的连通块数量
for i in range(rows): # 遍历矩阵的每一行
    for j in range(cols): # 遍历矩阵的每一列
        # 从任意一个位置的1开始遍历
        if matrix[i][j] == 1: # 如果当前位置是1
            result += 1 # 连通块数量加1
            dfs(matrix, i, j) # 对以当前位置为起点的连通块进行深度优先遍历

print(result) # 输出矩阵中1的连通块数量