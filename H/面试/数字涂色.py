import sys

N = int(input())  # 读取整数N，表示黑板上数字的数量
numList = list(map(int, input().split()))  # 读取N个数字并存储在列表numList中
numList.sort()  # 对numList进行从小到大排序

colors = []  # 创建一个列表colors来存储颜色组的最小数
colorCount = 0  # 记录使用的颜色种数
for i in range(N):
    foundColor = False  # 标志位，用于检查当前数字是否找到合适的颜色组
    for j in range(colorCount):
        if numList[i] % colors[j] == 0:  # 检查当前数字能否被已有颜色组的最小数整除
            foundColor = True  # 如果找到合适的颜色组，标志位置为True
            break  # 跳出循环
    if not foundColor:  # 如果没有找到合适的颜色组
        colors.append(numList[i])  # 将当前数字作为一个新的颜色组的最小数添加到colors列表中
        colorCount += 1  # 增加颜色组数量

print(colorCount)  # 输出最少需要的颜色种数