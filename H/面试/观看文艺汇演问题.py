import sys

# 输入演出场数
n = int(input())

# 创建一个列表来存储演出时间表
schedule = []

# 循环读取每个演出的开始时间和持续时间，并将其添加到演出时间表中
for i in range(n):
    time = input()
    startTime = int(time.split()[0])
    endTime = startTime + int(time.split()[1])
    schedule.append([startTime, endTime])

# 将演出时间表按照结束时间进行排序
schedule.sort(key=lambda x: x[1])

# 获取第一个演出的结束时间和初始化观看的演出场数
firstEndTime = schedule[0][1]
numShows = 1

# 遍历演出时间表中的每个演出时间段
for interval in schedule:
    startTime = interval[0]
    endTime = interval[1]

    # 如果当前演出的开始时间与前一个演出的结束时间间隔大于等于15分钟，则可以观看该演出
    if startTime - firstEndTime >= 15:
        numShows += 1
        firstEndTime = endTime

# 输出最多能观看的演出场数
print(numShows)