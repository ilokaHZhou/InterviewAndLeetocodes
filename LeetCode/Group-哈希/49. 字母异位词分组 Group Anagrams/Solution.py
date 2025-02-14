# 互为字母异位词的两个字符串包含的字母相同，因此字符串字母排序之后得到的字符串一定是相同的，故可以将排序之后的字符串作为哈希表的键
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        
        return list(mp.values())
