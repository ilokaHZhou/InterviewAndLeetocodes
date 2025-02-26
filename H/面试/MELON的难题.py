# 输入雨花石个数
n = int(input())

# 输入雨花石重量，将输入的字符串转换为整数列表
stones = list(map(int, input().split()))

# 计算所有雨花石的总重量
totalWeight = 0
for stone in stones:
    totalWeight += stone

# 如果总重量为奇数，则无法平均分配，输出 -1
if totalWeight % 2 != 0:
    print(-1)
else:
    # 计算目标重量，即总重量的一半
    targetWeight = totalWeight // 2

    # 初始化动态规划数组 dp，长度为目标重量加 1
    dp = [0] * (targetWeight + 1)

    # 将 dp 数组的值从索引 1 开始设置为 n
    for i in range(1, targetWeight + 1):
        dp[i] = n

    # 遍历所有雨花石
    for i in range(1, n + 1):
        weight = stones[i - 1]
        # 更新 dp 数组的值
        for j in range(targetWeight, weight - 1, -1):
            # 如果当前重量可以由前面的雨花石组成，更新dp[j]为最小需要拿出的雨花石数量
            dp[j] = min(dp[j], dp[j - weight] + 1)

    # 如果 dp[targetWeight] 等于 n，说明无法平均分配，输出 -1
    if dp[targetWeight] == n:
        print(-1)
    else:
        # 输出最少需要拿出的雨花石数量，使两堆的重量相等
        print(dp[targetWeight])