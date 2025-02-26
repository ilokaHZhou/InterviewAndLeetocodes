def find_redundant_cover(s1, s2, k):
    """
    查找满足条件的子串起始位置
    :param s1: 字符串 s1
    :param s2: 字符串 s2
    :param k: 冗余长度 k
    :return: 返回满足条件的子串的最左侧起始位置，如果没有返回 -1
    """
    # 计算 s1 中每个字符的出现次数
    s1_count = [0] * 26  # 创建一个长度为26的数组，用于记录每个字母的出现次数
    for c in s1:
        s1_count[ord(c) - ord('a')] += 1  # 通过字符的ASCII码计算其在数组中的位置并递增计数

    # 初始化滑动窗口的左右边界、剩余需要匹配的 s1 字符数和窗口内字符计数数组
    left, right = 0, 0  # 滑动窗口的左右边界初始都为0
    s1_chars_left = len(s1)  # 剩余需要匹配的字符数为 s1 的长度
    window_count = [0] * 26  # 初始化滑动窗口中每个字母的出现次数数组

    # 开始遍历 s2 字符串
    while right < len(s2):
        # 将右边界字符加入窗口计数
        right_char = s2[right]  # 获取当前右边界字符
        window_count[ord(right_char) - ord('a')] += 1  # 增加该字符在窗口中的计数

        # 如果该字符在 s1 中存在且匹配的数量不超过 s1 中的数量，减少剩余需要匹配的字符数
        if window_count[ord(right_char) - ord('a')] <= s1_count[ord(right_char) - ord('a')]:
            s1_chars_left -= 1

        # 如果窗口的长度大于 s1 长度 + k，移动左边界
        if right - left + 1 > len(s1) + k:
            left_char = s2[left]  # 获取当前左边界字符
            # 如果左边界字符在 s1 中存在且数量不超过 s1 中的数量，增加剩余需要匹配的字符数
            if window_count[ord(left_char) - ord('a')] <= s1_count[ord(left_char) - ord('a')]:
                s1_chars_left += 1
            # 将左边界字符从窗口计数中移除
            window_count[ord(left_char) - ord('a')] -= 1
            left += 1  # 左边界右移

        # 如果剩余需要匹配的字符数为0，返回满足条件的子串起始位置
        if s1_chars_left == 0:
            return left

        # 移动右边界
        right += 1

    # 如果遍历完 s2 仍未找到满足条件的子串，返回 -1
    return -1

   
s1 = input()   # 读取字符串 s1
s2 = input()   # 读取字符串 s2
k = int(input().strip())  # 读取并将字符串转换为整数的 k

# 调用查找函数并输出结果
print(find_redundant_cover(s1, s2, k))