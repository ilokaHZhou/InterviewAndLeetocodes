import sys

# 定义数字到字母的映射关系，map[0] 对应 'abc', map[1] 对应 'def'，依此类推
map = ["abc", "def", "ghi", "jkl", "mno", "pqr", "st", "uv", "wx", "yz"]

# 深度优先搜索 (DFS) 递归函数
def dfs(letters, index, path, res, filter, used):
    # 如果当前索引等于字母组的长度，说明已经生成了一个完整的字母组合
    if index == len(letters):
        # 如果生成的组合不包含屏蔽字符串，则将其加入结果集
        if filter not in path:
            res.append(path + ",")
        return
    
    # 遍历当前索引位置对应的所有字母
    for i in range(len(letters[index])):
        c = letters[index][i]  # 当前字母
        # 如果当前字母尚未被使用
        if c not in used:
            path += c  # 将字母加入当前路径
            used.add(c)  # 标记字母为已使用
            # 递归调用下一层，处理下一个索引
            dfs(letters, index + 1, path, res, filter, used)
            path = path[:-1]  # 回溯，移除最后添加的字母
            used.remove(c)  # 取消字母的使用标记


digits = input().strip()  # 读取输入的数字字符串，并去除首尾空格
filter = input().strip()  # 读取输入的屏蔽字符串，并去除首尾空格

# 将输入的数字字符串转换为对应的字母组，如"78" -> ['uv', 'wx']
letters = [map[int(digit)] for digit in digits]

sb = ""  # 初始化一个空字符串，用于存储当前路径
res = []  # 结果列表，存储所有符合条件的字母组合
dfs(letters, 0, sb, res, filter, set())  # 调用DFS函数，开始递归搜索

# 输出结果，将结果列表中的元素连接成一个字符串并打印
print("".join(res))