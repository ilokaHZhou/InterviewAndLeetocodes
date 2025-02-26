import sys

# 输入适合种树的坐标数量
n = int(input())

# 输入适合种树的坐标位置
positions = list(map(int, input().split()))

# 输入树苗的数量
m = int(input())

# 将坐标位置排序
positions.sort()

# 初始化最小种植间距的最小值和最大值
minDistanceMin = 1
minDistanceMax = positions[n - 1] - positions[0]

ans = 0

# 二分查找最佳的最小种植间距
for minDistance in range(minDistanceMin, minDistanceMax + 1):
    count = 1
    curPos = positions[0]

    # 计算当前种植间距下可以种植的树苗数量
    for i in range(1, n):
        if positions[i] - curPos >= minDistance:
            count += 1
            curPos = positions[i]

    # 如果当前种植间距下可以种植的树苗数量大于等于目标树苗数量，更新答案并继续搜索更大的种植间距
    if count >= m:
        ans = minDistance
        minDistanceMin = minDistance + 1
    else:
        minDistanceMax = minDistance - 1

# 输出最佳的最小种植间距
print(ans)