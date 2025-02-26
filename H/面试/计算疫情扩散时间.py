import math
from queue import Queue

def getInfectionDays(map):
    # 计算地图边长，即每一行（或列）的元素个数
    n = int(math.sqrt(len(map)))
    
    # 构建二维矩阵表示地图，初始值为0
    matrix = [[0 for j in range(n)] for i in range(n)]
    
    # 初始化一个队列，用于存放已感染区域的位置
    q = Queue()
    
    # 遍历地图，将已感染区域的坐标入队，并初始化二维矩阵
    for i in range(n):
        for j in range(n):
            matrix[i][j] = map[i * n + j]
            if matrix[i][j] == 1:
                q.put((i, j))
    
    # 如果队列为空（没有感染区域）或所有区域都已被感染，返回-1
    if q.empty() or q.qsize() == len(map):
        return -1
    
    # 计算未感染区域的数量
    healthy = len(map) - q.qsize()
    
    # 定义四个方向的偏移量（上下左右）
    offsets = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    # 初始化天数计数器
    day = 0
    
    # 广度优先搜索，通过队列逐层扩散感染
    while not q.empty() and healthy > 0:
        tmp = q.get()
        x, y = tmp[0], tmp[1]
        day = matrix[x][y] + 1  # 更新天数
        
        # 对当前节点的四个方向进行探索
        for offset in offsets:
            new_x = x + offset[0]
            new_y = y + offset[1]
            
            # 检查新坐标是否越界
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n:
                continue
            
            # 如果新坐标的区域未被感染，则将其感染，并将其加入队列
            if matrix[new_x][new_y] == 0:
                healthy -= 1
                matrix[new_x][new_y] = day
                q.put((new_x, new_y))
    
    # 返回全部区域被感染所需的天数，由于最后一天的增加已在循环中完成，故减1
    return day - 1

# 读取输入，并转换成整数列表
input_str = input()
input_list = list(map(int, input_str.split(",")))

# 输出计算结果
print(getInfectionDays(input_list))