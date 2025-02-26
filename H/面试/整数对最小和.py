# 从输入中获取数组array1，使用map函数将输入的字符串转换为整数，并使用列表切片[1:]去除第一个元素
array1 = list(map(int, input().split()))[1:]

# 从输入中获取数组array2，使用map函数将输入的字符串转换为整数，并使用列表切片[1:]去除第一个元素
array2 = list(map(int, input().split()))[1:]

# 从输入中获取k的值，将其转换为整数
k = int(input())

# 存储所有可能的元素对的和
pairsSum = []
for value1 in array1:
    for value2 in array2:
        pairsSum.append(value1 + value2)

# 对和进行排序
pairsSum.sort()

# 取前k个元素进行求和
minSum = sum(pairsSum[:k])

# 输出最小和
print(minSum)