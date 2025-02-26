import sys


# 读取窗口数量N
numberOfRows = int(input())
# 读取每个窗口需要的元素数量K
numberOfColumns = int(input())

# 创建队列列表，用于存储每个列表的元素
queueList = []
while True:
    try:
        queueList.append(list(map(int, input().split())))
    except:
        break
 

# 创建一个列表，用于存储最终的元素排列
matrix = [0] * (numberOfColumns * numberOfRows)
matrixIndex = 0  # 用于标记当前填充到matrix列表中的位置
queueIndex = 0  # 用于标记当前处理的队列索引

# 循环，直到matrix列表被完全填满
while matrixIndex < len(matrix):
    didRemoveQueue = False  # 标记本轮循环中是否有队列被移除

    # 遍历每个窗口，并尝试从当前队列中为每个窗口提取一个元素
    for i in range(numberOfRows):
        if not queueList:  # 如果所有队列都已处理完毕，则退出循环
            break
        # 如果当前队列为空，则移除该队列
        if not queueList[queueIndex]:
            queueList.pop(queueIndex)
            if not queueList:
                break
            queueIndex %= len(queueList)
            didRemoveQueue = True
        # 如果当前队列不为空，则从队列中取出一个元素填充到matrix列表中
        if queueList and queueList[queueIndex]:
            matrix[matrixIndex] = queueList[queueIndex].pop(0)
            matrixIndex += 1
            if matrixIndex >= len(matrix):
                break

    # 如果本轮循环没有队列被移除，并且队列列表不为空，则处理下一个队列
    if not didRemoveQueue and queueList:
        queueIndex = (queueIndex + 1) % len(queueList)

# 按照窗口顺序构建输出字符串
for row in range(numberOfRows):
    for col in range(numberOfColumns):
        print(matrix[col * numberOfRows + row], end=" ")