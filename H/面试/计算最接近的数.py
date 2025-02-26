input_str = input().replace("[", "").replace("]", "").split(",")

# 计算输入数组的长度，n是数组的元素数量，最后一个元素为K
n = len(input_str) - 1

# 将前n个元素转换为整数，构建整数数组nums
nums = [int(input_str[i]) for i in range(n)]

# 将最后一个元素转换为整数，作为K的值
k = int(input_str[n])

# 创建nums的副本，并对副本进行排序以计算中位数
sorted_nums = nums.copy()
sorted_nums.sort()

# 计算中位数：排序后下标为n//2的元素
median = sorted_nums[n // 2]

# 初始化最小差值为正无穷大，结果下标初始化为-1
minDiff = float('inf')
result = -1

# 遍历所有可能的起始下标i，范围为0到n-k
for i in range(n - k + 1):
    count = nums[i]  # 初始化count为当前下标的元素
    # 计算从i到i+k-1的元素的差值
    for j in range(i + 1, i + k):
        count -= nums[j]  # 依次减去下标j对应的元素

    # 计算当前count与中位数之间的绝对差值
    diff = abs(count - median)

    # 如果当前差值小于已知最小差值，则更新最小差值和结果下标
    if diff < minDiff:
        minDiff = diff
        result = i
    # 如果当前差值等于已知最小差值，则更新结果下标为较大的那个
    elif diff == minDiff:
        result = max(result, i)

# 输出最终结果下标
print(result)