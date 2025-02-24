def count_negative_and_average_positive(nums):
    negative_count = 0  # 负数个数
    positive_sum = 0  # 正数之和
    positive_count = 0  # 正数个数

    for num in nums:  # 遍历数字列表
        if num < 0:  # 如果是负数
            negative_count += 1  # 负数计数加 1
        elif num > 0:  # 如果是正数
            positive_sum += num  # 正数累加
            positive_count += 1  # 正数计数加 1

    # 计算正数平均值
    average = (positive_sum / positive_count) if positive_count > 0 else 0.0

    return negative_count, average  # 返回负数个数和正数平均值


# 输入处理
n = int(input())  # 数字个数
nums = list(map(int, input().split()))  # 数字列表

# 调用函数并输出结果
negative_count, average = count_negative_and_average_positive(nums)
print(negative_count, average)
