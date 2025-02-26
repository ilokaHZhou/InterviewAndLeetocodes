memoryInfo = input() # 读取内存池资源列表
applyList = input() # 读取申请列表

# 内存信息
memoryList = [] # 创建一个列表，用于存储内存池中可用的内存大小
memoryInfoList = memoryInfo.split(",") # 将内存池资源列表按逗号分隔，转换为列表
for info in memoryInfoList: # 遍历内存池资源列表
    colonIndex = info.index(":") # 找到冒号的位置
    size = int(info[:colonIndex]) # 截取内存大小
    count = int(info[colonIndex + 1:]) # 截取内存块数量
    for i in range(count): # 将内存块数量的内存大小添加到内存列表中
        memoryList.append(size)

# 申请信息
applyMemoryList = [] # 创建一个列表，用于存储申请的内存大小
applyListList = applyList.split(",") # 将申请列表按逗号分隔，转换为列表
for apply in applyListList: # 遍历申请列表
    applyMemoryList.append(int(apply)) # 将申请的内存大小添加到申请内存列表中

# 分配内存
resultList = [] # 创建一个列表，用于存储每个申请是否成功
for applyMemory in applyMemoryList: # 遍历申请内存列表
    flag = False # 定义一个标志位，用于标记是否成功分配内存
    for i in range(len(memoryList)): # 遍历内存列表
        if memoryList[i] >= applyMemory: # 如果当前内存块的大小大于等于申请的内存大小
            flag = True # 标记成功分配内存
            memoryList.pop(i) # 将当前内存块从内存列表中移除
            break # 跳出循环
    resultList.append(flag) # 将是否成功分配内存的结果添加到结果列表中

# 输出结果
for i in range(len(resultList)): # 遍历结果列表
    print(resultList[i], end='') # 输出当前申请是否成功分配内存
    if i != len(resultList) - 1: # 如果不是最后一个结果
        print(',', end='') # 输出逗号分隔符