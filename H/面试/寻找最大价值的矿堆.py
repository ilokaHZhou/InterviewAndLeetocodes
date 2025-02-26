from collections import deque

# 地图矩阵
map = []

# 上下左右，四个方向的偏移量
offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 读入地图信息
lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except:
        break

# 构建地图矩阵
rows = len(lines)
cols = len(lines[0])
map = [[0 for j in range(cols)] for i in range(rows)]
for i in range(rows):
    line = lines[i]
    for j in range(cols):
        map[i][j] = int(line[j])

# 记录最大矿堆价值
maxVal = 0

# 遍历地图矩阵
for i in range(rows):
    for j in range(cols):
        # 如果点(i,j)没有被访问过，且点(i,j)上有矿，则进入深搜
        if map[i][j] > 0:
            stack = deque()
            stack.append((i, j))

            sum = 0

            while stack:
                pos = stack.pop()
                x, y = pos

                sum += map[x][y]
                map[x][y] = 0

                # 遍历四个方向
                for offset in offsets:
                    newX = x + offset[0]
                    newY = y + offset[1]

                    # 如果新位置在地图范围内，且有矿，则加入栈中
                    if newX >= 0 and newX < rows and newY >= 0 and newY < cols and map[newX][newY] > 0:
                        stack.append((newX, newY))

            # 更新最大矿堆价值
            maxVal = max(maxVal, sum)

print(maxVal)
