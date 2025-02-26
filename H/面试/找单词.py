n = int(input())  # 读取二维数组的大小
matrix = []  # 初始化二维数组
for _ in range(n):  # 读取二维数组的每一行
    line = input()
    matrix.append(line.split(","))  # 使用逗号分割每一行，得到每个单元格的字符
tar = input()  # 读取待查找的字符串

visited = [[False] * n for _ in range(n)]  # 初始化访问记录数组

def findString():
    path = []  # 存储路径的列表
    for i in range(n):  # 遍历二维数组的每个单元格
        for j in range(n):
            if matrix[i][j] == tar[0]:  # 如果当前单元格的字符与待查找字符串的第一个字符相同
                found = dfs(i, j, 0, path)  # 使用深度优先搜索查找字符串
                if found:  # 如果找到了字符串
                    result = ""  # 初始化结果字符串
                    for pos in path:  # 将路径中的每个单元格的位置添加到结果字符串中
                        result += str(pos[0]) + "," + str(pos[1]) + ","
                    result = result[:-1]  # 删除最后一个逗号
                    return result  # 返回结果字符串
    return "N"  # 如果没有找到字符串，返回"N"

def dfs(i, j, k, path):
    # 如果当前位置越界，或已被访问，或当前位置的字符与待查找字符串的当前字符不相同
    if i < 0 or i >= n or j < 0 or j >= n or visited[i][j] or tar[k] != matrix[i][j]:
        return False  # 返回false
    path.append([i, j])  # 将当前位置添加到路径中
    visited[i][j] = True  # 标记当前位置已被访问
    if k == len(tar) - 1:  # 如果已经找到了所有的字符
        return True  # 返回true
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 定义四个方向
    for direction in directions:  # 对四个方向进行深度优先搜索
        ni = i + direction[0]
        nj = j + direction[1]
        res = dfs(ni, nj, k + 1, path)
        if res:  # 如果在某个方向上找到了字符串
            return True  # 返回true
    visited[i][j] = False  # 撤销对当前位置的访问标记
    path.pop()  # 从路径中移除当前位置
    return False  # 返回false

result = findString()  # 查找字符串
print(result)  # 输出结果