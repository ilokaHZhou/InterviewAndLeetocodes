def min_replacement_length(input_str):
    # 初始化方向键计数字典
    direction_count = {'W': 0, 'A': 0, 'S': 0, 'D': 0}

    # 统计输入字符串中每个方向键的出现次数
    for char in input_str:
        direction_count[char] += 1

    # 初始化左右指针和结果变量
    left = 0
    right = 0
    min_length = len(input_str)

    # 更新右指针对应的方向键计数
    direction_count[input_str[0]] -= 1

    while True:
        # 计算当前最大方向键计数
        max_count = max(direction_count.values())

        # 计算当前窗口长度和可替换的字符数
        window_length = right - left + 1
        replaceable_chars = window_length - sum(max_count - count for count in direction_count.values())

        # 如果可替换字符数大于等于0且能被4整除，则更新结果变量
        if replaceable_chars >= 0 and replaceable_chars % 4 == 0:
            min_length = min(min_length, window_length)

            # 更新左指针并检查是否越界
            if left < len(input_str):
                direction_count[input_str[left]] += 1
                left += 1
            else:
                break
        else:
            # 更新右指针并检查是否越界
            right += 1
            if right >= len(input_str):
                break
            direction_count[input_str[right]] -= 1

    return min_length


if __name__ == "__main__":
    input_str = input()
    print(min_replacement_length(input_str))
