import sys
input = sys.stdin.readline

work_time, n = map(int, input().split()) # 工作时间和工作数量
tasks = [] # 存储每项工作的耗时时间和报酬
for i in range(n):
    tasks.append(list(map(int, input().split())))

min_time = float('inf') # 找到所有工作中耗时最短的那个min_time
for task in tasks:
    min_time = min(min_time, task[0])

dp = [[0] * (work_time + 1) for _ in range(n + 1)] # 初始化dp数组
for i in range(1, n + 1):
    for j in range(min_time, work_time + 1):
        last = dp[i - 1][j] # 上一项工作在j时间内能获得的最大报酬
        current = 0 if tasks[i - 1][0] > j else tasks[i - 1][1] + dp[i - 1][j - tasks[i - 1][0]] # 当前工作在j时间内能获得的最大报酬
        dp[i][j] = max(last, current) # 取上一项工作和当前工作在j时间内能获得的最大报酬的最大值

print(dp[n][work_time]) # 输出前n项工作在T时间内能获得的最大报酬