"""
dp[i] 表示字符串 s 的前 i 个字符是否可以被拆分成字典中的单词
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        max_len = max(len(word) for word in wordDict) if wordDict else 0  # 计算最长单词的长度
        n = len(s)
        if not n:
            return False
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            # 原本是for j in range(0, i):
            # 剪枝：只遍历可能的拆分点, 如果子串s[j:i]长度超过字典中最大长度，则单一子串s[j:i]不可能在wordDict中，如果是拼合则会在后面的循环中处理
            # 所以有 i-j<=max_length, i - max_len<=j
            for j in range(max(0, i - max_len), i):  
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]