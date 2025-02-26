n, m = list(map(int, input().split()))  # 输入n和m，n代表菜的个数，m代表手速

times = []  # 用来存储每个菜的时间
for _ in range(n):
    start, duration = list(map(int, input().split()))  # 输入每个菜的开始时间和需要的时间
    times.append(start + duration)  # 将每个菜的结束时间存入times列表中

nums = [0] * (max(times) + 1)  # 用来记录每个时间点是否有菜，初始化为0
for t in times:
    nums[t] = 1  # 将有菜的时间点置为1

dp = []  # 用来存储每种策略下能吃到的刚好合适的菜的数量

def dfs(t, data):  # 深度优先搜索函数，t表示当前时间点，data表示当前策略下已经吃到的菜的数量
    if t >= len(nums):  # 如果当前时间点超过了最大时间点，说明已经搜索完所有时间点
        dp.append(sum(data))  # 将当前策略下吃到的菜的数量加入dp列表中
        return
    if nums[t] == 1:  # 如果当前时间点有菜
        dfs(t + m, data + [1])  # 选择捞菜，并将捞到的菜的数量加入data列表中
        dfs(t + 1, data)  # 不捞菜，继续搜索下一个时间点
    else:  # 如果当前时间点没有菜
        dfs(t + 1, data)  # 直接搜索下一个时间点

dfs(1, [])  # 从第一个时间点开始搜索，初始策略下没有吃到任何菜

print(max(dp))  # 输出最多能吃到的刚好合适的菜的数量