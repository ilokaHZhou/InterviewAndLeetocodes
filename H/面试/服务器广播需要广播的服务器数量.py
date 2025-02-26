import sys

# 深度优先搜索函数，递归遍历图中与当前服务器相连的所有服务器
def dfs(arr, visited, index):
    visited[index] = True  # 标记当前服务器为已访问
    flag = True  # 标记是否存在相连的服务器
    for i in range(index + 1, len(arr)):  # 遍历所有服务器
        if arr[index][i] == 1:  # 如果当前服务器与服务器 i 相连
            flag = False  # 发现相连的服务器，设置 flag 为 False
            dfs(arr, visited, i)  # 递归搜索与服务器 i 相连的所有服务器
    if flag:  # 如果没有发现相连的服务器，即 flag 仍为 True
        global count  # 使用全局变量 count 计数
        count += 1  # 说明这是一个新的连通分量，计数加 1

# 初始化计数器
count = 0

# 读取输入的第一行，表示服务器的连接矩阵的第一行
str = input().split(" ")
n = len(str)  # 服务器的数量，也就是矩阵的维度

# 初始化 n*n 的二维数组 arr 来存储服务器连接状态
arr = [[0]*n for _ in range(n)]

# 将第一行数据存入 arr 的第一行
for i in range(n):
    arr[0][i] = int(str[i])

# 读取剩下的行并存入 arr 中
for i in range(1, n):
    s = input().split(" ")
    for j in range(n):
        arr[i][j] = int(s[j])

# 初始化 visited 数组，用来标记每个服务器是否已经被访问
visited = [False] * n

# 遍历每个服务器，执行 DFS 查找连通分量
for i in range(n):
    if not visited[i]:  # 如果该服务器没有被访问
        dfs(arr, visited, i)  # 递归查找所有与该服务器相连的服务器

# 输出连通分量的数量，即需要广播的服务器数量
print(count)