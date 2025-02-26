# 导入所需模块
from itertools import permutations

def main():
    # 读取输入的一行字符串，并将其转换为整数列表
    nums = list(map(int, input().split(',')))

    # 使用集合来记录输入的数字，避免重复，并进行后续检查
    num_set = set()
    # 记录输入数字中的最大值，用于后续输出
    n = float('-inf')

    # 遍历输入的每一个数字，进行合法性检查并找出最大值
    for num in nums:
        # 检查数字是否在1到9的范围内，且是否重复
        if num < 1 or num > 9 or num in num_set:
            print(-1)
            return
        num_set.add(num)
        n = max(n, num)
    
    # 检查是否输入了4个数字，并且不允许2和5同时出现，或6和9同时出现
    if len(num_set) != 4 or (2 in num_set and 5 in num_set) or (6 in num_set and 9 in num_set):
        print(-1)
        return

    # 定义替换规则
    replace_map = {2: 5, 5: 2, 6: 9, 9: 6}

    # 初始化结果列表
    res_list = []

    # 调用递归函数，生成所有排列组合
    dfs(nums, set(), "", replace_map, res_list)

    # 如果没有生成任何有效的排列结果，输出-1
    if not res_list:
        print(-1)
        return

    # 对结果列表进行升序排序
    res_list.sort()

    # 确定要输出的第n个数字，n为输入的最大值
    nth = min(n, len(res_list))

    # 输出排序后的第nth个数字
    print(res_list[nth - 1])

def dfs(nums, used, path, replace_map, res):
    # 如果当前路径不为空，将路径转换为整数并加入结果集中
    if path:
        res.append(int(path))

    # 如果当前路径的长度已经等于输入的数字数量，返回（递归结束条件）
    if len(path) == len(nums):
        return

    # 遍历所有输入的数字，尝试将每个数字放入当前路径中
    for num in nums:
        if num in used:
            continue

        used.add(num)

        # 递归调用，将当前数字加入路径中
        dfs(nums, used, path + str(num), replace_map, res)

        # 如果当前数字有替代规则且替代数字未被使用，则尝试使用替代数字
        if num in replace_map and replace_map[num] not in used:
            dfs(nums, used, path + str(replace_map[num]), replace_map, res)

        # 回溯
        used.remove(num)

if __name__ == "__main__":
    main()