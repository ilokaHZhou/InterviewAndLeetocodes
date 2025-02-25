from collections import deque

# 读取迷宫的行数和列数
m, n = map(int, input().split())
# 初始化迷宫矩阵
maze = []
for _ in range(m):
    row = list(map(int, input().split()))
    maze.append(row)

# 定义四个方向：上、下、左、右
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 初始化访问标记矩阵，用于记录每个位置是否已经访问过
visited = [[False] * n for _ in range(m)]
# 初始化队列，用于广度优先搜索，队列元素为 (x, y, path)，path 记录到达该点的路径
queue = deque([(0, 0, [(0, 0)])])
# 标记起点已访问
visited[0][0] = True

while queue:
    # 从队列中取出当前位置和路径
    x, y, path = queue.popleft()
    # 如果到达终点
    if x == m - 1 and y == n - 1:
        # 输出路径
        for p in path:
            print(f"({p[0]},{p[1]})")
        break
    # 遍历四个方向
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        # 检查新位置是否在迷宫范围内，是否为通路且未被访问过
        if 0 <= new_x < m and 0 <= new_y < n and maze[new_x][new_y] == 0 and not visited[new_x][new_y]:
            # 标记新位置已访问
            visited[new_x][new_y] = True
            # 生成新的路径
            new_path = path + [(new_x, new_y)]
            # 将新位置和路径加入队列
            queue.append((new_x, new_y, new_path))