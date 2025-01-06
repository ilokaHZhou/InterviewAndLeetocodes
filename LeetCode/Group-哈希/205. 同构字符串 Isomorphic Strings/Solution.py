# s和t两个字符串里的字符应该是一一对应关系（双射），因此建两个哈希表分别表示单射和满射
# 同时遍历两个字符串，看是否有不属于哈希表映射关系的元素，元素不存在则添加
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}
        for a, b in zip(s, t):
            if a in s2t and s2t[a] != b or \
                b in t2s and t2s[b] != a:
                return False
            s2t[a] = b
            t2s[b] = a
        return True