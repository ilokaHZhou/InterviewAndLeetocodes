import sys

# 定义四个可能的移动方向：右，左，下，上
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# 使用深度优先搜索（DFS）来探索网格
def dfs(matrix, visited, x, y):
    # 标记当前网格点为已访问
    visited[x][y] = True
    # 初始化当前网格点的范围计数为1
    range = 1
    # 遍历所有可能的移动方向
    for direction in directions:
        newX = x + direction[0]  # 计算新的行坐标
        newY = y + direction[1]  # 计算新的列坐标
        # 检查新坐标是否在网格内部，且未访问过，并且满足编号差值绝对值小于等于1的条件
        if newX >= 0 and newX < len(matrix) and newY >= 0 and newY < len(matrix[0]) \
            and not visited[newX][newY] and abs(matrix[newX][newY] - matrix[x][y]) <= 1:
            # 递归地继续探索并累加可活动的网格点数目
            range += dfs(matrix, visited, newX, newY)
    # 返回从当前网格点出发可活动的最大网格点数目
    return range

# 读取输入数据
m, n = 0, 0  # 初始化网格的行数和列数
matrix = []  # 初始化网格矩阵

# 逐行读取输入
for line in sys.stdin:
    if not m and not n:
        m, n = map(int, line.split())  # 读取网格的行数和列数
    else:
        matrix.append(list(map(int, line.split())))  # 读取网格中的数值
        if len(matrix) == m:  # 如果已经读取完所有行，结束读取
            break

# 寻找机器人可以活动的最大范围
maxRange = 0
for i in range(m):
    for j in range(n):
        visited = [[False] * n for _ in range(m)]  # 初始化访问标记数组
        ranges = dfs(matrix, visited, i, j)  # 对每个网格点执行DFS
        maxRange = max(maxRange, ranges)  # 更新最大活动范围

# 输出机器人可以活动的最大范围对应的网格点数目
print(maxRange)