"""
使用动态规划，核心思想是构建一个二维 DP 表，其中 dp[i][j] 表示 text1 的前 i 个字符和 text2 的前 j 个字符的最长公共子序列的长度。

1. 定义状态：

    dp[i][j]：表示 text1 的前 i 个字符和 text2 的前 j 个字符的最长公共子序列的长度。

2. 状态转移：

    如果 text1[i - 1] == text2[j - 1]，则 dp[i][j] = dp[i - 1][j - 1] + 1。

    如果 text1[i - 1] != text2[j - 1]，则 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])。

3. 初始化：

    dp[0][j] = 0 和 dp[i][0] = 0，表示空字符串与任何字符串的最长公共子序列长度为 0。

4. 返回结果：

    dp[m][n]，其中 m 和 n 分别是 text1 和 text2 的长度。


用一维数组作为DP表，优化空间复杂度：
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    # 使用一维 DP 表
    dp = [0] * (n + 1)

    for i in range(1, m + 1):
        prev = 0  # 保存 dp[i-1][j-1] 的值
        for j in range(1, n + 1):
            temp = dp[j]  # 保存 dp[i-1][j] 的值
            if text1[i - 1] == text2[j - 1]:
                dp[j] = prev + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            prev = temp  # 更新 prev 为 dp[i-1][j]

    return dp[n]

"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_len = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) 
                    # 字符不匹配, dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) 表示当 text1[i - 1] 和 text2[j - 1] 不相等时，最长公共子序列的长度取决于忽略其中一个字符后的结果。
        return max_len
