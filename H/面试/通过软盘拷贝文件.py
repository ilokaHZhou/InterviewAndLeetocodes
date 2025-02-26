import math

n = int(input())

fileSizeArray = []
for i in range(n):
    fileSizeArray.append(int(input()))

blockCount = 1474560 // 512

dp = [0] * (blockCount + 1)

for fileSize in fileSizeArray:
    weight = math.ceil(fileSize / 512)
    worth = fileSize
    for j in range(blockCount, weight - 1, -1):
        dp[j] = max(dp[j], dp[j - weight] + worth)

print(dp[blockCount])
