"""
经典滑动窗口题
需要两个边界指针，一个记录最小子串的长度的min_len，一个记录记录最小子串起始位置的start index
t中字符的哈希表，window的哈希表

最后是valid flag，意思是当前窗口中满足 need 条件的字符个数

先向右一直扩展窗口将整个s字符串包括在内，同时标记符合t中字符的个数
然后移动 left 指针收缩窗口，尝试找到更小的满足条件的子串。

通过比较两个哈希表来判断当前窗口是否满足条件。

使用一个变量 valid 记录当前窗口中已经满足 t 中字符条件的字符个数。
当 valid 等于 t 中不同字符的总数时，说明当前窗口满足条件。
"""
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        # 初始化哈希表
        need = defaultdict(int)  # 记录 t 中字符的频率
        window = defaultdict(int)  # 记录当前窗口中字符的频率
        for char in t:
            need[char] += 1

        # 初始化滑动窗口指针和结果
        left, right = 0, 0
        valid = 0  # 记录当前窗口中满足 need 条件的字符个数
        start = 0  # 记录最小子串的起始位置
        min_len = float('inf')  # 记录最小子串的长度

        # 滑动窗口
        while right < len(s):
            # 右移 right 指针，扩展窗口
            char = s[right]
            right += 1

            # 更新窗口数据
            if char in need:
                window[char] += 1
                if window[char] == need[char]:
                    valid += 1

            # 当窗口满足条件时，尝试收缩窗口
            while valid == len(need):
                # 更新最小子串
                if right - left < min_len:
                    min_len = right - left
                    start = left

                # 左移 left 指针，收缩窗口
                char = s[left]
                left += 1

                # 更新窗口数据
                if char in need:
                    if window[char] == need[char]:
                        valid -= 1
                    window[char] -= 1

        # 返回结果
        return "" if min_len == float('inf') else s[start:start + min_len]

