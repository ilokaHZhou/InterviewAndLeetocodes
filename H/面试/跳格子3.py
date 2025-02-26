from collections import deque

n = int(input().strip())
scores = list(map(int, input().strip().split()))
k = int(input().strip())

# 特殊情况处理：如果格子数量为1，直接输出该格子的分数
if n == 1:
    print(scores[0])
    exit()

# 动态规划数组，dp[i]存储到达第i个格子时能得到的最大分数
dp = [0] * n
dp[0] = scores[0]  # 初始化，起点的最大分数就是起点的分数

# 使用双端队列来维护窗口内的最大dp值的索引
deque = deque([0])

for i in range(1, n):
    # 如果队列不为空且队列头部的索引已经超出了跳跃范围，从队列中移除头部
    if deque and deque[0] < i - k:
        deque.popleft()

    # 计算当前格子的最大分数：当前格子的分数加上可以跳到该格子的最大分数
    dp[i] = scores[i] + (dp[deque[0]] if deque else 0)

    # 维护队列，保持队列为递减，新的最大值需要添加到队尾
    while deque and dp[deque[-1]] <= dp[i]:
        deque.pop()

    # 将当前索引加到队列尾部
    deque.append(i)

# 输出到达最后一个格子时能得到的最大分数
print(dp[-1])