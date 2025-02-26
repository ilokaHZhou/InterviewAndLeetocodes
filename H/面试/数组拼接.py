# 读取固定长度和数组的数量
fixedLength = int(input())  # 每次取出的固定长度
arrayNum = int(input())  # 数组数量
totalCount = 0  # 用于记录所有数组中元素的总数
inputArrays = []  # 存储所有输入的数组

# 读取输入的数组并存储
for i in range(arrayNum):  # 读取每个数组
    inputStr = input()  # 读取输入字符串
    v = []  # 用于存储当前数组
    while ',' in inputStr:  # 查找逗号分隔符
        found = inputStr.index(",")  # 找到逗号的位置
        v.append(int(inputStr[:found]))  # 提取逗号前的部分并转换为整数
        inputStr = inputStr[found + 1:]  # 删除已经处理过的部分
        totalCount += 1  # 更新总元素个数
    v.append(int(inputStr))  # 添加最后一个元素
    totalCount += 1  # 更新总元素个数
    inputArrays.append(v)  # 将当前数组添加到数组集合中

# 合并数组
result = []  # 用于存储合并后的结果
num = 0  # 记录已合并的元素数量
while num < totalCount:  # 当合并的元素数量少于总数时继续
    for i in range(len(inputArrays)):  # 遍历所有数组
        for j in range(fixedLength):  # 每次从当前数组中取固定长度的元素
            if len(inputArrays[i]) > 0:  # 如果当前数组不为空
                num += 1  # 更新已处理的元素数量
                result.append(inputArrays[i][0])  # 将第一个元素添加到结果中
                inputArrays[i].pop(0)  # 删除该元素
            else:
                break  # 如果当前数组为空，则跳过

# 输出结果
for i in range(len(result) - 1):  # 输出结果数组，元素之间用逗号分隔
    print(result[i], end=',')
print(result[-1])  # 输出最后一个元素时不加逗号