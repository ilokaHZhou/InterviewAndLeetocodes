import sys

grid = []  # 网格
for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    else:
        row = line.split()
        grid.append(row)

rows = len(grid)
cols = len(grid[0])

q = []  # 存储已经改造的位置
toConvert = 0  # 需要改造的位置数

for r in range(rows):
    for c in range(cols):
        val = grid[r][c]
        if val == "YES":
            q.append([r, c])
        elif val == "NO":
            toConvert += 1

if not q:  # 如果没有已经改造的位置，则无法继续改造
    print(-1)
    sys.exit()
if len(q) == rows * cols:  # 如果所有位置都已经改造，则不需要继续改造
    print(0)
    sys.exit()

days = 0  # 改造天数
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 上下左右四个方向

while q and toConvert > 0:  # 只要还有需要改造的位置，就继续改造
    new_q = []  # 存储新改造的位置

    for pos in q:
        x, y = pos
        for dir in dirs:
            new_x = x + dir[0]
            new_y = y + dir[1]

            if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == "NO":  # 如果新位置可以改造，就改造它
                grid[new_x][new_y] = "YES"
                new_q.append([new_x, new_y])
                toConvert -= 1

    days += 1  # 改造天数加一
    q = new_q  # 更新已经改造的位置

if toConvert == 0:
    print(days)  # 如果所有位置都已经改造，则返回改造的天数
else:
    print(-1)  # 否则返回-1