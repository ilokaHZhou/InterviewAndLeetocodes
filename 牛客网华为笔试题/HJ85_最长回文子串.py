def getLongestPalindrome(A: str) -> int:
    if not A:
        return 0

    def expand_around_center(left, right):
        # 从中心向左右扩展，找到最长的回文子串
        while left >= 0 and right < len(A) and A[left] == A[right]:
            left -= 1
            right += 1
        return right - left - 1

    max_len = 0
    for i in range(len(A)):
        # 奇数长度的回文子串
        len1 = expand_around_center(i, i)
        # 偶数长度的回文子串
        len2 = expand_around_center(i, i + 1)
        # 更新最大长度
        max_len = max(max_len, len1, len2)

    return max_len

s = input().strip()
print(getLongestPalindrome(s))
