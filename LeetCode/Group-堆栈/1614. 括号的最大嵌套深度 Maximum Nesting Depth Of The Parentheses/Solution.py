"""
因为输入是有效的括号字符串不会出现多缺括号的情况，因此直接遍历找最大深度即可, 不用真用stack
"""
class Solution:
    def maxDepth(self, s: str) -> int:
        result, maxSize = 0, 0
        for c in s:
            if c == '(':
                result += 1
                maxSize = max(result, maxSize)
            if c == ')':
                result -= 1
        return maxSize