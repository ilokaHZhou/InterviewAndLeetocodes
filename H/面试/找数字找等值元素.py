import sys
from collections import defaultdict

# 读取输入的行数和列数
n = int(input())
m = int(input())

# 读取矩阵数据
matrix = [list(map(int, input().split())) for _ in range(n)]

# 用字典记录每个数字出现的位置
posMap = defaultdict(list)

# 遍历矩阵，记录每个数字的位置
for i in range(n):
    for j in range(m):
        num = matrix[i][j]
        posMap[num].append((i, j))

# 初始化结果矩阵
result = [[-1] * m for _ in range(n)]

# 遍历矩阵中的每个元素，计算到最近的相同元素的距离
for i in range(n):
    for j in range(m):
        num = matrix[i][j]
        minDist = float('inf')
        
        # 如果该数字只出现一次，则返回 -1
        if len(posMap[num]) == 1:
            result[i][j] = -1
        else:
            # 遍历相同数字的所有位置，计算曼哈顿距离
            for (x, y) in posMap[num]:
                if (x, y) != (i, j):
                    dist = abs(x - i) + abs(y - j)
                    minDist = min(minDist, dist)
            
            result[i][j] = minDist
print(result)
   