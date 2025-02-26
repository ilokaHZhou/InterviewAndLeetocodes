# 容忍的平均失败率
toleratedAverageLoss = int(input())

# 读取失败率数组
failureRates = list(map(int, input().split()))

arrayLength = len(failureRates)

# 创建一个累积和数组，用于快速计算任意时间段的失败率总和
cumulativeSum = [0] * arrayLength
cumulativeSum[0] = failureRates[0] 
for i in range(1, arrayLength):
    cumulativeSum[i] = cumulativeSum[i - 1] + failureRates[i]

# 存储满足条件的时间段的开始和结束索引
validPeriods = []
maxLength = 0
for start in range(arrayLength):
    for end in range(start, arrayLength):
        sum = cumulativeSum[end] if start == 0 else cumulativeSum[end] - cumulativeSum[start - 1]
        length = end - start + 1
        toleratedLoss = length * toleratedAverageLoss

        # 如果这个时间段的平均失败率小于等于容忍的平均失败率
        if sum <= toleratedLoss:
            # 如果这个时间段比之前找到的时间段更长，清空结果列表并添加这个时间段
            if length > maxLength:
                validPeriods = []
                validPeriods.append((start, end))
                maxLength = length
            # 如果这个时间段和之前找到的最长时间段一样长，添加这个时间段
            elif length == maxLength:
                validPeriods.append((start, end))

# 如果没有找到满足条件的时间段，输出"NULL"
if len(validPeriods) == 0:
    print("NULL")
# 否则，输出所有满足条件的时间段
else:
    validPeriods.sort()

    print(' '.join(f'{start}-{end}' for start, end in validPeriods))
