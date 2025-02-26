from collections import deque

# 读取棋盘的行数和列数
m, n = map(int, input().split())
# 初始化棋盘数组，虽然在这个程序中没有直接使用棋盘数据
board = [[0] * n for _ in range(m)]

# 存储每个马的位置和它们的最大移动步数
horses = []
for i in range(m):
    line = input().split()
    for j in range(n):
        if line[j] != '.':
            # 如果位置不是空点，则记录马的位置和初始步数
            horses.append((i, j, int(line[j])))

def bfs():
    # 马可以移动的八个方向
    directions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
    # 初始化最小步数为无穷大
    min_steps = float('inf')

    # 遍历棋盘上的每一个位置作为目标位置
    for i in range(m):
        for j in range(n):
            steps = 0
            possible = True

            # 遍历每个马
            for horse in horses:
                queue = deque([(horse[0], horse[1], 0)])
                visited = set()
                visited.add((horse[0], horse[1]))
                found = False

                # 使用 BFS 寻找每个马到目标位置的最短路径
                while queue and possible:
                    x, y, dist = queue.popleft()
                    if (x, y) == (i, j):
                        steps += dist
                        found = True
                        break

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        # 检查新位置是否有效，并且未被访问过
                        if 0 <= nx < m and 0 <= ny < n and dist < horse[2] and (nx, ny) not in visited:
                            queue.append((nx, ny, dist + 1))
                            visited.add((nx, ny))
                
                # 如果找不到路径，则此目标位置不可达
                if not found:
                    possible = False
            
            # 如果所有马都可以到达此位置，更新最小步数
            if possible:
                min_steps = min(min_steps, steps)
    
    # 如果找不到任何可行的解决方案，则返回0，否则返回最小步数
    return 0 if min_steps == float('inf') else min_steps

# 打印广度优先搜索的结果
print(bfs())
