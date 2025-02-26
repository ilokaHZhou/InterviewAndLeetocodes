def solve_24_game(nums):
    def dfs(nums):  # 深度优先搜索
        if len(nums) == 1:  # 如果只剩一个数
            return abs(nums[0] - 24) < 1e-6  # 判断是否等于 24
        for i in range(len(nums)):  # 遍历所有数
            for j in range(len(nums)):  # 遍历所有数
                if i == j:  # 不能选择同一个数
                    continue
                new_nums = [
                    nums[k] for k in range(len(nums)) if k != i and k != j
                ]  # 去掉已选的两个数
                # 尝试四种运算
                for op in ["+", "-", "*", "/"]:
                    if op == "+" or op == "*":  # 加法和乘法满足交换律，避免重复计算
                        if i > j:
                            continue
                    if op == "/" and nums[j] == 0:  # 除法时除数不能为 0
                        continue
                    if op == "+":
                        new_nums.append(nums[i] + nums[j])
                    elif op == "-":
                        new_nums.append(nums[i] - nums[j])
                    elif op == "*":
                        new_nums.append(nums[i] * nums[j])
                    elif op == "/":
                        new_nums.append(nums[i] / nums[j])
                    if dfs(new_nums):  # 递归检查
                        return True
                    new_nums.pop()  # 回溯
        return False

    return dfs(nums)  # 调用深度优先搜索


# 输入处理
nums = list(map(int, input().split()))
print("true" if solve_24_game(nums) else "false")
