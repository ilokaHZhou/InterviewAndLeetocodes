import re

def convertToMillisecond(timeStr):
    hour, minute, second, millisecond = map(int, re.findall(r'\d+', timeStr))
    return hour * 60 * 60 * 1000 + minute * 60 * 1000 + second * 1000 + millisecond
logs = []
n = int(input())

for i in range(n):
    log = input()
    logs.append(log)

# 日志排序
logs.sort(key=lambda log: convertToMillisecond(log))

for log in logs:
    print(log)
