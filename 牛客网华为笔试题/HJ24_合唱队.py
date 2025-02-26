"""
从两侧分别找最长的递增子序列
"""
def longest_increasing_subsequence(heights):
    dp = [1] * len(heights)  # dp[i] 表示以 heights[i] 结尾的最长递增子序列长度
    for i in range(1, len(heights)):  # 遍历数组
        for j in range(i):  # 检查前面的元素
            if heights[i] > heights[j]:  # 如果当前元素大于前面的元素
                dp[i] = max(dp[i], dp[j] + 1)  # 更新 dp[i]  状态转移！！
    return dp


def min_removals(heights):
    left = longest_increasing_subsequence(heights)  # 从左到右的最长递增子序列
    right = longest_increasing_subsequence(heights[::-1])[::-1]  # 从右到左的最长递增子序列
    max_len = 0
    for i in range(len(heights)):  # 遍历数组
        max_len = max(max_len, left[i] + right[i] - 1)  # 计算合唱队的最大长度
    return len(heights) - max_len  # 返回需要移除的人数


# 输入处理
n = int(input())
heights = list(map(int, input().split()))
print(min_removals(heights))
