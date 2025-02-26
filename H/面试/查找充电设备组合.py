n = int(input()) # 充电设备个数
power = list(map(int, input().split())) # 每个充电设备的输出功率
p_max = int(input()) # 充电站最大输出功率

dp = [[0] * (p_max + 1) for _ in range(n + 1)] # 初始化为0

for i in range(1, n + 1):
    for j in range(1, p_max + 1):
        if power[i - 1] > j: # 当前充电设备的功率大于当前总功率j，不能选
            dp[i][j] = dp[i - 1][j] # 不选当前充电设备
        else:
            dp[i][j] = max(dp[i - 1][j], power[i - 1] + dp[i - 1][j - power[i - 1]]) # 选或不选当前充电设备

print(dp[n][p_max]) # 输出最大功率