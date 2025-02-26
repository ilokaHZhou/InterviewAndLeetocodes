# 读取一行输入，分割字符串并转换为整数列表，表示每项任务所需的时间
times = list(map(int, input().split(',')))

# 读取并转换为整数，表示最大允许的天数
max_days = int(input())


# 初始化总时间和最大单个时间
total_time = sum(times)
max_time = max(times)

# 初始化二分搜索的范围
low = 0
high = total_time - max_time

# 使用二分搜索确定最小的可行时间限制
while low <= high:
    mid = (low + high) >> 1  # 计算中点
    current_sum = 0  # 当前段的时间总和
    can_adjust = True  # 标记是否可以调整当前任务到前一天
    current_day = 1  # 当前天数计数
    i = 0  # 时间数组的索引

    # 遍历时间数组，试图按照每天不超过 mid 的限制来分配任务
    while i < len(times):
        current_sum += times[i]

        if current_sum > mid:
            if can_adjust:
                # 如果当前和超过了 mid，尝试不计入当前任务，继续下一任务
                current_sum -= times[i]
                can_adjust = False  # 标记当天已经进行过调整
                i += 1
            else:
                # 如果不能再调整，增加天数，重置当前和和调整标记
                current_day += 1
                if current_day > max_days:
                    # 如果天数超过最大允许值，中断内部循环
                    break
                current_sum = 0
                can_adjust = True
        else:
            # 如果当前和未超过 mid，继续累加下一个任务
            i += 1

    # 判断是否所有任务都能在 max_days 天内完成
    if i == len(times) and current_day <= max_days:
        # 如果可以，尝试更小的 mid
        high = mid - 1
    else:
        # 如果不可以，尝试更大的 mid
        low = mid + 1

# 输出找到的最小的满足条件的最大每日工作时间
print(low)
