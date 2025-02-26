import sys

# 计算两个一维数组的点积
def dotProduct(a, b):
    result = 0.0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result

# 根据不等式约束判断一个数是否大于、大于等于、小于、小于等于、等于 0
def satisfiesConstraint(val, constraint):
    if constraint == '>':
        return val > 0
    elif constraint == '>=':
        return val >= 0
    elif constraint == '<':
        return val < 0
    elif constraint == '<=':
        return val <= 0
    elif constraint == '=':
        return val == 0
    else:
        return False

# 读入不等式
for line in sys.stdin:
    arr = [s.split(',') for s in line.strip().split(';')]

    # 将不等式系数转换为 Double 类型的二维数组
    matrix = [[float(num) for num in row] for row in arr[:3]]

    # 将不等式的变量转换为 Double 类型的一维数组
    x = [float(num) for num in arr[3]]

    # 将不等式的目标值转换为 Double 类型的一维数组
    b = [float(num) for num in arr[4]]

    # 将不等式约束转换为字符串数组
    y = arr[5]

    # 计算每个不等式的差值
    diffs = [dotProduct(matrix[i], x) - b[i] for i in range(3)]

    # 判断所有不等式是否都成立
    flag = satisfiesConstraint(diffs[0], y[0]) and satisfiesConstraint(diffs[1], y[1]) and satisfiesConstraint(diffs[2], y[2])

    # 计算不等式的最大差值，并输出其整数部分
    maxDiff = int(max([abs(num) for num in diffs]))
    print(str(flag) + ' ' + str(maxDiff))