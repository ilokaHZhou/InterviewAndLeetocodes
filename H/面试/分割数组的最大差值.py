import sys

# 输入数组长度
length = int(sys.stdin.readline())

# 输入数字序列
numbers = list(map(int, sys.stdin.readline().split()))

# 计算前缀和
prefixSum = [0] * length
prefixSum[0] = numbers[0]
for i in range(1, length):
  prefixSum[i] = prefixSum[i-1] + numbers[i]

# 差值的最大取值
maxDifference = 0

# 计算差值的最大取值
for i in range(length - 1):
  leftSum = prefixSum[i]
  rightSum = prefixSum[length-1] - prefixSum[i]
  difference = abs(leftSum - rightSum)
  maxDifference = max(maxDifference, difference)

# 输出差值的最大取值
print(maxDifference)