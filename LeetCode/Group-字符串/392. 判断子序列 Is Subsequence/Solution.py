# 双指针遍历主字符串找子串
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = t_index = 0
        while s_index < len(s) and t_index < len(t):
            if t[t_index] == s[s_index]:
                s_index += 1
            t_index += 1
        return s_index == len(s)
