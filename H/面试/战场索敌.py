import sys

def dfs(i, j):
    visited[i][j] = 1  # 标记当前位置已访问

    if matrix[i][j] == 'E':  # 如果当前位置是敌人，增加敌人数量
        global enemyCount
        enemyCount += 1

    offsets = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 定义上下左右四个方向

    # 遍历四个方向，检查相邻格子
    for offset in offsets:
        newX = i + offset[0]
        newY = j + offset[1]

        # 检查相邻格子是否在范围内、未访问且不是墙壁
        if newX >= 0 and newX < n and newY >= 0 and newY < m and visited[newX][newY] == 0 and matrix[newX][newY] != '#':
            dfs(newX, newY)  # 递归访问相邻格子

# 读取地图行数、列数和目标敌人数量
n, m, k = map(int, input().split())

matrix = []  # 初始化地图矩阵
visited = [[0] * m for _ in range(n)]  # 初始化访问标记数组

# 读取地图数据
for _ in range(n):
    row = input()
    matrix.append(list(row))

ans = 0  # 初始化符合条件的区域计数

# 遍历地图的每个格子
for i in range(n):
    for j in range(m):
        # 如果该格子已访问或是墙壁，跳过
        if visited[i][j] != 0 or matrix[i][j] == '#':
            continue
        enemyCount = 0  # 初始化敌人数量
        dfs(i, j)  # 深度优先搜索
        # 如果该区域敌人数小于k，则符合条件
        ans += 1 if enemyCount < k else 0

# 输出符合条件的区域数量
print(ans)