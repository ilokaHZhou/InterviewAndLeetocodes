# 看子串翻转后是否还在原字符串即可
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(len(s) - 1):
            seg = s[i:i+2]
            if seg[::-1] in s:
                return True
        return False