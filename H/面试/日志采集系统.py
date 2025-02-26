import sys

# 读取输入的日志序列
input = sys.stdin.readline().strip()
# 将日志序列按空格分割成数组
logs = input.split(" ")

totalCount = 0  # 总日志条数
maxScore = 0  # 最大积分数
for i in range(len(logs)):
    logCount = int(logs[i])  # 当前时间点的日志条数
    if logCount == 0:
        continue  # 如果当前时间点没有日志条数，则跳过

    totalCount += logCount  # 更新总日志条数

    score = 0  # 当前时间点的积分数
    for j in range(i+1):
        if totalCount > 100 and i == j:
            # 如果总日志条数超过100，并且当前时间点是最后一个时间点
            score += logCount - (totalCount - 100)  # 计算得分
        else:
            score += int(logs[j]) - (i - j) * int(logs[j])  # 计算得分

    if score > maxScore:
        maxScore = score  # 更新最大积分数

    if totalCount >= 100:
        break  # 如果总日志条数达到100条以上，则退出循环

print(maxScore)  # 输出最大积分数