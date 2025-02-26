"""
dp[i][j] 表示以字符串 a 的第 i 个字符和字符串 b 的第 j 个字符为结尾的最长公共子串的长度
"""
def find_longest_common_substring(a, b):
    # 确保 a 是较短的字符串，因为如果存在多个答案，输出在较短串中最先出现的那个
    if len(a) > len(b):
        a, b = b, a

    # 初始化动态规划表
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0  # 记录最长公共子串的长度
    end_pos = 0  # 记录最长公共子串的结束位置

    # 填充动态规划表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                # 当前字符匹配，因此最长公共子串的长度可以在之前的基础上增加 1
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_pos = i  # 更新最长公共子串的结束位置
            else:
                dp[i][j] = 0  # 字符不匹配, 重置为0

    # 提取最长公共子串
    if max_len == 0:
        return ""  # 没有公共子串
    return a[end_pos - max_len:end_pos]

# 示例输入
a = input().strip()
b = input().strip()
result = find_longest_common_substring(a, b)
print(result) 