from itertools import zip_longest

# 一般解法用双指针即可
# zip_longest当多个输入iterables的长度不相等的时候，zip会按照最小的长度进行迭代处理，其余补fillvalue值
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))