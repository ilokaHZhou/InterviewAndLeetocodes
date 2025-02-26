import heapq  # 导入heapq模块用于实现优先队列

# 定义一个Task类来存储每个任务的开始时间和结束时间
class Task:
    def __init__(self, startTime, endTime):
        self.startTime = startTime  # 任务开始时间
        self.endTime = endTime      # 任务结束时间

    def __lt__(self, other):
        # 定义小于操作，用于优先队列中比较Task对象，根据结束时间进行排序
        return self.endTime < other.endTime

# 创建一个列表，用于存储所有的任务，每个时间点对应一个任务列表
a = [[] for _ in range(100001)]

# 读取任务的总数
n = int(input())

# 读取每个任务的开始时间和结束时间，并将其添加到对应的任务列表中
for _ in range(n):
    x, y = map(int, input().split())  # 读取任务开始时间和结束时间
    a[x].append(Task(x, y))  # 创建任务并添加到任务列表中

ans = 0  # 用于记录能完成的任务数量
# 创建一个优先队列，根据任务的结束时间进行排序，确保每次都处理结束时间最早的任务
pq = []

# 遍历每个时间点
for i in range(100001):
    # 如果优先队列不为空且队列顶部的任务结束时间小于当前时间，则将其移除
    while pq and pq[0].endTime < i:
        heapq.heappop(pq)

    # 如果当前时间点有任务
    for task in a[i]:
        # 将当前时间点的所有任务加入优先队列
        heapq.heappush(pq, task)

    # 如果优先队列不为空，则从队列中移除一个任务，并将完成任务的数量加一
    if pq:
        ans += 1
        heapq.heappop(pq)

# 输出能完成的任务数量
print(ans)