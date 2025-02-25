def longest_palindromic_substring(s):
    def expand_around_center(left, right):  # 中心扩展函数
        while left >= 0 and right < len(s) and s[left] == s[right]:  # 向左右扩展
            left -= 1
            right += 1
        return right - left - 1  # 返回回文子串的长度

    max_len = 0  # 最长回文子串的长度
    for i in range(len(s)):  # 遍历字符串
        len1 = expand_around_center(i, i)  # 奇数长度的回文子串
        len2 = expand_around_center(i, i + 1)  # 偶数长度的回文子串
        max_len = max(max_len, len1, len2)  # 更新最大长度
    return max_len  # 返回最长回文子串的长度


# 输入处理
s = input().strip()
print(longest_palindromic_substring(s))
