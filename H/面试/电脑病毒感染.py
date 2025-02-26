import sys

# 计算感染所有电脑所需的最少时间的函数
def network_delay_time(times, N, K):
    INF = float('inf')  # 定义无穷大的值，用于初始化距离数组
    dist = [INF] * N  # 存储从源电脑到其他所有电脑的最短感染时间
    dist[K] = 0  # 源电脑的感染时间为0

    # 使用Bellman-Ford算法更新所有电脑的最短感染时间
    for _ in range(N):
        for u, v, w in times:
            # 如果可以通过电脑u感染到电脑v，并且时间更短，则更新电脑v的感染时间
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # 找出所有电脑中最长的感染时间
    max_wait = max(dist)
    # 如果有电脑的感染时间仍为无穷大，表示该电脑不可被感染，返回-1
    return max_wait if max_wait < INF else -1

 
N = int(input())
connections = int(input()) # 电脑的数量和网络连接的数量
times = []  # 存储每个连接和对应的感染时间
for _ in range(connections):
    # 读取每个连接的信息，将电脑编号减1转换为从0开始的索引
    u, v, w = map(int, input().split())
    times.append((u - 1, v - 1, w))  # 感染源电脑编号，被感染电脑编号，感染所需时间
initial = int(input()) - 1  # 初始被感染的电脑编号，转换为从0开始的索引

# 输出感染所有电脑所需的最少时间
print(network_delay_time(times, N, initial))