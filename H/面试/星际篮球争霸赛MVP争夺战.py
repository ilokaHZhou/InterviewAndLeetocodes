# 输入处理：读取元素个数和元素值，计算总和
n = int(input())  # 读取元素个数
nums = list(map(int, input().split()))  # 读取所有元素并转换为整数列表
sum_nums = sum(nums)  # 计算所有元素的总和

# 主体逻辑：尝试将 nums 分成 k 个子集，每个子集的和相等
for k in range(n, 0, -1):
    # 如果总和不能被 k 整除，则无法分为 k 个和相等的子集，跳过
    if sum_nums % k != 0:
        continue

    per_sum = sum_nums // k  # 每个子集的目标和

    # 对数组排序，确保较大元素在前，有助于提前剪枝
    nums.sort()

    # 如果最大的元素已经大于每个子集的目标和，则无法分割，跳过
    if nums[-1] > per_sum:
        continue

    # 使用动态规划判断是否可以分成 k 个子集
    subset_count = len(nums)
    dp = [False] * (1 << subset_count)  # dp[i] 表示是否能构成下标 i 的子集
    cur_sum = [0] * (1 << subset_count)  # cur_sum[i] 记录下标 i 对应的当前子集和
    dp[0] = True  # 初始化空集状态

    for i in range(1 << subset_count):
        if not dp[i]:
            continue  # 如果当前子集状态不可行，跳过
        for j in range(subset_count):
            if (i >> j) & 1:
                continue  # 如果 nums[j] 已经在当前子集中使用，跳过

            # 如果将 nums[j] 加入子集后超出目标和，跳过
            if cur_sum[i] + nums[j] > per_sum:
                break

            next_subset = i | (1 << j)  # 将 nums[j] 加入新的子集中
            if not dp[next_subset]:
                cur_sum[next_subset] = (cur_sum[i] + nums[j]) % per_sum  # 更新新子集的和
                dp[next_subset] = True  # 标记新子集状态为可行

    # 如果最终所有元素都能被划分为合法的子集，则输出每个子集的和
    if dp[(1 << subset_count) - 1]:
        print(per_sum)  # 输出每个子集的和
        break