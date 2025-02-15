class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        n = len(s)
        result = 0
        left = right = 0 # 窗口左右边界指针
        while right < n:
            ch = s[right]
            while ch in char_set: # 如果新字符在字串中已经出现过，缩短左边界并从set移除左侧元素，直到从左边界开始到右边界的连续子串中完全没有重复的新ch
                char_set.remove(s[left])
                left += 1
            char_set.add(ch) # 不要忘记新字符加入集合
            result = max(result, right - left + 1)
            right += 1
        return result