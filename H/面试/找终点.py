numbers = list(map(int, input().split())) # 将输入的字符串分割并映射为整数列表
length = len(numbers) # 获取数组的长度
result = [] # 用于存储所有可能的步数结果
for i in range(1, length // 2): # 遍历所有从第一个元素开始的有效步长
    step = 1 # 初始化步数为1，因为第一步已经走出
    index = i # 将索引设为当前步长
    while index < length - 1: # 只要没有走到数组的最后一个元素
        index += numbers[index] # 按照当前索引位置的数字值前进
        step += 1 # 每走一步，步数加1
    if index == length - 1: # 如果恰好到达数组的最后一个元素
        result.append(step) # 将步数结果存入结果列表
if len(result) > 0:
    result.sort() # 对步数结果进行排序
    print(result[0]) # 输出最小的步数
else:
    print(-1) # 如果没有结果，输出-1