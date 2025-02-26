def check(current_version_set, n, matrix):
    for i in range(len(matrix)):
        if i in current_version_set:    # 若该节点已被访问过，则跳过
            continue
        if n != i and matrix[n][i] == 1:   # 如果当前版本与 n 版本相连，则将其加入到版本集合中
            current_version_set.add(i)
            check(current_version_set, i, matrix)   # 继续递归查找以 i 节点为起点的关联版本

# 处理输入
n = int(input())   # 版本数量

matrix = []
for i in range(n):
    row = list(map(int, input().split()))   # 将每行版本信息存储在 matrix 中
    matrix.append(row)

#记录已经遍历过的版本号
visited_versions = set()    
res = 0   # 最大关联版本数量
for i in range(n):
    if i not in visited_versions:   # 若当前版本已经遍历过，则跳过
        current_version_set = set()   # 当前版本集合
        check(current_version_set, i, matrix)   # 深度优先搜索找到以 i 版本为起点的关联版本
        res = max(res, len(current_version_set))   # 更新最大关联版本数量
        visited_versions.update(current_version_set)   # 将当前版本集合中的所有版本加入 visitedVersions

print(res)   # 输出最大关联版本数量