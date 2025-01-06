# 反向遍历字符串，从结尾开始的第一个字母开始记录字母数，直到遇到空格或者index碰到字符串头
# 用python就简单多了hhh
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])