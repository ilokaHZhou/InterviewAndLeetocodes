import sys

def dfs(i, current_val):
    """
    深度优先搜索寻找增广路径
    :param i: 当前正在处理的行索引
    :param current_val: 当前考虑的值
    :return: 如果找到增广路径，返回True；否则返回False
    """
    for j in range(m):
        # 检查第j列是否未被访问过且第i行第j列的值小于等于current_val
        if not vis[j] and matrix[i][j] <= current_val:
            vis[j] = True  # 标记第j列为已访问
            # 如果第j列未匹配或其匹配的行可以找到其他匹配列
            if match[j] == -1 or dfs(match[j], current_val):
                match[j] = i  # 将第j列与第i行匹配
                return True
    return False

def check(current_val):
    """
    检查当前值是否满足条件
    :param current_val: 当前考虑的值
    :return: 如果满足条件，返回True；否则返回False
    """
    global match, vis
    match = [-1] * m  # 初始化匹配数组，所有列都标记为未匹配
    vis = [False] * m  # 初始化访问标记数组
    smaller_count = 0  # 统计满足条件的数量

    for i in range(n):
        vis = [False] * m  # 每次搜索前重置访问标记
        if dfs(i, current_val):
            smaller_count += 1  # 如果找到增广路径，则计数增加

    return smaller_count >= n - k + 1  # 检查是否有足够的小于等于current_val的数

# 读取输入
n, m, k = map(int, input().split())  # 读取行数、列数和k值

# 初始化矩阵
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# 初始化二分查找的上下界
min_val, max_val = 1, -sys.maxsize

# 更新矩阵元素的最大值，作为二分查找的上界
for row in matrix:
    max_val = max(max_val, max(row))

# 二分查找确定第K大的数的最小可能值
while min_val <= max_val:
    mid = (min_val + max_val) // 2
    if check(mid):
        max_val = mid - 1
    else:
        min_val = mid + 1

# 输出最终结果
print(min_val)