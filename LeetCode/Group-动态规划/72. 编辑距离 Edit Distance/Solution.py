class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 获取两个字符串的长度
        m, n = len(word1), len(word2)

        # 创建一个二维数组 dp，dp[i][j] 表示 word1 前 i 个字符转换为 word2 前 j 个字符所需的最小操作次数
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 初始化第一行和第一列
        # dp[0][j] 表示将空字符串转换为 word2 前 j 个字符所需的操作次数，即插入 j 次
        for j in range(n + 1):
            dp[0][j] = j
        # dp[i][0] 表示将 word1 前 i 个字符转换为空字符串所需的操作次数，即删除 i 次
        for i in range(m + 1):
            dp[i][0] = i

        # 填充 dp 数组
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # 当前字符相同，不需要额外操作，操作次数等于前一个状态
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 当前字符不同，取插入、删除、替换操作中的最小操作次数加 1
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        # 输出结果，即 word1 转换为 word2 所需的最小操作次数
        return dp[m][n]