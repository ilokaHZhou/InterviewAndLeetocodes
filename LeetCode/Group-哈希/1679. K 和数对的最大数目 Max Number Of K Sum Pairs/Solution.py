# 两数之和进阶版，用dict（map）的哈希特性
# 哈希表取值用dict.get(key[, value]) 更简便，value是当key不存在时的默认值
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        records = dict()
        count = 0
        for v in nums:
            if records.get(k - v, 0) > 0:
                count += 1
                records[k-v] -= 1
            else:
                records[v] = records.get(v, 0) + 1
        return count