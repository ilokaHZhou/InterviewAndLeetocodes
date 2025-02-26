def max_reliability(S, N, components):
    # 初始化每种类型的元器件
    types = [[] for _ in range(N)]
    
    # 将每个元器件根据其类型进行分类
    for t, r, p in components:
        types[t].append((r, p))
    
    # 初始化 dp 数组，dp[i][j] 表示选择前i种类型的元器件，预算为j时的最大可靠性
    dp = [[-1] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = float('inf')  # dp[0][0] 初始化为无穷大，表示没有选择任何元器件时可靠性无穷大

    # 对每种类型的元器件进行处理
    for i in range(1, N + 1):
        # 遍历每种类型的所有元器件
        for r, p in types[i - 1]:
            # 从后向前更新dp数组，确保每个元器件只使用一次
            for budget in range(S, p - 1, -1):
                if dp[i - 1][budget - p] != -1:
                    dp[i][budget] = max(dp[i][budget], min(dp[i - 1][budget - p], r))

    # 找到预算范围内的最大可靠性
    result = max(dp[N])
    
    # 如果结果仍然是-1，表示无法满足条件，返回-1
    return result if result != -1 else -1

# 从输入获取预算和元器件信息
S, N = map(int, input().split())
total = int(input())

components = []

for _ in range(total):
    t, r, p = map(int, input().split())
    components.append((t, r, p))

# 计算并输出最大可靠性
print(max_reliability(S, N, components))