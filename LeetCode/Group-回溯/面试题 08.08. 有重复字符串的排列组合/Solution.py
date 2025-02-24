"""
统计字符频率：

使用 collections.Counter 统计字符串 S 中每个字符的出现次数。

回溯算法：

使用 backtrack 函数递归生成所有排列。
path 记录当前路径（即当前排列）。
counter 记录剩余可用字符的数量。

递归过程：

如果当前路径长度等于字符串长度，说明找到一个排列，将其加入结果列表。
遍历所有可用字符，选择当前字符并递归。
递归结束后，撤销选择，继续尝试其他字符。

返回结果：

返回所有不重复的排列组合。
"""
from collections import Counter
class Solution:
    def permutation(self, S: str) -> List[str]:
        def backtrack(path, counter):
            # 如果当前路径长度等于字符串长度，说明找到一个排列
            if len(path) == len(S):
                result.append(''.join(path))
                return

            for char in counter:
                if counter[char] > 0:
                    # 选择当前字符
                    path.append(char)
                    counter[char] -= 1

                    # 递归
                    backtrack(path, counter)

                    # 撤销选择,这样下一个循环就可以换另一个字符了
                    path.pop()
                    counter[char] += 1

        # 统计字符出现次数
        counter = Counter(S)
        result = []
        backtrack([], counter)
        return result