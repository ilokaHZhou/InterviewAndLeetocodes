def min_window(s, t):
    from collections import defaultdict

    # 统计 t 中每个字符的出现次数
    target_counts = defaultdict(int)
    for char in t:
        target_counts[char] += 1

    # 滑动窗口的左右指针
    left, right = 0, 0
    # 当前窗口中满足条件的字符数量
    required = len(target_counts)
    formed = 0
    # 记录当前窗口的字符出现次数
    window_counts = defaultdict(int)
    # 记录最小窗口的长度和起始位置
    min_len = float('inf')
    min_left = 0

    while right < len(s):
        # 扩展右边界
        char = s[right]
        window_counts[char] += 1

        # 如果当前字符在 t 中，并且窗口中的数量达到 t 中的数量
        if char in target_counts and window_counts[char] == target_counts[char]:
            formed += 1

        # 当窗口满足条件时，尝试收缩左边界
        while left <= right and formed == required:
            # 更新最小窗口
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left = left

            # 收缩左边界
            left_char = s[left]
            window_counts[left_char] -= 1
            if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                formed -= 1
            left += 1

        # 扩展右边界
        right += 1

    return "" if min_len == float('inf') else s[min_left:min_left + min_len]

# 输入处理
S = input().strip()
T = input().strip()
print(min_window(S, T))